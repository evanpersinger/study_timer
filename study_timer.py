#!/usr/bin/env python3
"""
Study Timer - A Pomodoro-style timer for focused study sessions
Supports both 50/10 minute and 25/5 minute study/break intervals
"""

import time
import threading
import tkinter as tk
from tkinter import ttk
import platform
import subprocess
import os
import json
from datetime import datetime

# Import winsound only on Windows
if platform.system() == "Windows":
    import winsound


class StudyTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Study Timer")
        self.root.geometry("440x320")
        self.root.resizable(False, False)
        
        # Set dark theme colors
        self.root.configure(bg='black')
        
        # Timer settings
        self.study_duration = 25  # minutes
        self.break_duration = 5   # minutes
        self.is_running = False # indicates whether the timer is running
        
        # indicates whether the timer is in study time
        # true: study time, false: break time
        self.is_study_time = True 
        
        self.time_remaining = self.study_duration * 60  # seconds
        self.timer_thread = None
        self.sound_thread = None 
        self.playing_sound = False # indicates whether the sound is playing
        
        # Session tracking
        self.session_count = 0
        self.total_study_time = 0
        self.session_start_time = None  # Track when current session started
        
        # Data collection
        self.data_dir = "data"
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.data_file = os.path.join(self.data_dir, "data.json")
        self.load_data()
        
        # Setup UI
        self.setup_ui()
        self.update_display()
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        """Create the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure dark theme for ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='black', foreground='white')
        style.configure('TFrame', background='black')
        style.configure('TButton', background='gray20', foreground='white')
        style.configure('TLabelFrame', background='black', foreground='white')
        
        # Configure custom button hover effect with ring/border
        style.configure('TButton', relief='flat', borderwidth=1)
        style.map('TButton',
                  background=[('active', 'gray30')],  # Slightly lighter background on hover
                  foreground=[('active', 'white')],   # Keep white text
                  relief=[('active', 'solid')],        # Solid border on hover
                  borderwidth=[('active', '2')])       # 2px border on hover
        
        # Title
        title_label = ttk.Label(main_frame, text="Study Timer", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Timer display - dual clocks
        timer_frame = ttk.Frame(main_frame)
        timer_frame.grid(row=1, column=0, columnspan=2, pady=20)
        
        # Active timer (left) - shows current countdown
        self.active_label = ttk.Label(timer_frame, text="Study", font=("Arial", 14, "bold"))
        self.active_label.grid(row=0, column=0, padx=(0, 20))
        self.timer_label = ttk.Label(timer_frame, text="25:00", font=("Arial", 32, "bold"))
        self.timer_label.grid(row=1, column=0, padx=(0, 20))
        
        # Reference timer (right) - shows next timer duration
        self.reference_label = ttk.Label(timer_frame, text="Break", font=("Arial", 14, "bold"))
        self.reference_label.grid(row=0, column=1, padx=(20, 0))
        self.break_timer_label = ttk.Label(timer_frame, text="05:00", font=("Arial", 32, "bold"))
        self.break_timer_label.grid(row=1, column=1, padx=(20, 0))
        
        
        # Preset buttons
        preset_frame = ttk.Frame(main_frame)
        preset_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Button(preset_frame, text="25 min study / 5 min break", # 25 min button
                  command=self.set_25_5).grid(row=0, column=0, padx=5)
        ttk.Button(preset_frame, text="50 min study / 10 min break", # 50 min button
                  command=self.set_50_10).grid(row=0, column=1, padx=5)
        
        
        # Temporarily disabled test button
        """
        ttk.Button(preset_frame, text="TEST (10 sec)", # Test button
                  command=self.set_test).grid(row=0, column=2, padx=5)
        """
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        
        self.start_button = ttk.Button(control_frame, text="Start", command=self.toggle_timer) # Start button
        self.start_button.grid(row=0, column=0, padx=5)
        
        ttk.Button(control_frame, text="Reset", command=self.reset_timer).grid(row=0, column=1, padx=5) # Reset button
        
        # Break button (initially hidden)
        self.break_button = ttk.Button(control_frame, text="Start Break", command=self.start_break_timer)
        self.break_button.grid(row=0, column=2, padx=5)
        self.break_button.grid_remove()  # Hide initially
        
        # Study button (initially hidden)
        self.study_button = ttk.Button(control_frame, text="Start Study", command=self.start_study_timer)
        self.study_button.grid(row=0, column=3, padx=5)
        self.study_button.grid_remove()  # Hide initially
        
        
    
    def set_25_5(self):
        """Set timer to 25 minute study, 5 minute break"""
        if not self.is_running:
            self.study_duration = 25
            self.break_duration = 5
            self.reset_timer()
    
    def set_50_10(self):
        """Set timer to 50 minute study, 10 minute break"""
        if not self.is_running:
            self.study_duration = 50
            self.break_duration = 10
            self.reset_timer()
    
    def set_test(self):
        """Set timer to 10 second study, 10 second break (TEST MODE)"""
        if not self.is_running:
            self.study_duration = 10/60  # 10 seconds (10/60 minutes)
            self.break_duration = 10/60  # 10 seconds (10/60 minutes)
            self.reset_timer()
    
    def toggle_timer(self):
        """Start, pause, or stop the timer"""
        if self.start_button.cget("text") == "Start":
            self.start_timer()
        elif self.start_button.cget("text") == "Pause":
            self.pause_timer()
        elif self.start_button.cget("text") == "Stop":
            self.stop_timer()
    
    def start_timer(self):
        """Start the timer"""
        self.is_running = True
        self.start_button.config(text="Pause")
        
        # Set session start time if starting a study session
        if self.is_study_time and self.session_start_time is None:
            self.session_start_time = time.time()
        
        self.timer_thread = threading.Thread(target=self.timer_loop, daemon=True)
        self.timer_thread.start()
    
    def pause_timer(self):
        """Pause the timer"""
        self.is_running = False
        self.start_button.config(text="Start")
        self.stop_sound()
    
    def stop_timer(self):
        """Stop the timer and sound only"""
        self.is_running = False
        self.playing_sound = False
        self.stop_sound()
        
        # Add partial session time to total study time
        self.add_partial_session_time()
        
        # Just stop the sound, don't auto-start anything
        self.start_button.config(text="Start")
        self.update_display()
    
    def start_break_timer(self):
        """Start the break timer when user clicks the break button"""
        self.break_button.grid_remove()  # Hide the break button
        self.playing_sound = False  # Stop the notification sound
        self.stop_sound()
        
        # Add partial session time to total study time before switching to break
        self.add_partial_session_time()
        
        self.start_button.config(text="Pause")
        self.start_timer()
        self.update_display()
    
    def start_study_timer(self):
        """Start the study timer when user clicks the study button"""
        self.study_button.grid_remove()  # Hide the study button
        self.playing_sound = False  # Stop the notification sound
        self.stop_sound()
        
        # Add partial session time to total study time before starting new study session
        self.add_partial_session_time()
        
        self.start_button.config(text="Pause")
        self.start_timer()
        self.update_display()
    
    def reset_timer(self):
        """Reset the timer to initial state"""
        self.is_running = False
        
        # Add partial session time to total study time before resetting
        self.add_partial_session_time()
        
        self.is_study_time = True
        self.time_remaining = self.study_duration * 60
        self.start_button.config(text="Start")
        self.break_button.grid_remove()  # Hide break button
        self.study_button.grid_remove()  # Hide study button
        self.stop_sound()
        self.update_display()
    
    def timer_loop(self):
        """Main timer loop running in separate thread"""
        while self.is_running and self.time_remaining > 0:
            time.sleep(1)
            if self.is_running:
                self.time_remaining -= 1
                self.root.after(0, self.update_display)
        
        # Timer completed - call completion handler
        if self.time_remaining == 0:
            self.root.after(0, self.timer_complete)
    
    def timer_complete(self):
        """Handle timer completion"""
        self.is_running = False
        self.start_button.config(text="Stop")
        
        if self.is_study_time:
            # Study session completed
            self.session_count += 1
            self.total_study_time += self.study_duration
            self.save_data()  # Save data after each study session
            self.play_notification_sound()
            
            # Reset session start time since session completed naturally
            self.session_start_time = None
            
            # Switch to break mode and prepare break timer
            self.is_study_time = False
            self.time_remaining = self.break_duration * 60
            
            # Show break button instead of auto-starting
            self.break_button.grid()
        else:
            # Break completed
            self.play_notification_sound()
            
            # Switch to study mode and prepare study timer
            self.is_study_time = True
            self.time_remaining = self.study_duration * 60
            
            # Hide break button and show Start Study button (don't auto-start)
            self.break_button.grid_remove()
            self.study_button.grid()
            self.start_button.config(text="Start")
        
        self.update_display()
    
    def play_notification_sound(self):
        """Start playing notification sound continuously"""
        if not self.playing_sound:
            self.playing_sound = True
            self.sound_thread = threading.Thread(target=self.sound_loop, daemon=True)
            self.sound_thread.start()
    
    def get_sound_for_duration(self):
        """Get the appropriate sound based on study duration"""
        # For test mode (5 seconds), use Glass sound
        if self.study_duration <= 0.1:  # Test mode (5 seconds or less)
            return "/System/Library/Sounds/Glass.aiff"
        elif self.study_duration == 25:
            return "/System/Library/Sounds/Glass.aiff"  # Glass sound for 25 min
        else:
            return "/System/Library/Sounds/Ping.aiff"   # Ping sound for 50 min
    
    def sound_loop(self):
        """Play sound continuously until stopped"""
        try:
            if platform.system() == "Windows":
                while self.playing_sound:
                    winsound.Beep(1000, 200)  # 1000 Hz for 200ms (shorter beep)
                    time.sleep(0.1)  # Wait 0.1 seconds between beeps
            elif platform.system() == "Darwin":  # macOS
                # Get the appropriate sound based on study duration
                working_sound = self.get_sound_for_duration()
                print(f"Playing sound: {working_sound}")  # Debug
                
                while self.playing_sound:
                    result = subprocess.run(["afplay", working_sound], capture_output=True, text=True)
                    if result.returncode != 0:
                        print(f"Sound failed: {result.stderr}")
                        # Fallback to system beep
                        subprocess.run(["osascript", "-e", "beep"], capture_output=True)
                    time.sleep(0.1)  # Wait 0.1 seconds between sounds
            else:  # Linux
                while self.playing_sound:
                    subprocess.run(["paplay", "/usr/share/sounds/alsa/Front_Left.wav"], capture_output=True)
                    time.sleep(0.1)  # Wait 0.1 seconds between sounds
        except Exception as e:
            print(f"Sound error: {e}")
    
    def stop_sound(self):
        """Stop playing notification sound"""
        self.playing_sound = False
    
    def add_partial_session_time(self):
        """Add partial session time to total study time if in study mode"""
        if self.is_study_time and self.session_start_time is not None:
            # Calculate how much study time was completed
            elapsed_time = time.time() - self.session_start_time
            elapsed_minutes = elapsed_time / 60
            
            # Add to total study time
            self.total_study_time += elapsed_minutes
            print(f"Added {elapsed_minutes:.2f} minutes of partial session to total study time")
            
            # Save the updated data
            self.save_data()
            
            # Reset session start time
            self.session_start_time = None
    
    def load_data(self):
        """Load today's study data from file"""
        try:
            # Create data directory if it doesn't exist
            if not os.path.exists(self.data_dir):
                os.makedirs(self.data_dir)
                print(f"Created data directory: {self.data_dir}")
            
            # Load data
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    all_data = json.load(f)
                    
                # Check if we have data for today
                if self.today in all_data:
                    today_data = all_data[self.today]
                    self.session_count = today_data.get('session_count', 0)
                    self.total_study_time = today_data.get('total_study_time', 0)
                    print(f"Loaded today's data: {self.session_count} sessions, {self.total_study_time} minutes")
                else:
                    print(f"No data found for today ({self.today}), starting fresh")
                    self.session_count = 0
                    self.total_study_time = 0
            else:
                print(f"No data file found, starting fresh")
                self.session_count = 0
                self.total_study_time = 0
        except Exception as e:
            print(f"Error loading data: {e}")
            # Start fresh if there's an error
            self.session_count = 0
            self.total_study_time = 0
    
    def save_data(self):
        """Save today's study data to file"""
        try:
            # Load existing data
            all_data = {}
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    all_data = json.load(f)
            
            # Update today's data
            all_data[self.today] = {
                'session_count': self.session_count,
                'total_study_time': self.total_study_time,
                'last_updated': datetime.now().isoformat()
            }
            
            # Save all data back to file
            with open(self.data_file, 'w') as f:
                json.dump(all_data, f, indent=2)
            print(f"Saved today's data: {self.session_count} sessions, {self.total_study_time} minutes")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    
    
    def on_closing(self):
        """Handle window closing - stop all sounds and threads"""
        self.is_running = False
        self.playing_sound = False
        self.save_data()  # Save data before closing
        self.root.destroy()
    
    
    def update_display(self):
        """Update the timer display"""
        # Always keep Study on left, Break on right
        self.active_label.config(text="Study")
        self.reference_label.config(text="Break")
        
        if self.is_study_time:
            # Study mode - show study countdown on left, break duration on right
            minutes = int(self.time_remaining // 60)
            seconds = int(self.time_remaining % 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            break_minutes = int(self.break_duration)
            break_seconds = int((self.break_duration % 1) * 60)
            self.break_timer_label.config(text=f"{break_minutes:02d}:{break_seconds:02d}")
        else:
            # Break mode - show study duration on left, break countdown on right
            study_minutes = int(self.study_duration)
            study_seconds = int((self.study_duration % 1) * 60)
            self.timer_label.config(text=f"{study_minutes:02d}:{study_seconds:02d}")
            
            minutes = int(self.time_remaining // 60)
            seconds = int(self.time_remaining % 60)
            self.break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    
    
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main function to run the study timer"""
    print("Starting Study Timer...")
    print("Available presets:")
    print("- 25 minute study / 5 minute break")
    print("- 50 minute study / 10 minute break ")
    print()
    
    app = StudyTimer()
    app.run()


if __name__ == "__main__":
    main()

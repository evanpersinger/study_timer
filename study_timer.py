#!/usr/bin/env python3
"""
Study Timer - A Pomodoro-style timer for focused study sessions
Supports both 50/10 minute and 25/5 minute study/break intervals
"""

import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import subprocess
import os
from datetime import datetime, timedelta

# Import winsound only on Windows
if platform.system() == "Windows":
    import winsound


class StudyTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Study Timer")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Timer settings
        self.study_duration = 25  # minutes
        self.break_duration = 5   # minutes
        self.is_running = False
        self.is_study_time = True
        self.time_remaining = self.study_duration * 60  # seconds
        self.timer_thread = None
        self.sound_thread = None
        self.playing_sound = False
        
        # Session tracking
        self.session_count = 0
        self.total_study_time = 0
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        """Create the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Study Timer", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Timer display
        self.timer_label = ttk.Label(main_frame, text="25:00", font=("Arial", 32, "bold"))
        self.timer_label.grid(row=1, column=0, columnspan=2, pady=20)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready to Study", font=("Arial", 12))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        
        # Preset buttons
        preset_frame = ttk.Frame(main_frame)
        preset_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Button(preset_frame, text="25 min Study / 5 min Break", 
                  command=self.set_25_5).grid(row=0, column=0, padx=5)
        ttk.Button(preset_frame, text="50 min Study / 10 min Break", 
                  command=self.set_50_10).grid(row=0, column=1, padx=5)
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        
        self.start_button = ttk.Button(control_frame, text="Start", command=self.toggle_timer)
        self.start_button.grid(row=0, column=0, padx=5)
        
        ttk.Button(control_frame, text="Reset", command=self.reset_timer).grid(row=0, column=1, padx=5)
        
        # Session info
        info_frame = ttk.LabelFrame(main_frame, text="Session Info", padding="10")
        info_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.session_label = ttk.Label(info_frame, text="Sessions: 0")
        self.session_label.grid(row=0, column=0, sticky=tk.W)
        
        self.total_time_label = ttk.Label(info_frame, text="Total Study: 0:00")
        self.total_time_label.grid(row=1, column=0, sticky=tk.W)
    
    def set_25_5(self):
        """Set timer to 25 minute study, 5 minute break"""
        if not self.is_running:
            self.study_duration = 25
            self.break_duration = 5
            self.reset_timer()
            self.status_label.config(text="25 min Study / 5 min Break")
    
    def set_50_10(self):
        """Set timer to 50 minute study, 10 minute break"""
        if not self.is_running:
            self.study_duration = 50
            self.break_duration = 10
            self.reset_timer()
            self.status_label.config(text="50 min Study / 10 min Break")
    
    def toggle_timer(self):
        """Start or pause the timer"""
        if not self.is_running:
            self.start_timer()
        else:
            self.pause_timer()
    
    def start_timer(self):
        """Start the timer"""
        self.is_running = True
        self.start_button.config(text="Pause")
        self.timer_thread = threading.Thread(target=self.timer_loop, daemon=True)
        self.timer_thread.start()
    
    def pause_timer(self):
        """Pause the timer"""
        self.is_running = False
        self.start_button.config(text="Start")
        self.stop_sound()
    
    def reset_timer(self):
        """Reset the timer to initial state"""
        self.is_running = False
        self.is_study_time = True
        self.time_remaining = self.study_duration * 60
        self.start_button.config(text="Start")
        self.stop_sound()
        self.update_display()
        self.status_label.config(text="Ready to Study")
    
    def timer_loop(self):
        """Main timer loop running in separate thread"""
        while self.is_running and self.time_remaining > 0:
            time.sleep(1)
            if self.is_running:
                self.time_remaining -= 1
                self.root.after(0, self.update_display)
        
        if self.time_remaining == 0 and self.is_running:
            self.root.after(0, self.timer_complete)
    
    def timer_complete(self):
        """Handle timer completion"""
        self.is_running = False
        self.start_button.config(text="Start")
        
        if self.is_study_time:
            # Study session completed
            self.session_count += 1
            self.total_study_time += self.study_duration
            self.play_notification_sound()
            self.show_completion_message("Study session complete! Time for a break.")
            
            # Switch to break
            self.is_study_time = False
            self.time_remaining = self.break_duration * 60
            self.status_label.config(text=f"Break Time - {self.break_duration} minutes")
        else:
            # Break completed
            self.play_notification_sound()
            self.show_completion_message("Break over! Ready to study again.")
            
            # Switch to study
            self.is_study_time = True
            self.time_remaining = self.study_duration * 60
            self.status_label.config(text=f"Study Time - {self.study_duration} minutes")
        
        self.update_display()
        self.update_session_info()
    
    def play_notification_sound(self):
        """Start playing notification sound continuously"""
        if not self.playing_sound:
            self.playing_sound = True
            self.sound_thread = threading.Thread(target=self.sound_loop, daemon=True)
            self.sound_thread.start()
    
    def sound_loop(self):
        """Play sound continuously until stopped"""
        try:
            if platform.system() == "Windows":
                while self.playing_sound:
                    winsound.Beep(1000, 500)  # 1000 Hz for 500ms
                    time.sleep(1)  # Wait 1 second between beeps
            elif platform.system() == "Darwin":  # macOS
                # Try multiple Mac sound options
                sounds = [
                    "/System/Library/Sounds/Glass.aiff",
                    "/System/Library/Sounds/Ping.aiff", 
                    "/System/Library/Sounds/Submarine.aiff",
                    "/System/Library/Sounds/Basso.aiff"
                ]
                working_sound = None
                for sound in sounds:
                    try:
                        subprocess.run(["afplay", sound], check=True, capture_output=True)
                        working_sound = sound
                        break
                    except:
                        continue
                
                if not working_sound:
                    working_sound = "beep"  # Fallback to system beep
                
                while self.playing_sound:
                    if working_sound == "beep":
                        subprocess.run(["osascript", "-e", "beep"], capture_output=True)
                    else:
                        subprocess.run(["afplay", working_sound], capture_output=True)
                    time.sleep(2)  # Wait 2 seconds between sounds
            else:  # Linux
                while self.playing_sound:
                    subprocess.run(["paplay", "/usr/share/sounds/alsa/Front_Left.wav"], capture_output=True)
                    time.sleep(2)
        except Exception as e:
            print(f"Sound error: {e}")
    
    def stop_sound(self):
        """Stop playing notification sound"""
        self.playing_sound = False
    
    def show_completion_message(self, message):
        """Show completion message"""
        messagebox.showinfo("Timer Complete", message)
    
    def update_display(self):
        """Update the timer display"""
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    
    def update_session_info(self):
        """Update session information display"""
        self.session_label.config(text=f"Sessions: {self.session_count}")
        
        total_hours = self.total_study_time // 60
        total_minutes = self.total_study_time % 60
        self.total_time_label.config(text=f"Total Study: {total_hours}:{total_minutes:02d}")
    
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

import json
import os
import threading
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import ttk, messagebox, filedialog

try:
    from plyer import notification
except Exception:
    notification = None

try:
    from playsound import playsound
except Exception:
    playsound = None

import platform
if platform.system() == 'Windows':
    import winsound

APP_TITLE = "Reminder App"
CHECK_INTERVAL_SECONDS = 15

# reminder app
class ReminderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("730x598")
        self.resizable(False, False)

        self.reminders = []
        self.checking = False
        self.check_job = None

        self.build_ui()

    def build_ui(self):
        pad = {"padx": 10, "pady": 7}
        frm = ttk.Frame(self)
        frm.pack(fill="x", **pad)

        # Inputs
        ttk.Label(frm, text="Task").grid(row=0, column=0, sticky="w")
        self.task_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.task_var, width=20).grid(row=0, column=1, sticky="w", **pad)

        ttk.Label(frm, text="Date (YYYY-MM-DD)").grid(row=1, column=0, sticky="w")
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(frm, textvariable=self.date_var, width=20).grid(row=1, column=1, sticky="w", **pad)

        ttk.Label(frm, text="Time (24h HH:MM)").grid(row=2, column=0, sticky="w")
        self.time_var = tk.StringVar(value=(datetime.now() + timedelta(minutes=2)).strftime("%H:%M"))
        ttk.Entry(frm, textvariable=self.time_var, width=20).grid(row=2, column=1, sticky="w", **pad)

        ttk.Label(frm, text="Repeat").grid(row=3, column=0, sticky="w")
        self.repeat_var = tk.StringVar(value="None")
        repeat_cb = ttk.Combobox(frm, textvariable=self.repeat_var, width=18, state="readonly",
                                 values=["None", "Daily", "Weekly", "Monthly"])
        repeat_cb.grid(row=3, column=1, sticky="w", **pad)

        # Buttons
        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)

        ttk.Button(btns, text="Add", command=self.add_reminder).pack(side="left", padx=5)
        ttk.Button(btns, text="Delete", command=self.delete_selected).pack(side="left", padx=5)
        ttk.Button(btns, text="Snooze 5 min", command=self.snooze_selected).pack(side="left", padx=5)
        ttk.Button(btns, text="Save", command=self.save_to_file).pack(side="left", padx=5)
        ttk.Button(btns, text="Load", command=self.load_from_file).pack(side="left", padx=5)

        self.start_btn = ttk.Button(btns, text="Start", command=self.start_checking)
        self.start_btn.pack(side="right", padx=5)
        self.stop_btn = ttk.Button(btns, text="Stop", command=self.stop_checking, state="disabled")
        self.stop_btn.pack(side="right", padx=5)

        # Table
        table_frame = ttk.Frame(self)
        table_frame.pack(fill="both", expand=True, **pad)

        cols = ("task", "date", "time", "repeat", "status")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=15)
        for c, w in zip(cols, (320, 110, 90, 90, 120)):
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, width=w, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(self, textvariable=self.status_var, anchor="w").pack(fill="x", padx=10, pady=5)

    # -----------------------------
    # Helper methods
    # -----------------------------
    def refresh_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for idx, r in enumerate(self.reminders):
            status = "Done" if r.get('done') else "Pending"
            values = (r["task"], r["date"], r["time"], r['repeat'], status)
            self.tree.insert("", "end", iid=str(idx), values=values)

    def validate_datetime(self, date_str, time_str):
        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            return dt
        except ValueError:
            return None

    def notify(self, title, message):
        if notification:
            try:
                notification.notify(title=title, message=message, timeout=10)
            except Exception:
                pass

        try:
            messagebox.showinfo(title=title, message=message)
        except Exception:
            pass

        try:
            if platform.system() == "Windows":
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            elif playsound and os.path.exists("alarm.mp3"):
                threading.Thread(target=lambda: playsound("alarm.mp3"), daemon=True).start()
        except Exception:
            pass

    # -----------------------------
    # Reminder management
    # -----------------------------
    def add_reminder(self):
        task = self.task_var.get().strip()
        date = self.date_var.get().strip()
        time = self.time_var.get().strip()
        repeat = self.repeat_var.get()

        if not task:
            messagebox.showwarning("Validation", "Please enter a task")
            return

        dt = self.validate_datetime(date, time)
        if not dt:
            messagebox.showwarning("Validation", "Invalid date or time format")
            return

        self.reminders.append({
            "task": task,
            "date": date,
            "time": time,
            "repeat": repeat,
            "done": False,
            "created_at": datetime.now().isoformat()
        })

        self.refresh_table()
        self.status_var.set(f"Added {task} at {date} {time}")

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Delete", "Select a reminder from the list")
            return

        idx = int(sel[0])
        task = self.reminders[idx]["task"]
        del self.reminders[idx]
        self.refresh_table()
        self.status_var.set(f"Deleted: {task}")

    def snooze_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Snooze", "Select a reminder from the list")
            return

        idx = int(sel[0])
        r = self.reminders[idx]
        dt = self.validate_datetime(r["date"], r["time"])
        if not dt:
            messagebox.showwarning("Snooze", "Invalid date/time on selected reminder")
            return

        dt += timedelta(minutes=5)
        r["date"] = dt.strftime("%Y-%m-%d")
        r["time"] = dt.strftime("%H:%M")
        r["done"] = False
        self.refresh_table()
        self.status_var.set(f"Snoozed 5 min: {r['task']} at {r['date']} {r['time']}")

    def save_to_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON", "*.json")], title="Save Reminders")
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.reminders, f, ensure_ascii=False, indent=2)
            self.status_var.set(f"Saved {len(self.reminders)} reminders to {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Save error", str(e))

    def load_from_file(self):
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")], title="Load Reminders")
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Invalid file format")
                self.reminders = []
                for r in data:
                    self.reminders.append({
                        "task": r.get("task", "Untitled"),
                        "date": r.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "time": r.get("time", (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")),
                        "repeat": r.get("repeat", "None"),
                        "done": r.get("done", False),
                        "created_at": r.get("created_at", datetime.now().isoformat())
                    })
                self.refresh_table()
                self.status_var.set(f"Loaded {len(self.reminders)} reminders from {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Load error", str(e))

    # -----------------------------
    # Reminder checking
    # -----------------------------
    def start_checking(self):
        if self.checking:
            return
        self.checking = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_var.set("Reminder checker: RUNNING")
        self.schedule_check()

    def stop_checking(self):
        self.checking = False
        if self.check_job:
            self.after_cancel(self.check_job)
            self.check_job = None
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_var.set("Reminder checker stopped")

    def schedule_check(self):
        if not self.checking:
            return
        self.check_reminders()
        self.check_job = self.after(CHECK_INTERVAL_SECONDS * 1000, self.schedule_check)

    def check_reminders(self):
        now = datetime.now()
        fired_any = False

        for r in self.reminders:
            if r.get("done"):
                continue

            dt = self.validate_datetime(r["date"], r["time"])
            if not dt:
                continue

            if now >= dt:
                fired_any = True
                msg = f"{r['task']} scheduled at {r['date']} {r['time']}"
                self.notify("Reminder", msg)

                if r['repeat'] == "Daily":
                    dt_next = dt + timedelta(days=1)
                    r['date'] = dt_next.strftime('%Y-%m-%d')
                    r['time'] = dt_next.strftime('%H:%M')
                elif r['repeat'] == "Weekly":
                    dt_next = dt + timedelta(weeks=1)
                    r['date'] = dt_next.strftime('%Y-%m-%d')
                    r['time'] = dt_next.strftime('%H:%M')
                elif r['repeat'] == "Monthly":
                    dt_next = dt + timedelta(days=30)
                    r['date'] = dt_next.strftime('%Y-%m-%d')
                    r['time'] = dt_next.strftime('%H:%M')
                else:
                    r['done'] = True

        if fired_any:
            self.refresh_table()
            self.status_var.set("Reminder fired")


# -----------------------------
# Main
# -----------------------------
def main():
    app = ReminderApp()
    app.mainloop()


if __name__ == "__main__":
    main()

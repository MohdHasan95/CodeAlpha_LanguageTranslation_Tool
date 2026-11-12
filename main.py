"""CodeAlpha Task 1: Language Translation Tool."""
import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import MyMemoryTranslator

LANGUAGES = {
    "Arabic": "ar-SA", "Bengali": "bn-BD",
    "Chinese (Simplified)": "zh-CN", "Dutch": "nl-NL",
    "English": "en-GB", "French": "fr-FR",
    "German": "de-DE", "Gujarati": "gu-IN",
    "Hindi": "hi-IN", "Italian": "it-IT",
    "Japanese": "ja-JP", "Korean": "ko-KR",
    "Marathi": "mr-IN", "Nepali": "ne-NP",
    "Portuguese": "pt-PT", "Punjabi": "pa-IN",
    "Russian": "ru-RU", "Spanish": "es-ES",
    "Tamil": "ta-IN", "Urdu": "ur-PK"
}

class TranslationApp:
    def __init__(self, root):
        self.root = root
        root.title("CodeAlpha | Language Translation Tool")
        root.geometry("780x620")
        root.minsize(620, 520)
        root.configure(bg="#f1f5f9")

        title = tk.Label(root, text="Language Translation Tool",
                         font=("Segoe UI", 22, "bold"), bg="#f1f5f9", fg="#0f172a")
        title.pack(pady=(22, 5))
        tk.Label(root, text="CodeAlpha Artificial Intelligence Internship - Task 1",
                 font=("Segoe UI", 10), bg="#f1f5f9", fg="#64748b").pack(pady=(0, 18))

        controls = tk.Frame(root, bg="#f1f5f9")
        controls.pack(fill="x", padx=25)
        self.source = tk.StringVar(value="English")
        self.target = tk.StringVar(value="Hindi")
        tk.Label(controls, text="From", bg="#f1f5f9").grid(row=0, column=0, sticky="w")
        tk.Label(controls, text="To", bg="#f1f5f9").grid(row=0, column=2, sticky="w")
        names = [name for name in LANGUAGES if name != "Auto Detect"]
        self.from_box = ttk.Combobox(controls, values=names, textvariable=self.source, state="readonly")
        self.from_box.grid(row=1, column=0, sticky="ew", padx=(0, 12), pady=7)
        ttk.Button(controls, text="⇄ Swap", command=self.swap).grid(row=1, column=1, padx=8)
        self.to_box = ttk.Combobox(controls, values=names, textvariable=self.target, state="readonly")
        self.to_box.grid(row=1, column=2, sticky="ew", padx=(12, 0), pady=7)
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(2, weight=1)

        tk.Label(root, text="Enter text", bg="#f1f5f9", fg="#334155",
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=25, pady=(12, 5))
        self.input_text = tk.Text(root, height=7, wrap="word", font=("Segoe UI", 11),
                                  relief="solid", bd=1)
        self.input_text.pack(fill="both", expand=True, padx=25)

        buttons = tk.Frame(root, bg="#f1f5f9")
        buttons.pack(pady=14)
        ttk.Button(buttons, text="Translate", command=self.translate).pack(side="left", padx=6)
        ttk.Button(buttons, text="Clear", command=self.clear).pack(side="left", padx=6)
        ttk.Button(buttons, text="Copy Result", command=self.copy_result).pack(side="left", padx=6)

        tk.Label(root, text="Translation", bg="#f1f5f9", fg="#334155",
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=25, pady=(3, 5))
        self.output_text = tk.Text(root, height=7, wrap="word", font=("Segoe UI", 11),
                                   relief="solid", bd=1, state="disabled")
        self.output_text.pack(fill="both", expand=True, padx=25, pady=(0, 8))
        self.status = tk.StringVar(value="Ready. Internet connection required.")
        tk.Label(root, textvariable=self.status, bg="#f1f5f9", fg="#64748b").pack(pady=(0, 12))

    def set_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.config(state="disabled")

    def translate(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Missing text", "Please enter text to translate.")
            return
        if len(text) > 450:
            messagebox.showwarning("Too long", "Please enter 450 characters or fewer.")
            return
        try:
            self.status.set("Translating...")
            self.root.update_idletasks()
            if self.source.get() == self.target.get():
                self.set_output(text)
                self.status.set("Source and target are the same.")
                return
            result = MyMemoryTranslator(
                source=LANGUAGES[self.source.get()],
                target=LANGUAGES[self.target.get()]
            ).translate(text)
            self.set_output(result or "")
            self.status.set("Translation complete.")
        except Exception as exc:
            self.status.set("Translation failed.")
            messagebox.showerror("Translation error",
                                 f"Translation service could not complete the request.\n\nDetails: {exc}")

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.set_output("")
        self.status.set("Ready.")

    def copy_result(self):
        result = self.output_text.get("1.0", "end-1c")
        if not result.strip():
            messagebox.showinfo("Nothing to copy", "Translate some text first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        self.status.set("Translation copied to clipboard.")

    def swap(self):
        previous_source, previous_target = self.source.get(), self.target.get()
        self.source.set(previous_target)
        self.target.set(previous_source)
        result = self.output_text.get("1.0", "end-1c")
        if result.strip():
            self.input_text.delete("1.0", "end")
            self.input_text.insert("1.0", result)
            self.set_output("")

if __name__ == "__main__":
    window = tk.Tk()
    TranslationApp(window)
    window.mainloop()

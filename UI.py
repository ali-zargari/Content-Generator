import tkinter as tk
from tkinter import messagebox
from Scraper import scrapeRedditPostByURL
from text_gen import gpt_summarize


class GuiApplication:

    def __init__(self, root):
        self.root = root
        self.root.title("URL Processor")

        # Set window size
        self.root.geometry("400x200")

        # Give some padding to widgets
        self.root.configure(padx=10, pady=10)

        # Create a label and a text box for URL entry with some styling
        tk.Label(self.root, text="URL:", font=("Arial", 14)).pack(pady=10)

        # Store this Entry widget, so we can get its content later
        self.url_entry = tk.Entry(self.root, font=("Arial", 12), width=50)
        self.url_entry.pack(pady=10)

        # Create a 'Process' button which will get info and destroy window when clicked
        tk.Button(self.root,
                  text="Process URL",
                  command=self.process_url,
                  bg="#20987E",  # Button color
                  fg="#FFFFFF",  # Text color
                  font=("Arial", 12),
                  width=15,
                  height=1
                  ).pack(pady=10)

    def process_url(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showinfo("Error", "URL is required!")
            return

        # ... Put here your URL processing logic
        # You might want to consider using a separate thread
        # for the processing logic so that the UI doesn't hang

        print(gpt_summarize(scrapeRedditPostByURL(url)))

        messagebox.showinfo("Success", "URL processing completed!")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiApplication(root)
    root.mainloop()

import tkinter as tk
from vulnerability_analyzer import VulnerabilityAnalyzer

def main():
    root = tk.Tk()
    analyzer = VulnerabilityAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

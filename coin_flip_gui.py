import tkinter as tk
from tkinter import ttk
import random

class CoinFlipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coin Flip MTG")
        self.root.geometry("400x300")
        
        # Variable for number of coins per flip
        self.coins_per_flip = tk.IntVar(value=1)
        
        # Results display
        self.results_text = tk.Text(root, height=10, width=40, state='disabled')
        self.results_text.pack(pady=10)
        
        # Input frame
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="Coins per flip:").pack(side=tk.LEFT, padx=5)
        self.coins_spinbox = ttk.Spinbox(
            input_frame,
            from_=1,
            to=100,
            textvariable=self.coins_per_flip,
            width=10
        )
        self.coins_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Buttons frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Flip Once", command=self.flip_once).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Flip X Times", command=self.flip_x_times).pack(side=tk.LEFT, padx=5)
        
        # Flip until frame
        until_frame = ttk.Frame(root)
        until_frame.pack(pady=10)
        
        ttk.Label(until_frame, text="Flip until heads count:").pack(side=tk.LEFT, padx=5)
        self.until_spinbox = ttk.Spinbox(
            until_frame,
            from_=1,
            to=100,
            width=10
        )
        self.until_spinbox.pack(side=tk.LEFT, padx=5)
        ttk.Button(until_frame, text="Flip Until", command=self.flip_until).pack(side=tk.LEFT, padx=5)
        
        # Clear button
        ttk.Button(root, text="Clear Results", command=self.clear_results).pack(pady=5)
    
    def flip_once(self):
        coins = self.coins_per_flip.get()
        results = [random.choice(['H', 'T']) for _ in range(coins)]
        self.display_results(f"Flip Once ({coins} coin(s)): {' '.join(results)}")
    
    def flip_x_times(self):
        coins = self.coins_per_flip.get()
        self.display_results(f"--- Flip {coins} Coins ---")
        for i in range(coins):
            results = [random.choice(['H', 'T']) for _ in range(coins)]
            self.display_results(f"Flip {i+1}: {' '.join(results)}")
    
    def flip_until(self):
        target_heads = int(self.until_spinbox.get())
        coins = self.coins_per_flip.get()
        heads_count = 0
        flip_count = 0
        
        self.display_results(f"--- Flip until {target_heads} heads (flipping {coins} coin(s) per flip) ---")
        
        while heads_count < target_heads:
            flip_count += 1
            results = [random.choice(['H', 'T']) for _ in range(coins)]
            heads = results.count('H')
            heads_count += heads
            self.display_results(f"Flip {flip_count}: {' '.join(results)} | Total heads: {heads_count}")
    
    def display_results(self, text):
        self.results_text.config(state='normal')
        self.results_text.insert(tk.END, text + '\n')
        self.results_text.see(tk.END)
        self.results_text.config(state='disabled')
    
    def clear_results(self):
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()
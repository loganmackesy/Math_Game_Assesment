import tkinter as tk
import random

#add images(PILLOW), colours, laderboard, harder questions.

app = tk.Tk()
app.title("Mental Math Trainer")
app.geometry("420x480")  

game_info = {
    'player': "Guest",  # defualt name
    'current_mode': "",  
    'right_answer': 0
}

def clear_screen():  # clears all widgets
    for widget in app.winfo_children():
        widget.destroy()

def show_intro():  # first screen user sees
    clear_screen()
   
    
    tk.Label(app, text="Mental Math Trainer", font=("Arial", 22)).pack(pady=35)
   
    tk.Label(app, text="Enter your name :").pack()  #
    name_box = tk.Entry(app, width=25)  
    name_box.pack()
   
    
    tk.Button(app, text="Begin",
             command=lambda: show_modes(name_box.get())).pack(pady=30)

def show_modes(name=None):  
    clear_screen()
    if name and name.strip():  # only update if name provided
        game_info['player'] = name.strip()
   
    # Greeting mesage 
    tk.Label(app, text=f"Hi {game_info['player']}! Choose mode:",
            font=("Arial", 14)).pack(pady=25)
   
    
    tk.Button(app, text="Addition",
             command=lambda: start_game('add'),
             height=2, width=14).pack(pady=8)
    tk.Button(app, text="Subtraction", 
             command=lambda: start_game('sub'),
             height=2, width=14).pack(pady=8)

def start_game(mode):  # start the game
    clear_screen()
    game_info['current_mode'] = mode
   
    
    if mode == 'add':
        a = random.randint(12, 50)  
        b = random.randint(12, 50)
        game_info['right_answer'] = a + b
        problem = f"{a} + {b} = ?"
    else:  # sub
        a = random.randint(25, 60)
        b = random.randint(10, 24) #no negatives
        game_info['right_answer'] = a - b
        problem = f"{a} - {b} = ?"
   
    # Problem display
    tk.Label(app, text=problem, font=("Arial", 24)).pack(pady=45)  #
    
    ans_entry = tk.Entry(app, font=("Arial", 14), width=10)  
    ans_entry.pack()
    ans_entry.focus()
   
    
    tk.Button(app, text="Check",
             command=lambda: check_ans(ans_entry.get())).pack(pady=20)

def check_ans(answer):  
    clear_screen()
   
    try:
        user_num = int(answer)
    except:  # bare except
        user_num = None
   
    if user_num == game_info['right_answer']:
        result = "Correct! Well done."  
        color = "#4CAF50"  
    else:
        result = f"Wrong. Answer: {game_info['right_answer']}"  
        color = "#F44336"
   
    tk.Label(app, text=result, fg=color,
            font=("Arial", 14)).pack(pady=40)
   
    
    tk.Button(app, text="Same Type",
             command=lambda: start_game(game_info['current_mode']),
             bg="#2196F3").pack(side=tk.LEFT, padx=15)
    tk.Button(app, text="New Mode",
             command=lambda: show_modes(),  
             bg="#2196F3").pack(side=tk.RIGHT, padx=15)

# Main game loop 
show_intro()
app.mainloop()

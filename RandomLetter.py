import tkinter as tk
import random

root = tk.Tk()
root.title("Random")
root.geometry('300x250')
def random_gen():
    a = random.choice(['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Azir', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Cassiopeia', 'ChoGath', 'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'KhaZix', 'KogMaw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturn', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus', 'RekSai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Syndra', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'VelKoz', 'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra', 'aphelios', 'aurelion sol', 'bard', 'Camille', 'ekko', 'illaoi', 'ivern', 'kaisa', 'jhin', 'kayne', 'kindred', 'kled', 'lillia', 'neeko', 'ornn', 'pyke', 'qiyana', 'rakan', 'xayah', 'sett', 'senna', 'Sylas', 'tahm kench', 'Taliyah', 'yone', 'yuumi', 'zoe'])
    b = random.choice(['top', 'bottom', 'middle', 'support', 'jungle'])
    c = random.choice(['AD', 'Tank', 'AP', 'Crit', 'Attack speed', 'Assassin'])

    return a, c, b

def display():
    display1 = random_gen()
    display_result = tk.Text(master = root, height = 10, width = 30)
    display_result.grid(column = 3, row = 3)
    display_result.insert(tk.END, display1)

button = tk.Button(text = 'Randomize...', command = display)
button.grid(column = 0, row = 0)

root.mainloop()
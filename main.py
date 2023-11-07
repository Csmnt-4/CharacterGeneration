# This is a Python script to create a Pathfinder-style character sheet.
import random
import tkinter as tk
from tkinter import ttk
import namemaker


class Hero:
    def __init__(self, hero=False, race='', name='', surname='',
                 align='', cclass='', size=0, speed=0, wealt=0, batkb=0,
                 stren=0, dextr=0, const=0, intel=0, wisdm=0, charm=0):
        self.hero = hero
        self.race = race
        self.name = name
        self.surname = surname
        self.align = align
        self.cclass = cclass
        self.size = size
        self.speed = speed
        self.wealt = wealt
        self.batkb = batkb
        self.stren = stren
        self.dextr = dextr
        self.const = const
        self.intel = intel
        self.wisdm = wisdm
        self.charm = charm
        self.fort = (stren + const) / 2
        self.refl = (dextr + wisdm) / 2
        self.will = (intel + charm) / 2


def generate_stats(level):
    random.randint(1, 6)


def generate_random_name():
    new_hero.name = names.make_name()
    name_entry.delete(0, "end")  # Clear the existing text
    name_entry.insert(0, new_hero.name)
    new_hero.surname = surnames.make_name()
    surname_entry.delete(0, "end")  # Clear the existing text
    surname_entry.insert(0, new_hero.surname)


def choose_random_class():
    # Add logic to generate random values
    class_dropdown.set(random.choice(classes))
    new_hero.cclass = class_dropdown.get()
    new_hero.align = ''
    alignment_label_selected.config(text='')
    update_alignment_chart_availability()
    pass


def save_data():
    # Add logic to save data
    pass


def print_data():
    new_hero.stren = int(strength_box.get())
    new_hero.dextr = int(dexterity_box.get())
    new_hero.const = int(constitution_box.get())
    new_hero.intel = int(intelligence_box.get())
    new_hero.wisdm = int(wisdom_box.get())
    new_hero.charm = int(strength_box.get())

    print(new_hero.name + " " + new_hero.surname)
    print("class:" + new_hero.cclass)
    print("align:" + new_hero.align)

    print("\nstr:" + str(new_hero.stren))
    print("dex:" + str(new_hero.dextr))
    print("con:" + str(new_hero.const))
    print("int:" + str(new_hero.intel))
    print("wis:" + str(new_hero.wisdm))
    print("cha:" + str(new_hero.charm))

    print("fort:" + str((new_hero.stren + new_hero.const) / 2))
    print("refl:" + str((new_hero.dextr + new_hero.wisdm) / 2))
    print("will:" + str((new_hero.intel + new_hero.charm) / 2))


def set_alignment(event):
    clicked_button = event.widget
    for i in range(9):
        if alignment_button_dict[i] == clicked_button:
            if alignment_button_states[i]:
                # print(f"Clicked button name: {alignment_button_dict[clicked_button]}")
                alignment_label_selected.config(text=alignment_button_dict[clicked_button])
                new_hero.align = alignment_button_dict[clicked_button]


def update_alignment_chart_availability():
    # Pathfinder 1e
    # "Lawful Good", "Neutral Good", "Chaotic Good",
    # "Lawful Neutral", "True Neutral", "Chaotic Neutral",
    # "Lawful Evil", "Neutral Evil", "Chaotic Evil"

    for k in range(3):
        for l in range(3):
            alignment_button_dict[k * 3 + l].config(state="normal")
            alignment_button_states[k * 3 + l] = True
    if new_hero.cclass == "Barbarian":
        alignment_button_dict[0].config(state="disabled")
        alignment_button_dict[3].config(state="disabled")
        alignment_button_dict[6].config(state="disabled")
        alignment_button_states[0] = False
        alignment_button_states[3] = False
        alignment_button_states[6] = False
    if new_hero.cclass == "Druid":
        alignment_button_dict[0].config(state="disabled")
        alignment_button_dict[3].config(state="disabled")
        alignment_button_dict[6].config(state="disabled")
        alignment_button_dict[2].config(state="disabled")
        alignment_button_dict[5].config(state="disabled")
        alignment_button_dict[8].config(state="disabled")
        alignment_button_states[0] = False
        alignment_button_states[3] = False
        alignment_button_states[6] = False
        alignment_button_states[2] = False
        alignment_button_states[5] = False
        alignment_button_states[8] = False
    if new_hero.cclass == "Monk":
        alignment_button_dict[1].config(state="disabled")
        alignment_button_dict[4].config(state="disabled")
        alignment_button_dict[7].config(state="disabled")
        alignment_button_dict[2].config(state="disabled")
        alignment_button_dict[5].config(state="disabled")
        alignment_button_dict[8].config(state="disabled")
        alignment_button_states[1] = False
        alignment_button_states[4] = False
        alignment_button_states[7] = False
        alignment_button_states[2] = False
        alignment_button_states[5] = False
        alignment_button_states[8] = False
    if new_hero.cclass == "Paladin":
        for m in range(8):
            alignment_button_dict[m + 1].config(state="disabled")
            alignment_button_states[m + 1] = False


def class_dropdown_choice(*args):
    new_hero.cclass = class_dropdown.get()
    alignment_label_selected.config(text='')
    update_alignment_chart_availability()
    # print(str(new_hero.cclass))


def update_dropdowns(*args):
    selected_values = [strength_box.get(),
                       dexterity_box.get(),
                       constitution_box.get(),
                       intelligence_box.get(),
                       wisdom_box.get(),
                       charisma_box.get()]

    for combo in stat_boxes:
        combo['values'] = [value for value in stat_values if value not in selected_values]


def roll_dice():
    m = 3 if hero_type.get() == "Regular" else 4
    n = 3
    stat_values.clear()
    new_hero.wealt = random.randint(100, 200)
    wealth_label.config(text="Wealth: " + str(new_hero.wealt))

    for _ in range(6):
        rolls = [random.randint(1, 6) for _ in range(m)]
        largest_n_rolls = sorted(rolls, reverse=True)[:n]
        total = sum(largest_n_rolls)
        stat_values.append(str(total))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Character Creator")

    alignment_button_dict = {}
    alignment_button_states = {}
    new_hero = Hero()

    hero_type = tk.StringVar()
    hero_type.set("Regular")

    male_names = namemaker.make_name_set('male first names.txt', order=2)
    female_names = namemaker.make_name_set('female first names.txt', order=2)
    names = male_names + female_names
    surnames = namemaker.make_name_set('last names.txt', order=2)

    strength_box = tk.StringVar()
    dexterity_box = tk.StringVar()
    constitution_box = tk.StringVar()
    intelligence_box = tk.StringVar()
    wisdom_box = tk.StringVar()
    charisma_box = tk.StringVar()

    stat_values = []
    stat_boxes = []

    # 1st Line
    name_label = tk.Label(root, text="Name:")
    name_entry = tk.Entry(root)
    surname_label = tk.Label(root, text="Surname:")
    surname_entry = tk.Entry(root)
    random_name_button = tk.Button(root, text="Random", command=generate_random_name, padx=10)

    # 3rd Line
    # Create a 3x3 table with buttons in each cell
    alignment_table = tk.Frame(root)
    alignment = ["Lawful Good", "Neutral Good", "Chaotic Good",
                 "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                 "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
    for i in range(3):
        for j in range(3):
            alignment_button = tk.Button(alignment_table, text=alignment[i * 3 + j])
            alignment_button.grid(row=i, column=j)
            alignment_button_states[i * 3 + j] = True  # Map the button state to an index, then...
            alignment_button_dict[i * 3 + j] = alignment_button  # Map the button to an index and then...
            alignment_button_dict[alignment_button] = alignment[i * 3 + j]  # ...map the name to button in the
            root.bind("<Button-1>", set_alignment)  # dictionary... why so difficult???????

    alignment_label = tk.Label(root, text="Alignment:")
    alignment_label_selected = tk.Label(root, text="")

    # 2nd Line
    class_label = tk.Label(root, text="Class:")
    classes = ["Barbarian", "Bard", "Cleric",
               "Druid", "Fighter", "Monk",
               "Paladin", "Ranger", "Rogue",
               "Sorcerer", "Wizard"]
    class_dropdown = ttk.Combobox(root, values=classes)
    class_dropdown.bind("<<ComboboxSelected>>", class_dropdown_choice)
    random_class_button = tk.Button(root, text="Random", command=choose_random_class, padx=10)

    # 4th Line
    regular_radio = ttk.Radiobutton(root, text="Regular", variable=hero_type, value="Regular")
    heroic_radio = ttk.Radiobutton(root, text="Heroic", variable=hero_type, value="Heroic")
    roll_button = ttk.Button(root, text="Roll", command=roll_dice)

    # 5th-10th Lines
    attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    attribute_labels = [tk.Label(root, text=attr) for attr in attributes]
    for i, combo_var in enumerate(
            [strength_box, dexterity_box, constitution_box, intelligence_box, wisdom_box, charisma_box]):
        combo = ttk.Combobox(root, textvariable=combo_var, values=stat_values)
        combo.grid(row=i, column=0)
        stat_boxes.append(combo)
        combo_var.trace("w", update_dropdowns)  # Call update_dropdowns when combo_var changes

    size_label = tk.Label(root, text="Size:")
    speed_label = tk.Label(root, text="Speed:")
    wealth_label = tk.Label(root, text="Wealth:")

    fortitude_label = tk.Label(root, text="Fortitude:")
    reflex_label = tk.Label(root, text="Reflex:")
    will_label = tk.Label(root, text="Will:")

    # 10th Line
    save_button = tk.Button(root, text="Save", command=save_data)
    print_button = tk.Button(root, text="Print", command=print_data)

    # Packing widgets
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1, sticky='w')
    surname_label.grid(row=0, column=2)
    surname_entry.grid(row=0, column=3, sticky='w')
    random_name_button.grid(row=0, column=4, sticky='w', padx=10)

    class_label.grid(row=1, column=0)
    class_dropdown.grid(row=1, column=1, sticky='w')
    random_class_button.grid(row=1, column=2, sticky='w', padx=10)
    alignment_label.grid(row=1, column=3, sticky='w')
    alignment_label_selected.grid(row=1, column=4, sticky='w')

    alignment_table.grid(row=2, column=0, columnspan=5, pady=10)

    regular_radio.grid(row=4, column=0)
    heroic_radio.grid(row=4, column=1)
    roll_button.grid(row=4, column=2, columnspan=2)

    for i, (label, dropdown) in enumerate(zip(attribute_labels, stat_boxes), start=5):
        label.grid(row=i, column=0, sticky='w', padx=10)
        dropdown.grid(row=i, column=1)

    size_label.grid(row=5, column=2, sticky='w', padx=10)
    speed_label.grid(row=6, column=2, sticky='w', padx=10)
    wealth_label.grid(row=7, column=2, sticky='w', padx=10)
    fortitude_label.grid(row=8, column=2, sticky='w', padx=10)
    reflex_label.grid(row=9, column=2, sticky='w', padx=10)
    will_label.grid(row=10, column=2, sticky='w', padx=10)

    print_button.grid(row=11, column=1, padx=0, pady=10)
    save_button.grid(row=11, column=2, padx=0, pady=10)

    root.mainloop()

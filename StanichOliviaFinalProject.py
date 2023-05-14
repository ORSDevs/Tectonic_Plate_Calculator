import tkinter as tk
import random

facts = [
    'Hawaii was formed by the Pacific Plate.',
    "The Ring of Fire is created in the Pacific Ocean, it's made up of large volcanoes and mountain regions "
    "beneath the sea.",
    "Tectonic plates grinding and slipping against each other are the cause of earthquakes and tsunamis",
    "The largest tectonic plate is the Pacific Plate.",
    "Tectonic plates are able to move because the Earth's lithosphere has greater strength than the "
    "underlying asthenosphere.",
    "Plate motions range up to a typical 10–40 mm/year (Mid-Atlantic Ridge; about as fast as fingernails "
    "grow) to about 160 mm/year (Nazca Plate; about as fast as hair grows.",
    "The majority of the world's active volcanoes occur along plate boundaries, with the Pacific Plate's Ring "
    "of Fire being the most active and widely known today.",
    "The rock formations of eastern North America, Western Europe, and northwestern Africa were later found "
    "to have a common origin, and they overlapped in time with the presence of Gondwanaland. Together, "
    "these discoveries supported the existence of Pangea.",
    "A transform boundary happens when plates slide past each other but neither collide nor rip apart. The "
    "San Andreas Fault in California is a transform boundary."
]


class YearInputWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Year Input")

        birth_year_label = tk.Label(self.window, text="Please enter your birth year:")
        birth_year_label.pack()
        self.birth_year_entry = tk.Entry(self.window)
        self.birth_year_entry.pack()

        current_year_label = tk.Label(self.window, text="Please enter the current year:")
        current_year_label.pack()
        self.current_year_entry = tk.Entry(self.window)
        self.current_year_entry.pack()

        submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        submit_button.pack()

        fun_fact_button = tk.Button(self.window, text="Fun Fact!", command=self.show_fun_fact)
        fun_fact_button.pack()

        self.window.mainloop()

    def submit(self):
        birth_year = int(self.birth_year_entry.get())
        current_year = int(self.current_year_entry.get())
        self.window.destroy()
        PlateInputWindow(birth_year, current_year)

    def show_fun_fact(self):
        fact = random.choice(facts)
        tk.Label(self.window, text=fact)

        window = tk.Tk()
        window.title("Fun Facts")
        window.geometry("300x100")

        label = tk.Label(window, text="Fun fact!", wraplength=250)
        label.pack()

        fact = random.choice(facts)
        label.config(text=fact)

        self.window.mainloop()


class PlateInputWindow:
    def __init__(self, birth_year, current_year):
        self.window = tk.Tk()
        self.window.title("Plate Input")

        self.plate_options = {
            # The North American Plate
            "North American Plate": 1, "The North American Plate": 1, "north american plate": 1,
            "the north american plate": 1, "north american": 1, "North American": 1,
            # The African Plate
            "African Plate": 0.85, "The African Plate": 0.85, "african plate": 0.85, "african": 0.85, "African": 0.85,
            # The Antarctic Tectonic Plate
            "Antarctic Tectonic Plate": 0.4, "antarctic tectonic plate": 0.4, "The Antarctic Tectonic Plate": 0.4,
            "the antarctic tectonic plate": 0.4,
            # The Eurasian Tectonic Plate
            "Eurasian Tectonic Plate": 3.25, "eurasian tectonic plate": 3.25, "The Eurasian Tectonic Plate": 3.25,
            "Eurasian tectonic plate": 3.25,
            # The Indo-Australian Plate
            "Indo-Australian Plate": 2.2, "The Indo-Australian Plate": 2.2, "indo-australian plate": 2.2,
            "the indo-australian plate": 2.2,
            # The Pacific Plate
            "Pacific Plate": 2, "The Pacific Plate": 2, "the pacific plate": 2, "pacific plate": 2,
            # The South American Plate
            "South American Plate": 1.3, "south american plate": 1.3, "The South American Plate": 1.3,
            "the south american plate": 1.3,
            # The Scotia Plate
            "Scotia Plate": 0.87, "The Scotia Plate": 0.87, "scotia plate": 0.87, "the scotia plate": 0.87,
            # The Nazca Plate
            "Nazca Plate": 3.11024, "The Nazca Plate": 3.11024, "the nazca plate": 3.11024, "nazca plate": 3.11024,
            # The Cocos Plate
            "Cocos Plate": 3.07087, "The Cocos Plate": 3.07087, "cocos plate": 3.07087, "the cocos plate": 3.07087,
            # The Caribbean Plate
            "Caribbean Plate": 0.87, "The Caribbean Plate": 0.87, "the caribbean plate": 0.87, "caribbean plate": 0.87,
            # The Juan de Fuca Plate
            "Juan de Fuca Plate": 1.6, "The Juan de Fuca Plate": 1.6, "the juan de fuca plate": 1.6,
            "juan de fuca plate": 1.6,
            # The Amurian Plate
            "Amurian Plate": 0.393701, "The Amurian Plate": 0.393701, "amurian plate": 0.393701,
            "the amurian plate": 0.393701,
            # The Arabian Plate
            "Arabian Plate": 0.590551, "The Arabian Plate": 0.590551, "the arabian plate": 0.590551,
            "arabian plate": 0.590551,
            # The Burma Plate
            "Burma Plate": 1.81102, "The Burma Plate": 1.81102, "burma plate": 1.81102, "the burma plate": 1.81102,
            # The Caroline Plate
            "Caroline Plate": 3.4252, "The Caroline Plate": 3.4252, "caroline plate": 3.4252,
            "the caroline plate": 3.4252,
            # The Okhotsk Plate
            "The Okhotsk Plate": 0.551181, "Okhotsk Plate": 0.551181, "the okhotsk plate": 0.551181,
            "okhotsk plate": 0.551181,
            # The Philippine Sea Plate
            "Philippine Sea Plate": 1.88976, "The Philippine Sea Plate": 1.88976, "philippine sea plate": 1.88976,
            "the philippine sea plate": 1.88976,
            # The Somali Plate
            "Somali Plate": 0.23622, "The Somali Plate": 0.23622, "somali plate": 0.23622, "the somali plate": 0.23622,
            # the Sunda Plate
            "Sunda Plate": 0.551181, "The Sunda Plate": 0.551181, "sunda plate": 0.551181,
            "the sunda plate": 0.551181,
            # The Yangtze Plate
            "Yangtze Plate": 0.590551, "The Yangtze Plate": 0.590551, "yangtze plate": 0.590551,
            "the yangtze plate": 0.590551,
        }

        plate_label = tk.Label(self.window, text="Please enter the tectonic plate you want to know about:")
        plate_label.pack()
        self.plate_entry = tk.Entry(self.window)
        self.plate_entry.pack()

        submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        submit_button.pack()

        self.birth_year = birth_year
        self.current_year = current_year
        self.window.mainloop()

    class PlateNameWindow:
        def __init__(self):
            self.window = tk.Tk()
            self.window.title(" of plates")

    def submit(self):
        plate = self.plate_entry.get()
        try:
            plate_speed = self.plate_options[plate]
        except KeyError:
            error_label = tk.Label(self.window, text="Invalid plate entered.")
            error_label.pack()
            return
        years_passed = self.current_year - self.birth_year
        distance_moved = years_passed * plate_speed
        distance_label = tk.Label(self.window, text=f"The {plate} has moved {distance_moved:.2f} inches.")
        distance_label.pack()


root = YearInputWindow()

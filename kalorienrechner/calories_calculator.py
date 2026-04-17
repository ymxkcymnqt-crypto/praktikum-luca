"""
Calories Calculator - A simple meal tracking application.

This application allows you to:
- Add meals with their calorie count
- View the total calories for the day
- See a summary of all meals
- Reset the tracker for a new day

The application uses a Tkinter GUI (graphical user interface).

YOUR TASK: Implement the methods in the MealTracker class.
           Look for the "# TODO" comments below.
           The Tkinter UI is already complete - you only need to write the logic!
"""

# We import tkinter, Python's built-in library for creating graphical interfaces.
# "tk" is a short alias so we don't have to type "tkinter" every time.
import tkinter as tk

# messagebox is a sub-module of tkinter that lets us show pop-up dialogs
# (e.g. error messages, info messages).
from tkinter import messagebox


# =============================================================================
# MEAL TRACKER CLASS
# =============================================================================
# This class holds the DATA and LOGIC of our application.
# It does NOT know anything about the GUI - it only manages meals.
#
# A "class" is like a blueprint. We can create objects from it.
# Each object has its own data (attributes) and functions (methods).
# =============================================================================

class MealTracker:
    """
    Tracks meals and their calorie counts for a single day.

    Attributes:
        meals (list): A list of dictionaries. Each dictionary represents
                      one meal and has two keys:
                      - "name" (str): The name of the meal, e.g. "Breakfast"
                      - "calories" (int): The calorie count, e.g. 450

    Example of what self.meals should look like after adding two meals:
        [
            {"name": "Breakfast", "calories": 450},
            {"name": "Lunch", "calories": 700}
        ]
    """

    def __init__(self):
        """
        The __init__ method is called automatically when we create a new
        MealTracker object. It sets up the initial state.

        self.meals is an empty list that will store our meal dictionaries.

        A list in Python is an ordered collection of items:
            my_list = []          # empty list
            my_list.append(42)    # adds 42 to the list -> [42]
            my_list.append(99)    # adds 99 to the list -> [42, 99]

        A dictionary (dict) stores key-value pairs:
            my_dict = {"name": "Apple", "calories": 95}
            print(my_dict["name"])      # prints "Apple"
            print(my_dict["calories"])  # prints 95
        """
        self.meals = []

    def add_meal(self, name, calories):
        meal = {"name": name, "calories": calories}
        self.meals.append(meal)
        """
        Add a meal to the tracker.

        This method should create a dictionary with the keys "name" and
        "calories", and append it to self.meals.

        Args:
            name (str): The name of the meal (e.g. "Breakfast").
            calories (int): The number of calories (e.g. 450).

        Hint:
            - Create a dict:  meal = {"name": name, "calories": calories}
            - Append to list: self.meals.append(meal)

        Example:
            tracker = MealTracker()
            tracker.add_meal("Breakfast", 450)
            # Now self.meals == [{"name": "Breakfast", "calories": 450}]
        """
        # TODO: Implement this method (2 lines of code)
        pass  # Remove this line when you start implementing


    def get_total_calories(self):
        total = 0         
        for meal in self.meals:          
            total += meal["calories"]          
            return total
        """
        Calculate and return the total calories of all meals.

        This method should loop through self.meals, add up all the
        "calories" values, and return the total as an integer.

        Returns:
            int: The sum of all calories. Returns 0 if no meals exist.

        Hint - using a for-loop:
            total = 0
            for meal in self.meals:
                total = total + meal["calories"]
            return total

        Hint - shorter alternative using sum() and a generator:
            return sum(meal["calories"] for meal in self.meals)

        Example:
            tracker = MealTracker()
            tracker.add_meal("Breakfast", 450)
            tracker.add_meal("Lunch", 700)
            tracker.get_total_calories()  # returns 1150
        """
        # TODO: Implement this method (3-4 lines of code, or 1 line with sum())
        pass  # Remove this line when you start implementing


    def get_meals_summary(self):
        summary = []
        for meal in self.meals:
         summary.append(f"{meal['name']} - {meal['calories']} kcal")
         return summary
        """
        Return a list of formatted strings, one per meal.

        Each string should have the format: "MealName - 450 kcal"

        Returns:
            list: A list of strings. Empty list if no meals exist.

        Hint - f-strings:
            An f-string lets you embed variables directly in a string:
                name = "Breakfast"
                cals = 450
                text = f"{name} - {cals} kcal"  # "Breakfast - 450 kcal"

        Hint - building the list:
            summary = []
            for meal in self.meals:
                line = f"{meal['name']} - {meal['calories']} kcal"
                summary.append(line)
            return summary

        Example:
            tracker = MealTracker()
            tracker.add_meal("Breakfast", 450)
            tracker.add_meal("Lunch", 700)
            tracker.get_meals_summary()
            # returns ["Breakfast - 450 kcal", "Lunch - 700 kcal"]
        """
        # TODO: Implement this method (4-5 lines of code)
        pass  # Remove this line when you start implementing


    def reset_day(self):
        self.meals.clear()
        """
        Remove all meals from the tracker (start a new day).

        This method should clear the self.meals list so it becomes empty.

        Hint:
            You can clear a list in multiple ways:
                self.meals = []       # replace with a new empty list
                self.meals.clear()    # remove all items from existing list

        Example:
            tracker = MealTracker()
            tracker.add_meal("Breakfast", 450)
            tracker.reset_day()
            # Now self.meals == []
        """
        # TODO: Implement this method (1 line of code)
        pass  # Remove this line when you start implementing


# =============================================================================
# TKINTER GUI CLASS
# =============================================================================
# This class creates the graphical user interface (GUI).
# It uses the MealTracker class above to store and retrieve data.
#
# YOU DO NOT NEED TO CHANGE THIS CLASS for the basic tasks.
# Read the comments to understand how it works.
# The bonus tasks at the end will ask you to modify it.
# =============================================================================

class CaloriesApp:
    """
    A graphical user interface for the Calories Calculator.

    This class uses tkinter to create a window with:
    - Input fields for meal name and calories
    - An "Add Meal" button
    - A listbox showing all added meals
    - A label showing the total calories
    - A "Reset Day" button
    """

    def __init__(self):
        """
        Set up the main window and all widgets (UI elements).

        Tkinter works like this:
        1. Create a main window with tk.Tk()
        2. Add widgets (Label, Entry, Button, Listbox, ...) to the window
        3. Arrange them with a layout manager (we use .grid())
        4. Start the main loop that keeps the window open
        """

        # --- Create the MealTracker that holds our data ---
        # This is the "backend" - it stores meals and does calculations.
        self.tracker = MealTracker()

        # --- Create the main window ---
        # tk.Tk() creates the root window of our application.
        self.root = tk.Tk()

        # Set the title that appears in the window's title bar.
        self.root.title("Calories Calculator")

        # Set a minimum size for the window (width x height in pixels).
        self.root.minsize(450, 400)

        # Add some padding (space) around the entire window content.
        # padx = horizontal padding, pady = vertical padding (in pixels).
        self.root.configure(padx=15, pady=15)

        # --- Input Section ---
        # We use the .grid() layout manager to place widgets in a table-like
        # structure with rows and columns.

        # tk.Label creates a text label. It just displays text, no interaction.
        # grid(row=0, column=0) places it in the first row, first column.
        # sticky="w" means the label sticks to the West (left) side of its cell.
        tk.Label(self.root, text="Meal name:").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )

        # tk.Entry creates a text input field where the user can type.
        # We save it as self.entry_name so we can read its value later.
        self.entry_name = tk.Entry(self.root, width=30)
        self.entry_name.grid(row=0, column=1, pady=(0, 5), padx=(10, 0))

        # Another label + entry for the calorie count.
        tk.Label(self.root, text="Calories:").grid(
            row=1, column=0, sticky="w", pady=(0, 10)
        )

        self.entry_calories = tk.Entry(self.root, width=30)
        self.entry_calories.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))

        # --- Add Button ---
        # tk.Button creates a clickable button.
        # command=self._on_add_meal tells tkinter: "When this button is clicked,
        # call the method self._on_add_meal()".
        tk.Button(
            self.root,
            text="Add Meal",
            command=self._on_add_meal,
            width=20,
        ).grid(row=2, column=0, columnspan=2, pady=(0, 15))
        # columnspan=2 makes the button span across both columns.

        # --- Meals List ---
        # tk.Listbox creates a scrollable list widget.
        # It displays the meals we've added.
        tk.Label(self.root, text="Today's Meals:").grid(
            row=3, column=0, columnspan=2, sticky="w"
        )

        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.grid(row=4, column=0, columnspan=2, pady=(5, 10))

        # --- Total Calories Label ---
        # tk.StringVar is a special tkinter variable. When its value changes,
        # any widget connected to it updates automatically.
        self.total_var = tk.StringVar()
        self.total_var.set("Total: 0 kcal")

        # textvariable=self.total_var connects this label to our StringVar.
        # When we call self.total_var.set("new text"), the label updates.
        tk.Label(
            self.root,
            textvariable=self.total_var,
            font=("Arial", 14, "bold"),
        ).grid(row=5, column=0, columnspan=2, pady=(0, 10))

        # --- Reset Button ---
        tk.Button(
            self.root,
            text="Reset Day",
            command=self._on_reset,
            width=20,
        ).grid(row=6, column=0, columnspan=2)

    def _on_add_meal(self):
        """
        Called when the user clicks "Add Meal".

        Reads the input fields, validates them, adds the meal to the
        tracker, and updates the display.
        """
        # .get() reads the current text from an Entry widget.
        name = self.entry_name.get().strip()
        calories_text = self.entry_calories.get().strip()

        # Basic validation: check that both fields are filled in.
        if not name or not calories_text:
            messagebox.showerror("Error", "Please enter both a meal name and calories.")
            return

        # Try to convert the calories text to an integer.
        # If the user typed something like "abc", this will fail.
        try:
            calories = int(calories_text)
        except ValueError:
            messagebox.showerror("Error", "Calories must be a whole number.")
            return

        # Check that calories are not negative.
        if calories < 0:
            messagebox.showerror("Error", "Calories cannot be negative.")
            return

        # Add the meal using our MealTracker.
        self.tracker.add_meal(name, calories)

        # Update the listbox and total display.
        self._refresh_display()

        # Clear the input fields so the user can type the next meal.
        self.entry_name.delete(0, tk.END)
        self.entry_calories.delete(0, tk.END)

        # Set focus back to the name field for convenience.
        self.entry_name.focus()

    def _on_reset(self):
        """
        Called when the user clicks "Reset Day".

        Asks for confirmation, then clears all meals.
        """
        # askyesno shows a dialog with "Yes" and "No" buttons.
        # It returns True if the user clicks "Yes".
        if messagebox.askyesno("Confirm", "Reset all meals for today?"):
            self.tracker.reset_day()
            self._refresh_display()

    def _refresh_display(self):
        """
        Update the listbox and total calories label to reflect
        the current state of the tracker.
        """
        # Clear the listbox: delete all items from index 0 to the end.
        self.listbox.delete(0, tk.END)

        # Get the summary lines from the tracker and add each to the listbox.
        summary = self.tracker.get_meals_summary()
        if summary is not None:
            for line in summary:
                # insert(tk.END, ...) adds an item at the bottom of the list.
                self.listbox.insert(tk.END, line)

        # Update the total calories label.
        total = self.tracker.get_total_calories()
        if total is not None:
            self.total_var.set(f"Total: {total} kcal")
        else:
            self.total_var.set("Total: 0 kcal")

    def run(self):
        """
        Start the application.

        mainloop() is a tkinter method that keeps the window open and
        responsive. It listens for events (clicks, key presses, etc.)
        and calls the appropriate handler methods.
        The program stays in this loop until the window is closed.
        """
        self.root.mainloop()


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================
# The code below runs only when you execute this file directly:
#     python calories_calculator.py
#
# It does NOT run when the file is imported (e.g. in the test file).
# This is a common Python pattern.
# =============================================================================

if __name__ == "__main__":
    app = CaloriesApp()
    app.run()

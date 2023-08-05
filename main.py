import tkinter as tk
from tkinter import messagebox


def display_swot_analysis():
    """
    Display the SWOT analysis using the provided inputs.
    """
    scenario = scenario_entry.get("1.0", tk.END).strip()
    strengths = strengths_entry.get("1.0", tk.END).strip().split("\n")
    weaknesses = weaknesses_entry.get("1.0", tk.END).strip().split("\n")
    opportunities = opportunities_entry.get("1.0", tk.END).strip().split("\n")
    threats = threats_entry.get("1.0", tk.END).strip().split("\n")

    if not scenario:
        messagebox.showerror("Error", "Please enter a scenario.")
        return

    # Display the SWOT analysis in a message box
    message = f"--- SWOT Analysis ---\n\n"
    message += f"Scenario:\n{scenario}\n\n"
    message += f"Strengths:\n"
    for i, strength in enumerate(strengths):
        message += f"{i + 1}. {strength}\n"
    message += f"\nWeaknesses:\n"
    for i, weakness in enumerate(weaknesses):
        message += f"{i + 1}. {weakness}\n"
    message += f"\nOpportunities:\n"
    for i, opportunity in enumerate(opportunities):
        message += f"{i + 1}. {opportunity}\n"
    message += f"\nThreats:\n"
    for i, threat in enumerate(threats):
        message += f"{i + 1}. {threat}\n"

    # Save the SWOT analysis to a text file
    with open("swot_analysis.txt", "w") as file:
        file.write(message)

    messagebox.showinfo("SWOT Analysis", message)


# Create the main window
window = tk.Tk()
window.title("SWOT Analysis")

# Configure window styling options
window.configure(bg="#F5F5F5")
window.geometry("500x620")
window.resizable(False, False)

# Create the scenario label and text entry
scenario_label = tk.Label(window, text="Scenario:", font=("Arial", 12, "bold"), bg="#F5F5F5")
scenario_label.pack(pady=(20, 5))
scenario_entry = tk.Text(window, height=3, width=50, font=("Arial", 11))
scenario_entry.pack()

# Create the strengths label and text entry
strengths_label = tk.Label(window, text="Strengths:", font=("Arial", 12, "bold"), bg="#F5F5F5")
strengths_label.pack(pady=(10, 5))
strengths_entry = tk.Text(window, height=6, width=50, font=("Arial", 11))
strengths_entry.pack()

# Create the weaknesses label and text entry
weaknesses_label = tk.Label(window, text="Weaknesses:", font=("Arial", 12, "bold"), bg="#F5F5F5")
weaknesses_label.pack(pady=(10, 5))
weaknesses_entry = tk.Text(window, height=6, width=50, font=("Arial", 11))
weaknesses_entry.pack()

# Create the opportunities label and text entry
opportunities_label = tk.Label(window, text="Opportunities:", font=("Arial", 12, "bold"), bg="#F5F5F5")
opportunities_label.pack(pady=(10, 5))
opportunities_entry = tk.Text(window, height=6, width=50, font=("Arial", 11))
opportunities_entry.pack()

# Create the threats label and text entry
threats_label = tk.Label(window, text="Threats:", font=("Arial", 12, "bold"), bg="#F5F5F5")
threats_label.pack(pady=(10, 5))
threats_entry = tk.Text(window, height=6, width=50, font=("Arial", 11))
threats_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 12, "bold"), command=display_swot_analysis, bg="#4CAF50", fg="gold")
submit_button.pack(pady=(20, 0))

# Run the main window's event loop
window.mainloop()

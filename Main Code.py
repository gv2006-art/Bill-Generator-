import tkinter as tk
from tkinter import ttk, messagebox

class ElectricityBillTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Bill Generator & Power Tracker")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f0f0')
        self.appliances = []
        self.rate_per_kwh = 7.0
        
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(main_frame, text="⚡ Electricity Bill Generator", 
                               font=('Lucida Bright', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(0, 20))

        self.create_input_section(main_frame)
        self.create_appliances_section(main_frame)
        self.create_summary_section(main_frame)
        self.create_control_buttons(main_frame)

    def create_input_section(self, parent):
        input_frame = tk.LabelFrame(parent, text="Add New Appliance", font=('Lucida Bright', 12, 'bold'), 
                                    bg='#f0f0f0', fg='#34495e', padx=15, pady=15)
        input_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(input_frame, text="Appliance Name:", bg='#f0f0f0').grid(row=0, column=0, sticky='w', pady=5)
        self.name_entry = tk.Entry(input_frame, width=20, font=('Lucida Bright', 10))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Power Rating (Watts):", bg='#f0f0f0').grid(row=0, column=2, sticky='w', pady=5)
        self.power_entry = tk.Entry(input_frame, width=15, font=('Lucida Bright', 10))
        self.power_entry.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(input_frame, text="Daily Usage (Hours):", bg='#f0f0f0').grid(row=1, column=0, sticky='w', pady=5)
        self.hours_entry = tk.Entry(input_frame, width=15, font=('Lucida Bright', 10))
        self.hours_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Number of Days:", bg='#f0f0f0').grid(row=1, column=2, sticky='w', pady=5)
        self.days_entry = tk.Entry(input_frame, width=15, font=('Lucida Bright', 10))
        self.days_entry.grid(row=1, column=3, padx=10, pady=5)

        add_btn = tk.Button(input_frame, text="Add Appliance", command=self.add_appliance,
                            bg='#3498db', fg='white', font=('Lucida Bright', 10, 'bold'),
                            padx=20, pady=5, cursor='hand2')
        add_btn.grid(row=2, column=1, columnspan=2, pady=15)

        rate_frame = tk.Frame(input_frame, bg='#f0f0f0')
        rate_frame.grid(row=3, column=0, columnspan=4, pady=10)

        tk.Label(rate_frame, text="Rate per kWh (₹):", bg='#f0f0f0').pack(side=tk.LEFT)
        self.rate_entry = tk.Entry(rate_frame, width=10, font=('Lucida Bright', 10))
        self.rate_entry.pack(side=tk.LEFT, padx=10)
        self.rate_entry.insert(0, str(self.rate_per_kwh))

        rate_btn = tk.Button(rate_frame, text="Update Rate", command=self.update_rate,
                             bg='#e67e22', fg='white', font=('Lucida Bright', 9),
                             padx=10, pady=2, cursor='hand2')
        rate_btn.pack(side=tk.LEFT, padx=10)

    def create_appliances_section(self, parent):
        list_frame = tk.LabelFrame(parent, text="Added Appliances", font=('Lucida Bright', 12, 'bold'),
                                   bg='#f0f0f0', fg='#34495e', padx=15, pady=15)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        columns = ('Name', 'Power (W)', 'Hours/Day', 'Days', 'Energy (kWh)', 'Cost (₹)')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=8)
        column_widths = [120, 80, 80, 60, 100, 100]
        for i, col in enumerate(columns):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[i], anchor='center')

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        delete_btn = tk.Button(list_frame, text="Delete Selected", command=self.delete_appliance,
                               bg='#e74c3c', fg='white', font=('Lucida Bright', 10, 'bold'),
                               padx=15, pady=5, cursor='hand2')
        delete_btn.pack(pady=10)

    def create_summary_section(self, parent):
        summary_frame = tk.LabelFrame(parent, text="Bill Summary", font=('Lucida Bright', 12, 'bold'),
                                      bg='#f0f0f0', fg='#34495e', padx=15, pady=15)
        summary_frame.pack(fill=tk.X, pady=(0, 20))

        self.total_energy_label = tk.Label(summary_frame, text="Total Energy Consumption: 0.00 kWh",
                                           font=('Lucida Bright', 11, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        self.total_energy_label.pack(pady=5)

        self.total_cost_label = tk.Label(summary_frame, text="Total Electricity Bill: ₹0.00",
                                         font=('Lucida Bright', 14, 'bold'), bg='#f0f0f0', fg='#27ae60')
        self.total_cost_label.pack(pady=5)



    def create_control_buttons(self, parent):
        button_frame = tk.Frame(parent, bg='#f0f0f0')
        button_frame.pack(fill=tk.X)

        calc_btn = tk.Button(button_frame, text="Calculate Bill", command=self.calculate_bill,
                             bg='#27ae60', fg='white', font=('Lucida Bright', 12, 'bold'),
                             padx=30, pady=10, cursor='hand2')
        calc_btn.pack(side=tk.LEFT, padx=10)

        clear_btn = tk.Button(button_frame, text="Clear All", command=self.clear_all,
                              bg='#95a5a6', fg='white', font=('Lucida Bright', 12, 'bold'),
                              padx=30, pady=10, cursor='hand2')
        clear_btn.pack(side=tk.LEFT, padx=10)

    def add_appliance(self):
        try:
            name = self.name_entry.get().strip()
            power = float(self.power_entry.get())
            hours = float(self.hours_entry.get())
            days = int(self.days_entry.get())

            if not name:
                messagebox.showerror("Error", "Please enter appliance name!")
                return
            if power <= 0 or hours <= 0 or days <= 0 or hours > 24:
                messagebox.showerror("Error", "Please enter valid values!")
                return

            energy_kwh = (power * hours * days) / 1000
            cost = energy_kwh * self.rate_per_kwh

            appliance = {
                'name': name,
                'power': power,
                'hours': hours,
                'days': days,
                'energy_kwh': energy_kwh,
                'cost': cost
            }

            self.appliances.append(appliance)
            self.tree.insert('', tk.END, values=(name, f"{power:.0f}", f"{hours:.1f}", days,
                                                 f"{energy_kwh:.2f}", f"{cost:.2f}"))

            self.clear_inputs()
            self.update_summary()
            messagebox.showinfo("Success", f"Added {name} successfully!")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values!")

    def delete_appliance(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an appliance to delete!")
            return
        item = selected[0]
        index = self.tree.index(item)
        self.appliances.pop(index)
        self.tree.delete(item)
        self.update_summary()
        messagebox.showinfo("Success", "Appliance deleted successfully!")

    def update_rate(self):
        try:
            new_rate = float(self.rate_entry.get())
            if new_rate <= 0:
                messagebox.showerror("Error", "Rate must be positive!")
                return
            self.rate_per_kwh = new_rate
            # Recalculate costs for all existing appliances
            for i, app in enumerate(self.appliances):
                app['cost'] = app['energy_kwh'] * self.rate_per_kwh
                item = self.tree.get_children()[i]
                values = list(self.tree.item(item)['values'])
                values[5] = f"{app['cost']:.2f}"
                self.tree.item(item, values=values)
            self.update_summary()
            messagebox.showinfo("Success", f"Rate updated to ₹{new_rate:.2f}/kWh")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid rate!")

    def calculate_bill(self):
        if not self.appliances:
            messagebox.showwarning("Warning", "Please add appliances first!")
            return

        total_energy = sum(app['energy_kwh'] for app in self.appliances)
        total_cost = sum(app['cost'] for app in self.appliances)

        details = "Electricity Bill Calculation\n" + "="*40 + "\n\n"
        for app in self.appliances:
            details += f"{app['name']}:\n"
            details += f"  Power: {app['power']:.0f}W\n"
            details += f"  Usage: {app['hours']:.1f} hours/day × {app['days']} days\n"
            details += f"  Energy: {app['energy_kwh']:.2f} kWh\n"
            details += f"  Cost: ₹{app['cost']:.2f}\n\n"
        details += f"Total Energy Consumption: {total_energy:.2f} kWh\n"
        details += f"Rate: ₹{self.rate_per_kwh:.2f}/kWh\n"
        details += f"Total Bill Amount: ₹{total_cost:.2f}"
        self.show_calculation_window(details)

    def show_calculation_window(self, details):
        calc_window = tk.Toplevel(self.root)
        calc_window.title("Bill Calculation Details")
        calc_window.geometry("400x500")
        calc_window.configure(bg='#f0f0f0')

        text_frame = tk.Frame(calc_window, bg='#f0f0f0')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=('Courier', 10),
                              bg='white', fg='#2c3e50')
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget.insert(tk.END, details)
        text_widget.config(state=tk.DISABLED)

        close_btn = tk.Button(calc_window, text="Close", command=calc_window.destroy,
                              bg='#34495e', fg='white', font=('Lucida Bright', 11, 'bold'),
                              padx=20, pady=5)
        close_btn.pack(pady=10)

    def update_summary(self):
        if not self.appliances:
            self.total_energy_label.config(text="Total Energy Consumption: 0.00 kWh")
            self.total_cost_label.config(text="Total Electricity Bill: ₹0.00")
            return

        total_energy = sum(app['energy_kwh'] for app in self.appliances)
        total_cost = sum(app['cost'] for app in self.appliances)

        self.total_energy_label.config(text=f"Total Energy Consumption: {total_energy:.2f} kWh")
        self.total_cost_label.config(text=f"Total Electricity Bill: ₹{total_cost:.2f}")

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.power_entry.delete(0, tk.END)
        self.hours_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all appliances?"):
            self.appliances.clear()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.update_summary()
            messagebox.showinfo("Success", "All appliances cleared!")

def main():
    root = tk.Tk()
    app = ElectricityBillTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()

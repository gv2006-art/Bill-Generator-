# Bill-Generator-
MiniProject: Electricity Bill Generator 
Here’s a professional `README.md` file for your **Electricity Bill Generator & Power Tracker** project built using **Python**, **Tkinter**, **OOP**, and **user-defined functions**:

---

# ⚡ Electricity Bill Generator & Power Tracker

A user-friendly GUI application to **track power consumption of appliances** and **generate electricity bills** based on usage data. Built using Python's `tkinter` for the interface and follows Object-Oriented Programming (OOP) principles with modular, user-defined functions.

---

## 📌 Features

* Add appliances with power ratings, daily usage, and duration
* Automatically calculates:

  * Energy consumption (in kWh)
  * Cost per appliance
* Set custom electricity rate (₹/kWh)
* Display detailed bill summary and breakdown
* Update/delete appliances dynamically
* Clean, responsive UI using `tkinter`
* Built with **OOP concepts** and **user-defined methods** for clean structure

---

## 🛠 Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **Object-Oriented Programming** principles
* **User-defined functions**

---

## 🚀 How to Run

1. **Requirements**:

   * Python 3.x (Recommended 3.8 or later)
   * No external libraries needed

2. **Steps**:

   * Clone or download this repository
   * Run the script:

   ```bash
   python electricity_bill_tracker.py
   ```

3. **Usage**:

   * Enter appliance name, power rating (W), daily usage (hours), and days
   * Click **"Add Appliance"**
   * Set or update the electricity rate
   * Click **"Calculate Bill"** to get detailed usage & cost breakdown

---

## 🧠 Code Highlights

* `ElectricityBillTracker` class encapsulates all functionalities.
* Uses:

  * `add_appliance()` → Adds new appliance to the tracker
  * `calculate_bill()` → Computes total energy use and bill
  * `update_rate()` → Updates cost per unit
  * `clear_all()` → Resets all data
  * `delete_appliance()` → Removes selected item
* GUI divided into:

  * Input Section
  * Appliances List
  * Bill Summary
  * Action Buttons

---

## 📷 UI Preview

> A modern and clean GUI with collapsible sections, scrollable lists, and interactive buttons (Add, Delete, Calculate, Clear).

---

## 📄 License

This project is for educational purposes. Free to use and modify.

---


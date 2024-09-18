import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import requests

class CalendarWeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar and Weather Forecast")
        self.root.geometry("500x500")

        self.create_calendar()
        self.create_weather_section()
        self.events = {}

    def create_calendar(self):
        """Creates a calendar widget and event management section."""
        self.calendar = Calendar(self.root, selectmode="day", year=2024, month=9, day=1)
        self.calendar.pack(pady=20)

        event_label = tk.Label(self.root, text="Add Event:")
        event_label.pack()

        self.event_entry = tk.Entry(self.root, width=30)
        self.event_entry.pack()

        add_event_btn = tk.Button(self.root, text="Add Event", command=self.add_event)
        add_event_btn.pack(pady=5)

        view_event_btn = tk.Button(self.root, text="View Events", command=self.view_events)
        view_event_btn.pack(pady=5)

    def add_event(self):
        """Adds an event to the selected date."""
        selected_date = self.calendar.get_date()
        event = self.event_entry.get()

        if not event:
            messagebox.showwarning("Input Error", "Please enter an event description.")
            return

        if selected_date not in self.events:
            self.events[selected_date] = []

        self.events[selected_date].append(event)
        self.event_entry.delete(0, tk.END)
        messagebox.showinfo("Event Added", f"Event '{event}' added for {selected_date}.")

    def view_events(self):
        """Displays the events for the selected date."""
        selected_date = self.calendar.get_date()

        if selected_date in self.events:
            events = "\n".join(self.events[selected_date])
            messagebox.showinfo(f"Events on {selected_date}", events)
        else:
            messagebox.showinfo(f"No Events", f"No events for {selected_date}.")

    def create_weather_section(self):
        """Creates a section for displaying weather forecast."""
        city_label = tk.Label(self.root, text="Enter City:")
        city_label.pack()

        self.city_entry = tk.Entry(self.root, width=30)
        self.city_entry.pack()

        get_weather_btn = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        get_weather_btn.pack(pady=10)

        self.weather_display = tk.Label(self.root, text="", font=('Helvetica', 12), fg="blue")
        self.weather_display.pack()

    def get_weather(self):
        """Fetches weather forecast for the entered city."""
        api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
        city = self.city_entry.get()

        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(base_url)
            weather_data = response.json()

            if weather_data["cod"] != 200:
                messagebox.showerror("Error", f"City '{city}' not found.")
                return

            temperature = weather_data["main"]["temp"]
            weather_condition = weather_data["weather"][0]["description"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            weather_info = f"Temperature: {temperature}°C\nCondition: {weather_condition}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            self.weather_display.config(text=weather_info)

        except Exception as e:
            messagebox.showerror("Error", "Failed to fetch weather data.")
            print(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarWeatherApp(root)
    root.mainloop()

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompt the user to enter a number of days and display the future date after adding those days.
    The future date is formatted as 'YYYY-MM-DD'.
    """
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

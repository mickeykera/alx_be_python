from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(future_date):
    days = int(future_date)
    future_datetime = datetime.now() + timedelta(days=days)
    return future_datetime.strftime("%Y-%m-%d %H:%M:%S")
if __name__ == "__main__":
    display_current_datetime()
    future_date = input("Enter the number of days to add to the current date: ")
    future_formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future Date: {future_formatted_date}")
    
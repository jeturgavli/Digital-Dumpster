from datetime import datetime, date

def calculate_age(birth_str):
    try:
        birth_date = datetime.strptime(birth_str, "%d-%m-%Y").date()
        today = date.today()

        total_days = (today - birth_date).days

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            last_month = (today.replace(day=1) - timedelta(days=1)).day
            days += last_month

        if months < 0:
            years -= 1
            months += 12

        # Output
        print("-----------------------------------------------------")
        print(f"\n📅 Birthdate: {birth_date.strftime('%d-%m-%Y')}")
        print(f"🎂 Age: {years} years, {months} months, {days} days")
        print(f"📆 Total days lived: {total_days} days")
        print("-----------------------------------------------------")
        

    except ValueError:
        print("❌ Invalid date format. Please use DD-MM-YYYY.")

user_input = input("Enter your birthdate (DD-MM-YYYY): ")
calculate_age(user_input)

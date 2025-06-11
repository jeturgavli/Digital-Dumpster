from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_saving_plan():
    print("🧮 PS5/Goal Savings Time Estimator")

    # Input from user
    target = int(input("🎯 Enter your saving goal (₹): "))
    current = int(input("💰 How much have you saved so far (₹): "))
    monthly = int(input("📆 How much can you save per month (₹): "))

    if current >= target:
        print("✅ You already have enough saved! Go buy it now 😄")
        return

    months = 0
    date = datetime.today()
    total = current

    print("\n📅 Monthly Plan:")
    print("--------------------------")
    while total < target:
        months += 1
        save = min(monthly, target - total)
        total += save
        date += relativedelta(months=1)
        print(f"{months}. {date.strftime('%B %Y')} => Saved ₹{save} | Total: ₹{total}")

    # Final output
    print("\n🕒 You will reach your goal in", months, "months.")
    print("🎉 Target will be achieved by:", date.strftime("%B %Y"))

# Run the script
calculate_saving_plan()

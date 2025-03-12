from day_query import single_day_top_sales
from rich.prompt import Prompt, Confirm

while True:

    day = Prompt.ask("Enter a date for office sales:", default="2025-01-02")
    print("You said", day)

    try:
        row = single_day_top_sales(day)
        print({"Theater": row[0], "Total": row[1], "Date": day})
    except ValueError as e:
        print(e)

    if not Confirm.ask("Continue?"):
        print("K, bye.")
        break

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(year: int, month: int) -> int:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_leap_year(year):
        return 29
        
    return days_in_month[month]


def get_next_date(year: int, month: int, day: int) -> str:
    if day < get_days_in_month(year, month):
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
            
    # Sostituisce lo String.format("%04d-%02d-%02d") di Java usando le f-string di Python
    return f"{year:04d}-{month:02d}-{day:02d}"


def main():
    # In Python l'input da console si gestisce direttamente con la funzione nativa input()
    input_date = input("Enter a date (yyyy-MM-dd): ")
    
    # Suddividiamo la stringa proprio come faceva parts = inputDate.split("-")
    parts = input_date.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    
    next_date = get_next_date(year, month, day)
    print(f"Next date: {next_date}")


# Questo blocco assicura che il main parta solo se esegui direttamente questo file
if __name__ == "__main__":
    main()
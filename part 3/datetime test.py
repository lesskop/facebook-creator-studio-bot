from datetime import datetime

def get_last_date():
	now = datetime.now()

	year_now = int(now.strftime("%Y"))

	month_now = int(now.strftime("%m"))

	day_now = int(now.strftime("%d"))

	count_days = 0

	for month in range(month_now, month_now + 4):

		if year_now % 4 == 0:
			feb = 29
		else:
			feb = 28

		days_in_month = {1: 31, 2: feb, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

		if month % 12 == 0:
			m = 12
		else:
			m = month % 12

		if count_days == 75:
			break

		for day in range(day_now, days_in_month[m] + 1):

			count_days += 1

			if count_days == 75:
				last_date = f'{day}.{m}.{year_now}'
				break

			if day == days_in_month[m]:
				day_now = 1
				if month % 12 == 0:
					year_now += 1

	return last_date

get_last_date()
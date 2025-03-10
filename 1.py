import requests, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    if data['cod'] != 200: return None
    return f"Good Morning...!!\n\nWeather Report of {data['name']}, {data['sys']['country']}:\nLongitude {data['coord']['lon']}°, Latitude {data['coord']['lat']}°\nTemp: {data['main']['temp']}°C (Max: {data['main']['temp_max']}°C, Min: {data['main']['temp_min']}°C)\nFeels like: {data['main']['feels_like']}°C\nWeather: {data['weather'][0]['description']}\nHumidity: {data['main']['humidity']}%\nWind Speed: {data['wind']['speed']} m/s\n\nHave a Nice Day..."

def send_email(subject, body, to_email, from_email, from_password):
    msg = MIMEMultipart()
    msg['From'], msg['To'], msg['Subject'] = from_email, to_email, subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def save_report_to_file(report, filename="weather_report.txt"):
    with open(filename, "w") as file:
        file.write(report)
    print(f"Report saved to {filename}")

def main():
    city_name = input("Enter the city name: ")
    api_key = '5a204d2cf20bb44c760f50810e7d1af4'
    report = get_weather(city_name, api_key)
    if report:
        print(report)
        save_report_to_file(report)
        send_email(f"Weather Report for {city_name}", report, "tiwaridon007@gmail.com", "ritikrawat6510@gmail.com", "xuwc qpwo wbug fvoi")
    else:
        print("City not found or unable to fetch data.")

if __name__ == "__main__":
    main()


# GWALIOR, IN
# NOTE-: App Password  main jakr ctraete password kro tehn use pass wordko yahan use kro
#  and add email also  jise bhejna h


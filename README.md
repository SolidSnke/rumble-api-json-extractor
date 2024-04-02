A simple project that uses Python to call the Rumble.com API and read the JSON. After getting the data broke down you can get any information provided by the API. I use it in this example to get the Live user count from the API, and put it into a text file for OBS to read and display on screen.

I run this on a windows machine using Task Scheduler and in a batch file. I have found the script runs in just under 3secs in CMD and PowerShell. I run the script every minute to update the text file.

INSTALLATION; just need to install Python - https://www.python.org/ - which in windows is just running the executable from pythons website.

- First, open powershell/cmd and start with installing the requests package in Python; pip install requests
- Additionally you want to install JSON; pip install json
-	after that you should be good to go on running the script, where ever you run the script is where the text file is created.

If you find this useful, please feel to buy me a beer @GoChadTV (Venmo) - $GoChadTV (CashApp) - https://ko-fi.com/gochadtv

To see a working example of this, goto; https://rumble.com/CountryMusicRdo/live - This is the current process I use since 4/1/2024, before I used screen scraping to get the live user count.

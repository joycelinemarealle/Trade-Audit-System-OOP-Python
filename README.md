

# Trade-Audit-System-OOP-Python
SUMMARY:For this project, I developed a Python-based trade auditing system for a brokerage firm, utilizing Object-Oriented principles and TDD, to accurately model and process daily stock trades and generate end-of-day financial summaries.

PROJECT DETAILS: 
A brokerage firm undertakes many different types of trades on a daily basis, some of them being:
Stock trades
Bond trades
Futures trades
Forex trades
At the end of each day of trading, the firm has an obligation to the legal jurisdiction of the territory in which it operates to disclose its financial position to the regulators of that territory. To satisfy this requirement the firm must audit the basis for this financial position.

Your task is to create a system for auditing stock trades performed by the firm over the period of a given day.

Part 1: Modelling Trades
For the purposes of this piece of work, all stock trades have:
a unique trade ID
an code that identifies the exchange where the trade took place
a symbol that identitfies what was traded
a price that the trade was executed at (priced in US Dollars and Cents)
the quantity traded
the side (buy or sell)

Different types of trades calculate the value of the trade in different ways. For this work, we will only consider stock trades, but, your design should be ready for any other kind of trade in the future.
The value of a stock trade is calculated by multiplying the price that the trade was executed at, by the quantity traded.
For this work, the unique ID of the trade can be synthesized (for example, concatenating the string id with the string value of a unique, incrementing integer value, such as id1,id2, id3 ...).

FR1: Modelling stock trades
Use Object-Oriented techniques to model stock trades. Identify an apprpriate class hierchy (including abstract classes). Do not implement these classes yet.

FR2: Using tests to undertake a TDD approach to developing trade classess
Using an appropriate testing frame work, and using a TDD approach, write tests to verify that an instance of a 
Stock object had been successfully created, and that any behaviour that is should exhibit is correct.

FR3: Implementing classes
Using OO techniques, write one or more Python classes to implement your model.

Ensure that you are using appropriate:
Naming (of classes, methods, data members, etc.)
Inheritance and constructor calls
Operator overloads (where appropriate - the requirement for these will become clearer later, so you can add these when you need them)
Method overriding
Conventions for where your class definitions are stored (i.e. in their own files)
A string format to represent a generic Trade object when it is printed out (and if appropriate a specialized version for a Stock object)
The order in which the arguments will passed to the constructor for 
Stock trades is:
Trade ID
Exchange
Symbol
Price
Quantity
Side
As you are developing your class, ensure that it passes the tests that you wrote earlier.

FR4: Writing a driver program
Ensure that your code is able to use the following driver program (which should be stored in it's own standalone file):

### Appropriate import statements here ...
 
stock1 = Stock("id1", "CHX", "FB", 100.00, 120, "sell")
print(stock1)
stock2 = Stock("id2", "NASDAQ", "AAPL", 150.50, 75, "buy")
print(stock2)
stock3 = Stock("id3", "CHX", "ORCL", 70.22, 160, "sell")
print(stock3)
stock4 = Stock("id4", "NYSE", "F", 50.34, 200, "buy")
print(stock4)
stock5 = Stock("id5", "NASDAQ", "AAPL", 155.99, 65, "buy")
print(stock5)
stock6 = Stock("id6", "NASDAQ", "F", 55.12, 200, "buy")
print(stock6)
stock7 = Stock("id7", "NYSE", "FB", 100.34, 120, "sell")
print(stock7)
stock8 = Stock("id8", "CHX", "AAPL", 150.44, 75, "buy")
print(stock8)
stock9 = Stock("id9", "NYSE", "AAPL", 150.73, 80, "sell")
print(stock9)
stock10 = Stock("id10", "CHX", "ORCL", 75.89, 170, "sell")
print(stock10)
Part 2: Processing A Trading Activity Log
The trading activity for any specific day is recorded in CSV files, with each row describing a single trade that has taken place. There is no header line describing the columns in the file, and each element is separated by a semi-colon (;).

The data file for this work is called trades.csv and clicking here will download it.

The format of each line is: time;exchange;symbol;volume;price;side
The fields are: 
time : the time at which the trade took place to millisecond granularity
exchange: the exchange where the trade was executed
symbol: the stock market ticker symbol representing the stock that was traded
volume: the quantity of shares traded (bought or sold)
price: the stock price in US Dollars and Cents
side: whether the transaction was a buy or sell of stock

Example entries are:

09:30:00.000;CHX;MSFT;3000;404.29;sell
09:30:00.200;NASDAQ;AAPL;7600;199.32;buy
09:30:00.400;NYSE;IBM;8800;190.46;buy

Hint: When you are reading the contents of this file, treat every record (line) as a collection of strings, and then convert them to the appropriate type (e.g int or float) when calling the 
Stock constructor.

FR5: Reading and processing the trading log file
Write code to prompt for the path to the transaction file, and then have your program read the file's contents into a suitable representation.

Note: this representation should be used for the following sections. The trades.csv file should be read and processed only once during any run of the program.

FR6: Identifying the firm's end of day positons. Write code to generate the following summary statistics:

Summarise the total value of all trades for a given day (see below for a description of what is required for the summary).
Prompt for and read a specific stock symbol, filter by that symbol and summarise the total values for the trades in that stock (see below for a description of what is required for the summary).
Prompt for and read a specific exchange name, filter by that exchange and summarise the total values for the trades performed with the exchange (see below).
NOTE: The valueof a stock trade is calculated by multiplying the 
price that the stock trade was executed at, by the quantitytraded.

NOTE: For each of the summaries of the total value of the trades identified above, there should be two values displayed:
The total of the amount spent on purchases (buy trades)
The total amount received from sales (selltrades)

FR7: Monitor how traders are performing
The file actually contains the stock trades initiated by a specific trader (by submitting a request strategy to an algorithmic trading platform - there is no way that a trader could perform a trade every 200 milliseconds thoughout the day!).

The value of the first trade of the day that is executed should be, approximately, the average value of all of the days trades.

To see how well the traders are performing in this respect, all of the trades for the day are to be monitored using a special trade book, as follows:

The first trade of the day is used as the basis for comparing the remaining trades
The value of the remaining trades are compared to the first one, and are classified as:
larger than the first trade
smaller than the first trade
the same as the first trade
You will need to design, test and implement a dedicated Tradebook class for this section, in it's own source code file.

Depending upon the classification, the trade is added to an appropriate list in the book.

The comparison behaviour of whether one trade is larger / smaller / the same as another should be a part of the trade, not simply done comparing the value of the trade in the Book.

For example, the following pseudo code is an example of how the trades could be compared:

if first trade being processed
   'add new_trade into the reference list'
if new_trade > first_trade:
   'add new_trade in the big_trades_list'
elif new_trade < first_trade:
   'add new_trade into the small_trades_list'
else:
   'add new_trade into the same list as the first trade (reference trade)'
Once all of the days' trades have been categorised, there should be summary statistics printed for each list:

How many items are in each list?
What is the average value of trades for each list?
Ensure that your implementation of the trade book will allow the following code to be run (when using the sample trades as shown in FR4) to add the trades, and generate the statistics :

# Call the Tradebook constructor
tradebook = Tradebook()
 
# Add the trades to the Tradebook
tradebook.add(stock1)
tradebook.add(stock2)
tradebook.add(stock3)
tradebook.add(stock4)
tradebook.add(stock5)
tradebook.add(stock6)
tradebook.add(stock7)
tradebook.add(stock8)
tradebook.add(stock9)
tradebook.add(stock10)
 
# Generate and print the statistics
tradebook.print_reference_trades_statistics()
tradebook.print_small_trades_statistics()
tradebook.print_large_trades_statistics()
Modify your code so that it actually uses the representation that you have created for the stock trades recorded in the 
trades.csv
 file.

FR8: Extended Functionality (time permitting)
1. Using a floating point type, especially for any kinds of calculations involving currencies, is a really bad idea (see this Python specific discussion, or this slightly more theoretical treatise).

- Once approach would be to use the Python Decimal type instead (see here).
- Modify your code to use the Python Decimal type instead of floating point types, whever they are defined.
- Is there any difference in the output of the statistics once you hae made the changes?

2.Using PyTest, demonstrate the appropriate use of mock objects as part of your testing. You may wish to mock the call to the summary statistics code, for example.


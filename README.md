# Project 1: Crypto Wallet

![image](https://user-images.githubusercontent.com/89135778/193613110-e74db9e8-839d-49c8-bb3e-4e790765b783.png)
# Criteria A: Planning

## Problem definition
Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data store is
| Date | Description | Category | Amount |
|:-----:|:---------:|:------:|:-----:|
| Sep 23 2022 | bought a house | expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | food | 0.000001 BTC |


## Proposed Solution

### Design statement:
I will design and make a digital ledger for a client who is a trader. The digital ledger will consist on a tool for being able to keep track of cryptocurrencies investments, transactions and to know some statistics, and is constructed using the software Python. It will take 3 weeks to make and will be evaluated according to the criteria A and B.

### Rationale for the Proposed Solution
The program starts with a quick description of it, followed by a login system so the user's personal data doesn't get accessed third people. The user will be able to change the username and the password.
Then, the program has a list of actions, which makes the user's experience more enjoyable, as they will be able to choose quickly what they want to do.
After the user chooses an option, a function for that option runs, making the code clearer and easier to understand for developers.
There are comments on each step, so someone that reads the code can understand what is happening easily. Also, there are functions that make the code simple and variables with names that are understandable.

About the software selected, Python is one of the most accessible programming languages because it is not complicated and has simplified syntax very similar to the English language, which is perfect for beginners.[^1] According to Stack Overflow Developer Survey in 2022, 48% of programmers use Python[^2], so there is a big Internet community for asking for help. Also, its codes can be easily written and executed much faster than other programming languages[^3]. Python is an open source and has a lot of libraries to complement the code[^4], so you can do practically anything with your code.

[^1]: Makai, Matt. “Why Use Python?” Full Stack Python, 2021, https://www.fullstackpython.com/why-use-python.html.
[^2]: “Stack Overflow Developer Survey 2022.” Stack Overflow, May 2022, https://survey.stackoverflow.co/2022/#most-popular-technologies-language. 
[^3]: citation needed
[^4]: citation needed


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The user will only be able to see the data in the program after entering a password.
5. It will give value in two different currencies: EUR (Euros) and JPY (Yen).
6. The program will show statistics and graphs: total coins in the wallet, total money spent, money spent in each category
7. The program will show the real time value of the cryptocurrency.


# Criteria B: Design

## Test Plan
| Test | Description | Procedure | Expected Output |
|:----:|:-----------:|:---------:|:---------------:|
| Unit test of the login system | This test is evaluating the function for the login system | 1. Run the program main.py in CryptoWallet 2. Enter a username and a password | If the username and password are incorrect, the program will give two more oportunities. If the username and password are correct, it will show the rest of the program. | 
| Unit test of Option 1 |  |  |  
| Unit test of Option 2 |  |  |  
| Unit test of Option 3 |  |  |  

## System Diagram
![systemdiagram-systemdiagram drawio](https://user-images.githubusercontent.com/89135778/193449826-f7f245d0-d90a-4537-a517-168e76d2c484.png)

**Figure 1:** System diagram of my project

Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (main, login, website_data and proj_lib). Then, these codes connect with a database of csv files (data_transactions and login).

## Flow Diagrams

## User Interface Sketch


## Record of Tasks (make it chronological!)
| Task Number |                Planned Action                |                                            Planned Outcome                                           | Time estimate | Target completion date | Criterion |
|:-----------:|:--------------------------------------------:|:----------------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|
|      1      |             Create system diagram            |       To have a clear idea of the hardware and software requirements for the proposed solution       |     10min     |         Sep 24         |     B     |
|      2      |                 Code the MVP                 |                                                                                                      |       5h      |         Sep 22         |     C     |
|      3      |            Draw the flow diagrams            |                  To have clear ideas on how to code and how the programme would work                 |      1h30     |         Sep 30         |     B     |
|      4      | Write proposed solution and success criteria |           For having clear ideas about the project, the design, the software and the goals.          |     10min     |         Sep 22         |     A     |
|      5      |          Draw user interface sketch          |                             To know how the digital ledger will look like                            |     15min     |         Sep 20         |     B     |
|      6      |                Finish the code               |                                    To have the final project ready                                   |       5h      |          Oct 3         |     C     |
|      7      |               Test the project               |                    Different UWC ISAK Japan students will try my program as users                    |     20min     |          Oct 4         |     E     |
|      8      |      Improve user intuitive instructions     | Change some codes so it is easier for the user to understand the program, based on the previous test |     30min     |          Oct 4         |     C     |
|      9      |        Write future improvements ideas       |                   So the client can see that the program can be improved over time                   |     10min     |          Oct 4         |     B     |

**Table 1:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development (criterias A, B and C). The target completion date and the time estimate for each task is also shown.

# Criterion C

## Existing tools
This refers to the software tools used during the development of the solution, and structures such as for loops, and bash commands

## Sources
When code was researched in the web, proper citation is used to give credit to the original author.

## Tools used in Unit 1
- Functions
- For/while loops
- Input Validation
- If statements
- Encryption

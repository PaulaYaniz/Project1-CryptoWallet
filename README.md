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

Right now, there are multiple digital ledgers for cryptocurrencies. It is easy to find a lot of examples of them with a quick search on the internet. However, the digital ledger Ms. Sato wants will be made especially for her, so she will be able to totally personalize it and to add all the functions she want. Also, it will run locally in her computer, not on a website.

## Proposed Solution

### Design statement:
I will design and make a digital ledger for a client who is a trader. The digital ledger will consist on a tool for being able to keep track of cryptocurrencies investments, transactions and to know some statistics, and is constructed using the software Python. It will take 3 weeks to make and will be evaluated according to the criteria A and B.

### Rationale for the Proposed Solution
The program starts with a brief description of the cryptocurrency, followed by a login system so the user's personal data doesn't get accessed by third people. The user will be able to change the username and the password once the program is open.
Then, the program has a list of actions, which makes the user's experience more enjoyable, as they will be able to choose quickly what they want to do.
After the user chooses an option, that option runs. Each option is separated with comments, making the code clearer and easier to understand for developers.
There are also comments on each step, so someone that reads the code can understand what is happening easily. Also, there are functions that make the code simple and variables with names that are understandable.

About the software selected, Python is one of the most accessible programming languages because it is not complicated and has simplified syntax very similar to the English language, which is perfect for beginners.[^1] According to Stack Overflow Developer Survey in 2022, 48% of programmers use Python[^2], so there is a big Internet community for asking for help. Also, its codes can be easily written and executed much faster than other programming languages[^3]. Python is an open source and has a lot of libraries to complement the code[^4], so you can do practically anything with your code.

[^1]: Makai, Matt. “Why Use Python?” Full Stack Python, 2021, https://www.fullstackpython.com/why-use-python.html.
[^2]: “Stack Overflow Developer Survey 2022.” Stack Overflow, May 2022, https://survey.stackoverflow.co/2022/#most-popular-technologies-language. 
[^3]: “Advantages of Python over Other Programming Languages.” Vilmate, 2019, https://vilmate.com/blog/python-vs-other-programming-languages/. 
[^4]: “About Python.” Python.org, https://www.python.org/about/. 


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the XLM.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The user will only be able to see the data in the program after entering a correct username and password.
5. The program will show statistics: total coins in the wallet, total money spent and net balance.
6. The program will show a graph: changes in the XLM value during time.
7. The program will show the real time value of the XLM in EUR (euros) and JPY (yen) connecting to the internet.


# Criteria B: Design

## Test Plan
| Test | Description | Procedure | Expected Output |
|:----:|:-----------:|:---------:|:---------------:|
| Unit test of the login system | This test is evaluating the function for the login system | 1. Run the program CryptoWalletMain.py in CryptoWallet 2. Enter a username and a password | If the username and password are incorrect, the program will not show its content. If the username and password are correct, it will show the rest of the program. | 
| Unit test of Option 1 | This test is evaluation option 1, showing all data | The user press the "1" key after the program asks for it. | A table will be shown with all the information it is on the csv file of the data of the program. |  
| Unit test of Option 2 | This test in evaluating option 2, deposit of crypto. | 1. Run the  program CryptoWalletMain.py in CryptoWallet 2. Enter the correct username and password. 3. Press "2" key after the program asks for it. | It should appear a initial message explaining what is happening. Then, questions about your transaction (quantity, value, description) so the program can add the data to the csv file. | 
| Unit test of Option 6 | This test is evaluating option 6, real-time value of the XLM. | 1. Run the  program CryptoWalletMain.py in CryptoWallet 2. Enter the correct username and password. 3. The user press the "6" key after the program asks for it. | The program should try to connect to an internet website to get the data. Then, it will print it. If there is no internet conection, it should appear a message of error. |  

## System Diagram
![systemdiagram-systemdiagram drawio](https://user-images.githubusercontent.com/89135778/193449826-f7f245d0-d90a-4537-a517-168e76d2c484.png)

**Figure 1:** System diagram of my project

Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (main, login, website_data and proj_lib). Then, these codes connect with a database of csv files (data_transactions and login).

## Flow Diagrams

## Record of Tasks (make it chronological!)
| Task Number |                Planned Action                |                                            Planned Outcome                                           | Time estimate | Target completion date | Criterion |
|:-----------:|:--------------------------------------------:|:----------------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|
|      1      |             Create system diagram            |       To have a clear idea of the hardware and software requirements for the proposed solution       |     10min     |         Sep 22         |     B     |
|      2      |                 Code the MVP                 |                         To show the client the basic working of the program.                         |       5h      |         Sep 24         |     C     |
|      3      |            Draw the flow diagrams            |                  To have clear ideas on how to code and how the programme would work                 |      1h30     |         Sep 27         |     B     |
|      4      | Write proposed solution and success criteria |           For having clear ideas about the project, the design, the software and the goals.          |     10min     |         Sep 28         |     A     |
|      5      |                Write test plan               |                   For knowing the things that should work and how they should work.                  |     30min     |         Sep 30         |     B     |
|      6      |                Finish the code               |                                    To have the final project ready                                   |       5h      |          Oct 3         |     C     |
|      7      |               Test the project               |                    Different UWC ISAK Japan students will try my program as users                    |     20min     |          Oct 7         |     E     |
|      8      |      Improve user intuitive instructions     | Change some codes so it is easier for the user to understand the program, based on the previous test |     30min     |          Oct 8         |     C     |
|      9      |                Final revision                |                Prove that everything is working and I have all the information needed                |       1h      |          Oct 9         |  A,B,C,E  |

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

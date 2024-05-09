Treasury-Bill_calculator
A calculator that gives you your interest earned on any amount you invest
Treasury Bill calculator
Selenium and Python
Treasury Bills are control by the governemnt and banks use certain percentages to calculate how much you will earn from your investment 
There are three yields for your investment(91 days, 182 and 365 days)
Depending on the number of days you pick your interest amount would be calculated
Face value(FV) - Amount to be invested 
Purchasing price(PP) - Amount you actually pay
Interest earned(IE) - the interest you earn on your investment
IEY(Interst earned yearly)
DR(Discount rate) - how much discount you get for your investment. This is tell you how much you will actually pay for the bill(PP)
Implementation works

PP = FV x (1 - ((DRxT)/365)) -------------------------------------
IE = FV - PP -----------------------------------------------------
EAY = (FV/PP)^365/T -1 -------------------------------------------

Task to add
SQL database that stores the necessary values at midnight

Frontend - for users

To run application on your local machine
1. Clone project
2. Run source venv/bin/activate on your terminal to activate virtual environment
3. Run  python .\TreasuryBillCalculator\Calculator.py on your terminal


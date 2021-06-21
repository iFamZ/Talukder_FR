This is the submission to Fetch Rewards coding exercise from Famim Talukder.

I used the flask framework to create the web service. 

Steps to Run the Service:
1. This service was developed in Python3.8.10 - please ensure that Python3 is being used
2. Install flask within python
- pip install -r requirements.txt
3. Run the web service
- python3 pythonWebService_tested.py
4. A local address will be displayed in your terminal - go to that address to interact with the web service
5. Append the routes from below at the end of the local address to utilize them

Functions:
1. getPointBalance() --> route: '/getPointsBalance'
- returns the point balance of each payer in the database
2. addTransaction() --> route: '/addTransaction'
- adds individual transaction to the database using the templates/form.html for input data
3. spendPoints() --> route: '/spendPoints'
- spends points utilizing the logic stated in the problem statement.
- the input is taken in using the templates/spend.html
4. getTransactions() --> route: '/getTransactions'
- debugging method used to get a copy of the database
- commented out after test phase


One conscious decision made in this project is not to delete payers with 0 points in the database.
This affects the point balance route. It was also a conscious decision to not include these in the
return call to spendPoints. For instance, if we have payer A with 0 points and payer B with 100
points, chronologically sorted, and we want to spend 100 points. One solution will be to show
payer A with 0 point spend and payer B with 100 points spent. That is not what I choose to do,
instead I will only show payers with positive points spent.

I appreciate your time and consideration, please reach out to me if you have specific questions on
how I designed this project. You can reach me at 646-428-4844 or via email at famim123@gmail.com.

Thanks!
Famim
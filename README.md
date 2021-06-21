This is the submission to Fetch Rewards coding exercise from Famim Talukder.

I used the flask framework to create the web service. 

Steps to Run the Service:
1. This service was developed in Python3.8.10 - please ensure that Python3 is being used
2. Install flask within python
- pip install -r requirements.txt
3. Run the web service
- python3 pythonWebService_tested.py
4. A local address will be displayed in your terminal - go to that address to interact with the web service



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
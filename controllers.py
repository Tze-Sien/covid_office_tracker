import controllers
from csv import writer 
import pandas as pd
import json
from datetime import date
from ast import literal_eval

# ------- User Controllers ------- #

def signup(data):   

    dataframe = pd.DataFrame.from_dict(data, orient='index').T
    dataframe.to_csv('./data/user_profile.csv', mode='a', header=None, index=False)
    
    data = {
        "email" : data['email'],
        "pass": True
    }

    return data

def signin(data):

    email = data['email']
    pw = data['pw']

    import pandas as pd
    df = pd.read_csv(
        './data/user_profile.csv'
    )
    result_email = df.loc[df['email'].str.contains(email)] 
    result_pw = df.loc[df['pw'].str.contains(pw)] 

    if ((len(result_email) > 0) and (len(result_pw) > 0)):
        data = {
            "pass": True,
            "email": email
        }
    else:
        data = {
            "pass": False,
            "email": 'N/A'
        }

    return data

def checkin(data):

    time = date.today()
    time = time.strftime("%d/%m/%Y")
    data['date'] = time

    # 1. Get Personal Details
    email = data['email']
    df = pd.read_csv('./data/user_profile.csv')
    result_email = df.loc[df['email'].str.contains(email)] #dataframe

    # 2. Get the alert setting
    alert = pd.read_csv('./data/alert.csv')
    
    
    # 3. Checking
    error_msg = "Dissaproved:"
    before = len(error_msg)

    for x in alert:
        if x == "departments":
            
            for y in alert[x]:
                y = literal_eval(y)
                if y[0] == result_email['department'].values:
                    error_msg += "Department Restricted | "

        elif isinstance(alert[x][0], str):
            to_list = literal_eval(alert[x][0])
            if(to_list[0] == data[x][0]):
                error_msg += "{} |".format(x)
        else:
            if alert[x][0] != data[x]:
                error_msg += "{} |".format(x)
    
    # Creating New Index 
    read = pd.read_csv('./data/track_user.csv')
    new_index = len(read) + 1
    dataframe = pd.DataFrame.from_dict(data, orient='index')
    
    # Reindex date to front
    a = dataframe.index.to_list()[0:-1]
    b = dataframe.index.to_list()[-1:]
    for x in a:
        b.append(x)


    # Restrcited
    if before != len(error_msg):
        approve_stats = False
    else:
        approve_stats = True

    dataframe = dataframe.reindex(b).T
    dataframe['id'] = new_index
    dataframe['approve'] = approve_stats
    dataframe.to_csv('./data/track_user.csv', mode='a', header=False, index=False)

    res = {
        "pass":approve_stats,
        "email":dataframe['email'][0],
        "id": dataframe['id'][0].astype(str),
        "message": error_msg if before != len(error_msg) else "Welcome"
    }

    return res


# ------- Admin Controllers ------- #

def adlogin(data):

    email = data['email']
    pw = data['pw']

    if email == "admin@gmail.com" and pw == "admin":
        data = {
            "pass": True
        }
    else:
        data = {
            "pass": False
        }

    return data

# ------- Admin > Alert ------- #

def alert(data):
    
    dataframe = pd.DataFrame.from_dict(data, orient='index').T
    print(dataframe)

    dataframe.to_csv('./data/alert.csv', index=None, header=True)

    return {
		"pass": True
    }   

# ------- Admin > Dashboard ------- #

def dbalert(data):
    return data

def dbamount(data):
    
    return data


# Extra Stuffs
def doorcheck(department, record_id):
    print(record_id)
    # Find the series with record_id
    # Update the row
    # Put back
    return (department + record_id)
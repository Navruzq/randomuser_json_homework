from from_json import read_json as a
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    s=[]
    for i in data['users']:
        if i['gender']=='male':
            s.append(i)
    return s 
data=a('users.json')
print(get_male_users(data))
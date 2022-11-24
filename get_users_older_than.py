from from_json import read_json
def get_users_older_than(data:dict, age:int)->list:
    """Gets all users older than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    a=[]
    for i in data['users']:

        if i['age']>=age:
            a.append(i)
    return a 
data = read_json('users.json')
print(get_users_older_than(data,25))
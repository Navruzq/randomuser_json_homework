from from_json import read_json as a
def get_male_users_from_country(data:dict, country:str)->list:
    """
    Get male users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:

        list: A list of users
    """ 
    s=[]
    for i in data['users']:
        if i['gender']=='male' and i['country']==country:
            s.append(i)
    return s 
data=a('users.json')
print(get_male_users_from_country(data,'Norway'))

    
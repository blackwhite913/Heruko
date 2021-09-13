from models.user import User
from werkzeug.security import safe_str_cmp


#username_mapping={'bob':User(1,'bob','asdf')}
#username_mapping={u.username:u for u in users}
#this is writing the above example in complex python
# run the for loop for the lentgh of users and perform
# u.username:u
#mini function
#userid_mapping ={1:User(1,'bob','asdf')}  
#userid_mapping ={ u.id:u for u in users}     
# the above thing is done so that there is a unique id or name respectively,for
# peice of dictionary

#this is the authenticate function for the logic of check user loggin 
def authenticate(username,password):
    #user will store the dictionary object from the list of users
    #cause username_mapping is a dictionary which has a get method which takes in  a key and returns its value
    user= User.find_by_username(username)
    print(user)
    #weird dictionary thing
    if user and safe_str_cmp(user.password,password):
        return user

        
def identity(payload):
    user_id=payload['identity']
    return User.find_by_id(user_id)
    #object method be passed by a default value as they aint no contructors



    


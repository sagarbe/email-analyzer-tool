# Email Analyzer Tool

emails = [
    'ravi123@gmail.com',
    'priya.kumar@yahoo.com',
    'aman99@hotmail.com',
    'sneha_p@outlook.com',
    'amitverma@gmail.com',
    'usha123@yahoo.com'
]

# 1. Extract usernames
# 2. Extract unique domains
# 3. Map each email → domain
# 4. Count emails per domain
# 5. Print usernames that start with vowels
# 6. Display all in a formatted summary
user_names=[]
domains=set()
email_domain={}
email_count={}
vowel_user=[]
def em():
    try:
        for user in emails:
            user_name=user.split('@')[0]
            user_names.append(user_name)
            
            domain=user.split("@")[1]
            domains.add(domain)
        
            email_domain[user]=domain
        
            if domain not in email_count:
                email_count[domain]=1
            else:
                 email_count[domain]+=1
        
            if user_name.lower().startswith(('a','e','i','o','u')):
                vowel_user.append(user_name)
                
        print('username are:',user_names)
        print('domains are',domains)
        print("email:domaine--",email_domain)
        print("domain count are:",email_count)
        print("user name start with vowels are:",vowel_user)
    except exception as e:
        print("error is",e)
em()
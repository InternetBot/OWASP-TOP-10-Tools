import requests

'''example of user roles gotten from 
https://stackoverflow.com/questions/1598411/what-names-for-standard-website-user-roles '''

roles = ['admin', 'manager', 'editor', 'author', 'contributors', 'moderator', 'member',
         'subscriber', 'user', 'guest']

# ps you can change or add to the endpoint as you please
endpoints = [
    '/admin/dashboard',
    '/admin/settings',
    '/manager/reports',
    '/manager/team',
    '/editor/content',
    '/editor/publish',
    '/author/posts',
    '/author/new',
    '/contributors/submissions',
    '/moderator/review',
    '/moderator/approve',
    '/member/profile',
    '/member/settings',
    '/subscriber/content',
    '/subscriber/newsletter',
    '/user/home',
    '/user/profile',
    '/guest/welcome',
    '/guest/info'
]

# ps you can change or add to the credential as you please
credentials = {
    'admin': ('admin', 'admin'),
    'manager': ('manager', 'manager'),
    'editor': ('editor', 'editor'),
    'author': ('author', 'author'),
    'contributors': ('contributors', 'contributors'),
    'moderator': ('moderator', 'moderator'),
    'member': ('member', 'member'),
    'subscriber': ('subscriber', 'subscriber'),
    'user': ('user', 'user'),
    'guest': ('guest', 'guest'),
    
    'admin_user': ('admin_user', 'admin_password'),
    'manager_user': ('manager_user', 'manager_password'),
    'editor_user': ('editor_user', 'editor_password'),
    'author_user': ('author_user', 'author_password'),
    'contributor_user': ('contributor_user', 'contributor_password'),
    'moderator_user': ('moderator_user', 'moderator_password'),
    'member_user': ('member_user', 'member_password'),
    'subscriber_user': ('subscriber_user', 'subscriber_password'),
    'user_user': ('user_user', 'user_password'),
    'guest_user': ('guest_user', 'guest_password')
}

def testing_access(test_url):
    results = []

    for endpoint in endpoints:
        for role in roles:
            url = f"{test_url}{endpoint}"
            username, password = credentials[role]

            session = requests.Session()
            login_response = session.post(f"{test_url}/login", data={'username': username, 'password': password})
            
            response = session.get(url)
            
            # condition to check if access is granted 
            if response.status_code == 200:
                results.append((role, endpoint, 'Access Granted'))
            else:
                results.append((role, endpoint, 'Access Denied'))
    
    return results

def main():
    test_url = 'YOUR LINK GOES HERE '  # use a vulnerable website of choice - http://www.itsecgames.com/
    results = testing_access(test_url)
    
    for result in results:
        role, endpoint, access = result
        print(f"Role: {role}, Endpoint: {endpoint}, Access: {access}")
        print("")

if __name__ == '__main__':
    main()



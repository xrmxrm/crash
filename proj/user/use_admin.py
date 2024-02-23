from admin import Admin, Privileges

susan_priv_list = ['can ban', 'can delete']
susan_priv = Privileges(susan_priv_list)
susan = Admin('susan', 'smith', 
              'ssmith', 'ssmith@gmail.com',
              'HQ', susan_priv)

susan.privileges.show_privileges()
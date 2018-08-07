import webapp2
import jinja2
import os
import random
 

#dictionary is above the the_jinja_env
def get_login():    
        accounts = [
        {
            "username": "Admin",
            "password": "123"
        }
    ]   


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
   
class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
 
class ContactPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/contact.html')
        self.response.write(about_template.render())
       
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/login.html')
        self.response.write(about_template.render())
        
    def post(self):
        isError = False
        if (isError):
            self.response.write("Error!")
        else: 
            self.redirect("templates/about.html")


       
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/contact', ContactPage),
    ('/about', AboutPage),
    ('/login', LoginPage),
], debug=True)
import pyshorteners
import eel
  
eel.init("web")  
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python(link):
        sh = pyshorteners.Shortener()
        x = (sh.tinyurl.short(link))
        return x    

# Start the index.html file
eel.start("index.html" , port=8000 , mode = 'chrome')
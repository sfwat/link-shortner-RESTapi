# link-shortner-RESTapi
This is a simple api service for link shortening,
In the POST method it take 3 links one for each platform and create an alternative short link for them,
When a GET method is recieved a list of the shortened links with their original ones is returned
And through a PUT request the api update any of the platform original links by taking the shortened link.

#technologies used 
python language, Flask framework
MongoFrames a mongodb ODM
In the command line enter the following command from the app directory to run it  flask run

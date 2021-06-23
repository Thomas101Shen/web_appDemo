# The Purpose of this Repo...

is to to provide a demo of my programming capeabilities and display my understanding of handling http requests. The user is shown a contact form where they may input their name, email address, and whatever message they want. The web application will send the data to Cancel changesthe backend and send two emails-one to the owner of the website with the data given by the user, and the other to the user as a confirmation.

## Configuring files and setting up resources

Check the api folder and configure the app.py to your liking. Put in whatever email username you wish to use as the owner of the website, the password relating to that email, and your email provider's smtp server. You will usually find it via search engine. Usually the smtp server is: smtp.domain.tld.

>**If you are using Gmail** you may have to **enable less secure apps** [by following this guide](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account%2Cif-less-secure-app-access-is-on-for-your-account
)
## Next steps...

Make sure you have two clis/terminals open. In the first one, run the following: `npm install && npm start`.
A tab should open up in your default browser, and the url should be "localhost:3000". If not, then paste the url into your browser.

In the second terminal, navigate into the api directory and run the following:

`pip3 install -r requirements.txt && source bin/activate && flask run`

if the app doesn't start then run the following:

`python pi.py`

## Finally
Provide input into the given form fields at localhost:3000 as they are labeled and check your email inbox to see the email. For the "owner's" email address the email should have the client's name as the header and message and email address as the body. In the inbox of the email that was provided in the form field, the "client's" email, there should be an email with the header: Name and a little welcome message as the body.

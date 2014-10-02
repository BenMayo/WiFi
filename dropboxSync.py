# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = '7517gs092fguv7a'
app_secret = '62kmsca91v1vysx'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("sWGaE94VjT8AAAAAAAAe-vQl2zBISY1XPZKDA76yscSNUQexfmNJWH0nPCJQ_GQe").strip()

access_token, user_id = flow.finish(code)

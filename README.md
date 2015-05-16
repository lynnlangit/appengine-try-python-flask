## TKP Virtual Proctor Update on GAE w/Python

## Run Locally
 Run this project locally from the command line:
   ```
   dev_appserver.py .
   ```
  See the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
 Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
 [Deploy the application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
  Your application is now live at your-app-id.appspot.com

### Relational Databases and Datastore
To add persistence to your models, use [NDB](https://developers.google.com/appengine/docs/python/ndb/) for
scale.  Consider [CloudSQL](https://developers.google.com/appengine/docs/python/cloud-sql)
if you need a relational database.

### Installing Libraries
See the [Third party libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK libraries, add them in your app.yaml file. Other than libraries included in the SDK, only pure python libraries may be added to an App Engine project.



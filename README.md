# Hakura Cloud
Django / Python programming project, basically a Twitter clone.

Incorporates Microsoft authentication (Microsoft accounts and Azure AD accounts). This will require an Enterprise Application and App Registration on your Azure AD tenant if you want build this project yourself.

# Dependencies
This project has been built on the following
- [Django](https://www.djangoproject.com/) (built on 4.0.4)
- [django_microsoft_auth](https://github.com/AngellusMortis/django_microsoft_auth) (built on 2.4.1)
- [mssql-django](https://github.com/microsoft/mssql-django) (built on 1.1.3)

# Azure Infrastructure
- [Azure Database for MySQL flexible server](https://docs.microsoft.com/en-us/azure/mysql/flexible-server/)
    - _Costs around 10 USD per month._
- [Azure App Service Plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans)
  - _B1 tier (100 total ACU, 1.75GB memory)_
  - _Costs around 13 USD per month._
# Application Settings
- HAKURA_SERVER_SECRET_KEY
  - _Secret Key for your Django application_
- HAKURA_DB_URL
  - _URI of your Azure MySQL instance_
- HAKURA_DB_USERNAME
  - _Username for your Azure MySQL instance_
- HAKURA_DB_PASSWORD
  - _Password for your Azure MySQL instance_
- MICROSOFT_AUTH_CLIENT_ID
  - _Client ID of your enterprise application_
- MICROSOFT_AUTH_CLIENT_SECRET
  - _Client secret of your Azure enterprise application, this can be obtained in App Registrations._
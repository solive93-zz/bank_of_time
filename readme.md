# Banc del Temps (bank of time)

This is a sigle-sprint project done during *Factoria F5* Full Stack Web Dev Bootcamp.

### What's a Bank of Time?
as stated in their own website:
> A Bank of Time is an economic and social alternative
> to traditional currencies.
> In a Bank of Time abilities are exchanged among members without using money;
> the hours of service (offered and consumed) are counted. You pay with time.

Disclaimer: the original text was in Catalan, so the translation may not be accurate enough, but you get the point.


### What's my approach?
Banks of Time run physically and so it does 'time exchange'. You must go to a specific place to 'register' and get your 1h tickets to use in services.
I love the idea, but the System looks prehistoric to me.

That's why I wanted to modernize their system by:
1. Making a web app in which you can register/login, be aware of services you can 'purchase' with hours around you, upload your services, keep your profile updates (since I believe human factor is capital in this project), see the ratings of the services you wish to consume and rate the ones you consumed.
2. Improve their current website UX and UI.
3. Make a simple mobile app to make 'hour exchange' way easier than is now. Like verse or any other fintech app out there: you just send 1 hour of your time when you 'buy' a service, or recieve it in your account when you offer the service. As simple as that.


### The Stack
I used Python with Flask microframework to build a RESTful API, MySQL database and vueJS in the frontend

#### API endpoints
Services resource
* GET /api/services
* GET /api/services/{service_id}
* POST /api/services
* PATCH /api/services/{service_id}
* DELETE /api/services/{service_id}

Users resource
* GET /api/users
* GET /api/users/{user_id}
* POST /api/users
* PATCH /api/users/{user_id}
* DELETE /api/users/{user_id}

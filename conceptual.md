### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Syntaxically different (Python has an emphasis on indentation where as Javascript has an emphasis on c-type syntax with curly braces to define code blocks.)
  Python is not used in web browsers directly, but used for server sided applications for web apps and apis.
  Javascript is used in web development directly.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  Using dict.get(k, d), with a specified default value or None

  Try-Except block, catching the 'KeyError' that would occur with the missing key.

- What is a unit test?
  Unit tests are to ensure that the individual components work correctly and continue to work as changes have been made.

- What is an integration test?
  Integration tests are used to test interactions between multiple components within your application. Ensures that components such as routes, databases, etc work properly.

- What is the role of web application framework, like Flask?
  Web application frameworks such as Flask simplifies the process of creating web applications. Providing a wide array of tools such as libraries which allow developers to focus on the development process. Benefits such as security, scalability, testing and debugging can all be promoted by utilizing a web application framework.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Route URL - readable URL for users to follow
  important for when the parameter is important for the resource being accessed.

  Query Parameter - Flexible to include optional parameters without changing route structure.
  Can be used for more complex queries without cluttering the URL path.

- How do you collect data from a URL placeholder parameter using Flask?
  Flask will match the URL to the route pattern and pass on values to their respective arguments defined in the functions.

- How do you collect data from the query string using Flask?
  Flask will parse the query string and utilize the 'request' object. Separated parameter values will be evaluated via their respective parameters.

- How do you collect data from the body of the request using Flask?
  Using the 'request' object allows for access to data sent by the client.
  HTTP requests such as POST and PUT handle the data provided.

- What is a cookie and what kinds of things are they commonly used for?
  Cookies is data sent by a web server to the user's web browser which is then stored locally. Cookies are used for session management in web apps and allows for web apps to remember user-classified information and preferences.

- What is the session object in Flask?
  'Session' object is a a component which allows the web application to store and manage user-specified session information regarding multiple HTTP requests. A way to maintain the state of the session and remember specified information about the user as they use the web application. Used for user authentication and maintaining user-made decisions on the application.

- What does Flask's `jsonify()` do?
  A tool used to convert Python data structures (ie. dictionaries, lists, etc) into JSON (Javascript Object Notation) format. JSON is lightweight data interchangable format that is used for communicating data between a server and a client.
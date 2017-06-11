Client

This is the client of the application. It is responsible for closing and
opening the blind. The application is made up of two parts, the rest API
(this gives the information about the state and updates the state of the
blind), and constantly running program that updates the server API every
10 min with the state of the blind.

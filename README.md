# python-arlocameralib
A python library for retrieving images from an arlo camera (often battery operated, currently provided by a router company)

This will become a library--but currently it is a very hacky tool to get an image every ten minutes (you could use this for a time lapse....)

Please note, the arlo camera is battery operated--I'm not sure how much battery reducing power this will have...

Requires "keyring"

sudo pip install keyring

then

keyring set arlo username
and set your email address

then
keyring set arlo password
and set your arlo password

then execute the app.....


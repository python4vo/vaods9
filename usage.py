# This example shows the basic usage of the vaods9 module

# first of all, let's import the vaods9 module.

import vaods9

# let's get an instance of a new ds9 client (if an hub is not running, a new one is started).

client = vaods9.Client()

# launch ds9 now: it should automatically connect to the running hub.
# While testing the module, you might want to run a graphical
# SAMP hub monitor like the one shipped with Topcat, just to be sure ds9 is connected to the hub.

# let's send a fits image to ds9. You can send both relative or absolute paths to a local file, or a URL to a 
# remote file. Please be sure that ds9 can read the URL (e.g. ds9 doesn't support https)

client.send_fits_image('an_image', 'WFPC2u5780205r_c0fx.fits')
# The first argument is an arbitrary string defining an ID. I actually think ds9 ignores it.

# Now, let's send some 'set' commands to ds9. The vaods9 module allows you to use the ds9 set syntax
# described at: http://hea-www.harvard.edu/RD/ds9/ref/samp.html

# change the color map
client.set('cmap Heat')

# zoom to fit the image panel
client.set('zoom to fit')

# change scale to zscale
client.set('scale zscale')

# draw contours
client.set('contour yes')

# save contours to file
client.set('contour save ds9.con wcs fk5')

# To retrieve information from ds9 you have three options.

# The first one is the most simple, but the least flexible. You can use this method inside python scripts, when you need the script to
# wait for the DS9 response.
# The get_now function, in fact, let you call DS9 synchronously: the program waits for DS9
# to respond (at least unless a timeout occurs) and the response is returned to the program directly.
# For example:
contour_scale = client.get_now('contour scale')
print contour_scale

# The default timeout is 1000 ms, but you can define a different timeout:
contour_scale = client.get_now('contour scale', timeout=500)

# A 'basic' get call allows to asynchronously retrieve a value from ds9. This can be useful during interactive sessions, in that it doesn't
# block the python console. You can perform other operations while waiting for a response from DS9, and then retrieve the response:
client.basic_get('contour scale')

# The value is stored in the client.last_response value 
print client.last_response

# Under the hood, the vaods9 module is handling the SAMP message reply and it is storing it in the
# last_response variable.

# These two methods might be enough for basic usage.

# However, with a slightly more advanced approach, you might write your own handler function, that will be called by the module
# in the background, as soon as an answer is received from ds9 (i.e. asynchronously).
# All that you have to do is to define a function that takes just one argument, like the following:

def echo(ds9_response):
   print ds9_response

# Be sure to exit from the function definition and get the python prompt before continuing 

# Now, we will make a 'full' get call to ds9. This time, we will tell python that we want the echo
# function to handle the ds9 response automatically.

client.get('contour scale', echo) # notice that we need just the function name, without quotes.

# you should see the ds9 output echoed on your screen.

# before closing the session let's do some cleanup. The client will disconnect
# from any running hub. If we started a new hub, it will be closed. If you forget to "cleanup"
# the interactive python session will hang and won't let you return you to the shell prompt.

client.cleanup()

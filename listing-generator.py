#### README.md Generator ################
# Usage "python listing-generator.py"
# Output is a markdown formated README.MD
#########################################   

import glob
import sys

# redirect standard out to README.md
# per - http://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python

orig_stdout = sys.stdout
f = file('README.md', 'w')
sys.stdout = f

# Create README.md

print "###OpenChimp"
print ""
print "Photographers Tool Kit - http://www.openchimp.org"
print ""
print "Created by Ashley McNamara - http://www.ashleymcnamara.com"
print ""
print "Follow OpenChimp On Twitter - http://www.twitter.com/openchimp"
print ""
print "Follow OpenChimp On Facebook - http://www.facebook.com/openchimp1"
print ""
print "###Actions Available with OpenChimp"
print ""

#note two spaces are added after each listing so Github Markdown will 
# issue a newline

for atn in glob.iglob("*/*.atn"): # List the Actions
    print atn, '  '

print ""
print "###LightRoom Presets available with OpenChimp"
print ""    

for lrtemplate in glob.iglob("*/*.lrtemplate"): # List the Presets 
    print lrtemplate, '  '
    
print ""
print "###Templates available with OpenChimp"
print ""

for templates in glob.iglob("*/*.psd"): # List the Templates 
    print templates, '  '

# Return stdout back to normal
sys.stdout = orig_stdout
f.close()

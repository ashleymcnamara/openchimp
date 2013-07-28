#### README.md Generator ################
# Usage "python listing-generator.py"
# questions please contat colin@2cups.com
#########################################    

import glob
print "### OpenChimp"
print ""
print "Photographers Tool Kit - http://www.openchimp.org"
print ""
print "Created by Ashley McNamara - http://www.ashleymcnamara.com"
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

markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""

markup = markup.format('My Page Title', 'Page Heading')

print (markup)

'''
    <body>
        <h1>{heading}</h1>
    </body>

markup2 = markup.format(heading = "heading2")
print (markup2)

'''
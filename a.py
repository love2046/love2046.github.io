import markdown2
text='''
#this is header
##sub title
hello world
test
'''
html=markdown2.markdown(text)
print(html)
with open("index.html","w") as f:
    f.write(html)



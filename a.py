import markdown2
text='''
#this is header
##sub title

hello world

* test1
* test2
* test2
'''
html=markdown2.markdown(text)
print(html)
with open("index.html","w") as f:
    f.write(html)



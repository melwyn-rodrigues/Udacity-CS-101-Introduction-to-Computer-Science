# Print all links that appear in the string titled 'page'

page=('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://stanford.com"><a href="http://udacity.com">')
def get_next_target(page):
    start_link = page.find('<a href=')
    #print (start_link)
    if start_link==-1:
        return  None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(page):
    while  True :
        url,end_pos=get_next_target(page)   #url from get_next_target gets assigned to url in this line,
                                            #and end-quote gets assigned to end_pos
        if url:
            print (url)             #this line is run, if url exists
            page=page[end_pos:]     #this line is run, if url exists    
        else:
            break                   #this line is run, if url does not exist
print (print_all_links(page))
        
#while True means loop forever. The while statement takes an expression and executes the loop body
#while the expression evaluates to (boolean) "true". True always evaluates to boolean "true" and
#thus executes the loop body indefinitely. It's an idiom that you'll just get used to eventually!
#Most languages you're likely to encounter have equivalent idioms.
#Note that most languages usually have some mechanism for breaking out of the loop early.
#In the case of Python it's the break statement 

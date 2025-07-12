# Imports necessary class and Pillow library.

from PIL import Image, ImageDraw, ImageFont
from Main.models import PriceList

'''devnotes

# Categorization [success thanks to objects.all(type="domates")] [Success]
# 1st Part: Listing the objects giving it to Jinja [Success]
# 2nd Part: Taking the objects [Success]
# 3rd Part: Image Creation [Success]
# 4th Part: Saving the Queries [Success]

'''

class ImageCreation():
    # Firstly, we create the necessary variables to handle images with pillow library.

    # Global font
    font = ImageFont.truetype("Main/static/pillow/font.ttf", 18)
    # Numeric Operations Visualization
    up_arr = Image.open("Main/static/pillow/up.png").convert("RGBA") 
    down_arr = Image.open("Main/static/pillow/down.png").convert("RGBA")
    eq_arr = Image.open("Main/static/pillow/eq.png").convert("RGBA")
        
    ### The core method of the class. Its' function is with taking "baslik","dict" arguments, 
    ### handling the dict and 'baslik' string and drawing this datas to target image.

    def CreateImage(baslik,dict):
        # We basically opening the image in method, that's because we need to refresh the state of image everytime we call. And preventing overdraw.
        img= Image.open("Main/static/pillow/main_schema.png").convert("RGBA")
        draw = ImageDraw.Draw(img)

        # From dictionary, we load the specfic lists which seperated by types.
        biber_prices = dict['biber']
        domates_prices = dict['domates']
        salatalik_prices = dict['salatalik']
        patlican_prices = dict['patlican']
        kabak_prices = dict['kabak']
        ### IN THIS SEQUENCE WE NEED AN SPECIFIC OBJECT, BECAUSE THIS IS AN EXCEPTION. SO we use filter method.
        salkim_max_price = PriceList.filter(dict,'domates-salkim-max')
        
        # Font refresh (optional)
        font = ImageFont.truetype("Main/static/pillow/font.ttf", 18)

        # The method that easily gets the data from the lists and drawing this data as text between desired spaces.
        def draw_table(start_x,start_y,desired_list,color,font,is_yesterday,line=0,lineadder=31,prefix="",suffix=" TL",skip_index=None,ex_args=None,ex_blank=None,font_size=None):
            for selected_object in desired_list:
                if selected_object.yesterday_price == 0 and selected_object.today_price == 0:
                    line+=lineadder
                    continue
                # Exception Handling
                if desired_list.index(selected_object) == skip_index:
                    continue
                # Numeric Operation Handling and Price Status Check
                if is_yesterday == True:
                    content = f"{selected_object.yesterday_price}"
                else:                    
                    content = f"{selected_object.today_price}"
                if ex_args != None:
                    if selected_object.name == ex_args:
                        draw.text((start_x-ex_blank, start_y+line), prefix+content+suffix, fill=color, font=ImageFont.truetype("Main/static/pillow/font.ttf", font_size),anchor='rt')
                    else:
                        draw.text((start_x, start_y+line), prefix+content+suffix, fill=color, font=font,anchor='rt')
                else:
                    draw.text((start_x, start_y+line), prefix+content+suffix, fill=color, font=font,anchor='rt')
                item_index = desired_list.index(selected_object)
                if is_yesterday==True and ex_args != "no_arrow":
                    if selected_object.yesterday_price<selected_object.today_price:
                        img.paste(ImageCreation.up_arr,(start_x+18,start_y+line-4), ImageCreation.up_arr)
                    elif selected_object.yesterday_price>selected_object.today_price:
                        img.paste(ImageCreation.down_arr,(start_x+18,start_y+line-4), ImageCreation.down_arr)
                    else:
                        img.paste(ImageCreation.eq_arr,(start_x+18,start_y+line-7), ImageCreation.eq_arr)
                line+=lineadder
            return
       
        # Drawing old values
        draw_table(354,253,biber_prices,(50, 141, 168),font,is_yesterday=True)
        draw_table(854,253,domates_prices,(50, 141, 168),font,is_yesterday=True,skip_index=2,ex_args='domates-salkim',ex_blank=55,font_size=18)
        draw_table(854,423,salatalik_prices,(50, 141, 168),font,is_yesterday=True)
        draw_table(854,528,patlican_prices,(50, 141, 168),font,is_yesterday=True)
        draw_table(854,606,kabak_prices,(50, 141, 168),font,is_yesterday=True)
        draw_table(870,284,salkim_max_price,(50, 141, 168),font,is_yesterday=True, prefix="- ", ex_args="no_arrow")

        # Drawing Today values and arrows
        draw_table(464,253,biber_prices,(0, 0, 0),font,is_yesterday=False)
        draw_table(964,253,domates_prices,(0, 0, 0),font,is_yesterday=False, skip_index=2, ex_args='domates-salkim',ex_blank=24,font_size=15)
        draw_table(964,423,salatalik_prices,(0, 0, 0),font,is_yesterday=False)
        draw_table(964,528,patlican_prices,(0, 0, 0),font,is_yesterday=False)
        draw_table(964,606,kabak_prices,(0, 0, 0),font,is_yesterday=False)
        draw_table(1000,284,salkim_max_price,(0, 0, 0),ImageFont.truetype("Main/static/pillow/font.ttf", 15),is_yesterday=False,prefix="- ")

        # Drawing title
        font = ImageFont.truetype("Main/static/pillow/font.ttf", 58)
        draw.text((500,45), baslik, fill=(255, 255, 255), font=font,anchor='mm')
        
        # Saving the static folder.
        img.save('Main/static/yazili_resim.png')

        return # returns none.




    
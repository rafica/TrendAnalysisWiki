import os, fileinput

class wiki_pop:
     def __init__(self):
          
          
          self.forbid = ["Media", "Special", "Talk", "User", "User_talk", "Project", "Project_talk", "File", "File_talk", "MediaWiki"]
          self.extension = [".gif",".jpg",".txt",".png",".GIF",".JPG",".PNG",".ico"]
          self.boilerplate = ["404_Error", "Main_Page", "Hypertext_Transfer_Protocol", "Favicon.ico", "Search"]
          
     def mapper(self):
         
          #Mapper function for preprocessing
          #fileName = os.environ['map_input_file']
          fileName = "pagecounts-20131101-000003"
          filenamelist = fileName.split("-")
          date = filenamelist[1]
          for line in fileinput.input():
             
               flag=1
               list_obj = line.split()

               #Boilerplate check
               if list_obj[1] in self.boilerplate:
                continue

               #Filtering only english wikipedia articles
               if list_obj[0]=="en":

                #Talk related pages should be excluded
                for word in self.forbid:
                     
                     matchgroup = list_obj[1].find(word)
                     if matchgroup==0:
                          
                          flag=0
                          break
                if flag==0:
                     
                     continue

                #Articles name should start with lowercase letter
                if not list_obj[1][0].islower():
                     
                     if len(list_obj[1])>4:
                          ext = list_obj[1][-4:]

                        #Files such as images or any other files should not be taken
                          if ext not in self.extension:
                               
                              
                              

                                 #Replace %22 with underscore
                               list_obj[1].replace("%22", "_")

                                 #Output format
                               print "%s}%s %s" % (list_obj[1], date, list_obj[2])
                    
           
if __name__ == "__main__":
    wp_obj = wiki_pop()
    wp_obj.mapper() 
                

        
        

#!/usr/bin/python
import os,sys
import logging

class wiki_pop:
     def __init__(self):
          
          self.logger_file = "wiki_log_mapper1.txt"
          self.forbid = set(("Media", "Special", "Talk", "User", "User_talk", "Project", "Project_talk", "File", "File_talk", "MediaWiki"))
          self.extension = set((".gif",".jpg",".txt",".png",".GIF",".JPG",".PNG",".ico"))
          self.boilerplate = set(("404_Error", "Main_Page", "Hypertext_Transfer_Protocol", "Favicon.ico", "Search"))

     def initialize_logger(self):
          
         logging.basicConfig(filename=self.logger_file, level=logging.INFO)
         logging.info("Initialized logger")
         
     def mapper(self):
          #self.initialize_logger()
         
          #Mapper function for preprocessing
          fileName = os.environ['map_input_file']
          filenamelist = fileName.split("-")
          date = filenamelist[1]
          for line in sys.stdin:
               try:
                    if not line:
                         #logging.info("line was empty")
                         continue
                    
                    flag=1
                    list_obj = line.split()
                    if len(list_obj)!=4:
                         #logging.info("4 components not present")
                         continue
                         
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
                                    print "%s %s %s" % (list_obj[1], date, list_obj[2])
                                    
               except:
                    #e = sys.exc_info()[0]
                    #logging.info(e)
                    continue
                    

                    
           
if __name__ == "__main__":
    wp_obj = wiki_pop()
    wp_obj.mapper() 
                

        
        

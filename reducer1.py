#!/usr/bin/env python

from operator import itemgetter
import sys, logging

class wiki_pop_reduce1:
    def __init__(self):
        self.logger_file = "wiki_log_reducer1.txt"
        self.prev_name = None
        self.prev_views = 0
        self.prev_date = None
        self.prev_views_list = []
        self.prev_date_list = []
        self.prev_total = 0
        self.latest = 0
        self.earliest = 0
        

    def initialize_logger(self):
         logging.basicConfig(filename=self.logger_file, level=logging.INFO)
         logging.info("Initialized logger")
         
    def reducer(self):
        #self.initialize_logger()
        name = None
        date = None
        views= None
        ef =0
        lf =0

        # input comes from STDIN
        for line in sys.stdin:
        
            if not line:
                #logging.info("line empty")
                continue
            if len(line.split())!=3:
                #logging.info("3 components expected, not found")
                continue
            
            # parse the input we got from mapper.py
            name, date, views = line.split()
            day = date[-2:]
            try:
                views = int(views)
            except ValueError:
                continue
            #print self.prev_name, self.prev_date_list
            if self.prev_name == name and self.prev_date== date:
                #print "yes"
                self.prev_views = self.prev_views + views
                self.prev_total = self.prev_total + views

            elif self.prev_name==name and self.prev_date!= date:
                #print "yes2"
                self.prev_date_list.append(date)
                self.prev_views_list.append(self.prev_views)
                self.prev_total = self.prev_total + views
                if lf:
                    self.latest = self.latest + self.prev_views 
                else:
                    self.earliest = self.earliest + self.prev_views
                if int(day)>=8:
                    lf = 1
                    ef =0
                else:
                    ef = 1
                    lf = 0

                self.prev_views = views
                self.prev_date = date
                #print self.prev_date_list

                
            else:
                
                if self.prev_name:
                    #self.prev_views = self.prev_views + views
                    if self.prev_total<10:

                        self.prev_name = name
                        self.prev_date = date
                        self.prev_views = views
                        self.prev_views_list = []
                        self.prev_total = views
                        self.prev_date_list = [date]
                        self.latest = 0
                        self.earliest = 0
                        if int(day)>=8:
                            lf = 1
                            ef =0
                        else:
                            ef = 1
                            lf = 0
                        continue
                    #print self.earliest
                    self.prev_views_list.append(self.prev_views)
                    if ef:
                        self.earliest =self.earliest + self.prev_views
                    else:
                        self.latest= self.latest + self.prev_views
     
                    print "%s %s %s %s %s" % (self.prev_name, self.prev_date_list, self.prev_views_list, self.prev_total, self.latest-self.earliest)
                #print "else"
                self.prev_name = name
                self.prev_date = date
                self.prev_views = views
                self.prev_views_list = []
                self.prev_total = views
                self.prev_date_list = [date]
                self.latest = 0
                self.earliest = 0
                if int(day)>=8:
                    lf = 1
                    ef =0
                else:
                    ef = 1
                    lf = 0


        if self.prev_name == name and self.prev_date== date and self.prev_total>=10:
            self.prev_views_list.append(self.prev_views)
            if ef:
                self.earliest =self.earliest + self.prev_views
            else:
                self.latest= self.latest + self.prev_views
            print "%s %s %s %s %s" % (self.prev_name, self.prev_date_list, self.prev_views_list, self.prev_total,self.latest-self.earliest)

        
        


if __name__== "__main__":
    wp_obj = wiki_pop_reduce1()
    wp_obj.reducer()
   

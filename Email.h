//
//  Email.h
//  Spam2
//
//  Created by Konstantin Dmitriev on 11/11/14.
//  Copyright (c) 2014 Dmitriev. All rights reserved.
//

#ifndef __Spam2__Email__
#define __Spam2__Email__

#include <stdio.h>
#include <string>
#include <vector>

class Email
{
private:
    int emailID; //email ID (first two numbers in the sample data files
    bool spamMarker; //spam marker
    
    //vectors of all the words in the email and their frequencies
    std::vector<std::string> *words;
    std::vector<int> *frequencies;
public:
    //constructor
    Email(); //not sure yet what exactly to put here
    
    //Test files contain a string of the data for a particular email
    //this method creates an email, using a string that could be obtain after parsing
    //the test file
    void createEmailFromStringInDataSample(std::string &str);
    
    void setEmailID(int id);
    int getEmailID();
    
    void setSpamMarker(bool m);
    bool getSpamMarker();
    
    void setWords(std::vector<std::string> *w);
    std::vector<std::string> *getWords();
    
    void setFrequencies(std::vector<int> *f);
    std::vector<int> *getFrequencies();
    
    //mostly for debugging purposes
    //prints all of the available information about the email
    void print();
    
};

#endif /* defined(__Spam2__Email__) */

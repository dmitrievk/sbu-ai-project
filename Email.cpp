//
//  Email.cpp
//  Spam2
//
//  Created by Konstantin Dmitriev on 11/11/14.
//  Copyright (c) 2014 Dmitriev. All rights reserved.
//

#include "Email.h"
#include <iostream>

using namespace std;

void Email::createEmailFromStringInDataSample(std::string &str)
{
    
}

void Email::setEmailID(int id)
{
    emailID = id;
}
int Email::getEmailID()
{
    return emailID;
}

void Email::setSpamMarker(bool m)
{
    spamMarker = m;
}

bool Email::getSpamMarker()
{
    return spamMarker;
}

void Email::setWords(std::vector<std::string> *w)
{
    words = w;
}
std::vector<std::string> * Email::getWords()
{
    return words;
}

void Email::setFrequencies(std::vector<int> *f)
{
    frequencies = f;
}
std::vector<int> * Email::getFrequencies()
{
    return frequencies;
}

void Email::print()
{
    for (auto c : *words)
    {
        auto it = std::find(words->begin(), words->end(), c);
        auto index = std::distance(words->begin(), it);
        std::cout << "Word: " << c << "; Frequency: " << frequencies->at(index) << std::endl;
    }
    
}

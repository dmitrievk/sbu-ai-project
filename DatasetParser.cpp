//
//  DatasetParser.cpp
//  Spam2
//
//  Created by Konstantin Dmitriev on 11/11/14.
//  Copyright (c) 2014 Dmitriev. All rights reserved.
//

#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include "Email.h"

//Functions for parsing the sample dataset
//creates a vector of Emails
std::vector<Email> * parseFile(std::string *path)
{
    std::vector<Email> emails;
    std::ifstream fin;
    fin.open(*path); // open a file
    if (!fin.good())
        std::cout << "File is not found"; // exit if file not found
    
    // read each line of the file
    while (!fin.eof())
    {
//        // read an entire line into memory
//        char buf[MAX_CHARS_PER_LINE];
//        fin.getline(buf, MAX_CHARS_PER_LINE);
//        
//        // parse the line into blank-delimited tokens
//        int n = 0; // a for-loop index
//        
//        // array to store memory addresses of the tokens in buf
//        const char* token[MAX_TOKENS_PER_LINE] = {}; // initialize to 0
//        
//        // parse the line
//        token[0] = strtok(buf, DELIMITER); // first token
//        if (token[0]) // zero if line is blank
//        {
//            for (n = 1; n < MAX_TOKENS_PER_LINE; n++)
//            {
//                token[n] = strtok(0, DELIMITER); // subsequent tokens
//                if (!token[n]) break; // no more tokens
//            }
//        }
//        
//        // process (print) the tokens
//        for (int i = 0; i < n; i++) // n = #of tokens
//            cout << "Token[" << i << "] = " << token[i] << endl;
//        cout << endl;
    }
    return &emails;
}


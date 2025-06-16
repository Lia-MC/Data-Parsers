#include <iostream>

int loadfile(filename) {
    // load text file
    ifstream f(filename); // ifstream f("samplevals.txt");

    // check if file opened successfully
    if (!f.is_open()) {
        cerr << "Error opening the file!";
        return 1;
    }
    
    string s;

    // read each line of the file, 
    // store it in string s
    while (getline(f, s + len(alr_added))) { // some way to put the values without commas or arrays and stuff would be really nice... HOW ABOUT NODES!!!
        // put some of it into the x value text
        // skip over the space
        // add a comma before the number if not the first iteration through the while loop + put the rest of it into the y value file
    }

    // Close the file
    f.close();

    // while char isnt null
    // read in first num, ignore second and third, read in fourth num
    // repeat for each row until char is null then exit loop
    // display the two columns (each time just add word1 word2 newline for each row u read in)
    return 0;
}

int main() {
    // i need to make sure that i can access string s, maybe i malloc it here, then pass it into load file

    string filename = "samplesvals.txt";

    while (loadfile() != 0) {
        filename = ; // get user input
    }

    cout << "ran";
}
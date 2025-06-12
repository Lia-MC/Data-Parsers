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
    while (getline(f, s)) {
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

    while (loadfile() != 0) {
        filename = ; // get user input
    }

    cout << "ran";
}
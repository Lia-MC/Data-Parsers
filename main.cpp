#include <iostream>

int main() {
    // load text file
    ifstream f("samplevals.txt");

    // check if file opened successfully
    if (!f.is_open()) {
        cerr << "Error opening the file!";
        return 1;
    }
    string s;

    // read each line of the file, 
    // store it in string s and print it to the standard output stream 
    while (getline(f, s))
        cout << s << endl;

    // Close the file
    f.close();
    return 0;

    // while char isnt null
    // read in first num, ignore second and third, read in fourth num
    // repeat for each row until char is null then exit loop
    // display the two columns (each time just add word1 word2 newline for each row u read in)
    cout << "ran";
    return 0;
}
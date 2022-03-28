#include <stdio.h>


double find_ic(char* txt, char* alphabet, int* counters) {
    int txt_length = 0;
    for (int i = 0; *(txt + i); i++) {
        for (int j = 0;  j < 26; j++) {
            if (*(txt + i) == *(alphabet + j)) {
                *(counters + j) += 1;
                txt_length++;
                break;
            }
        }
    }
    double ic = 0;
    for (int i = 0; i < 26; i++) {
        ic += ((double)counters[i] / txt_length) * ((double)(counters[i] - 1) / ( txt_length - 1)); 
    }
    return ic;
}


int main() {
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    int counters[26] = {0};
    char txt[] = "The most beautiful things in the world cannot be seen or touched, they are felt with the heart.";
    double ic = find_ic(txt, alphabet, counters);
    printf("The index of coincidence for the text is: %lg\n", ic);
    return 0;
}

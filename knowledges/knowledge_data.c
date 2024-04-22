// ID,Name,Score
// 1,Alice,85
// 2,Bob,92
// 3,Charlie,78

#include <stddef.h>

typedef struct {
    int id;
    char name[10];
    int score;
} Person;

Person data[] = {
    {1, "Alice", 85},
    {2, "Bob", 92},
    {3, "Charlie", 78}
};

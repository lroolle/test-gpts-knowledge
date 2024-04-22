// ID,Name,Score
// 1,Alice,85
// 2,Bob,92
// 3,Charlie,78

export interface Student {
    id: number;
    name: string;
    score: number;
}

export const data: Student[] = [
    { id: 1, name: "Alice", score: 85 },
    { id: 2, name: "Bob", score: 92 },
    { id: 3, name: "Charlie", score: 78 },
];

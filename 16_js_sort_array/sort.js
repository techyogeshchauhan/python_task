function sortDescending(arr) {
    return [...arr].sort((a, b) => b - a);
}

// Example usage
const numbers = [5, 2, 9, 1, 7];
const sortedNumbers = sortDescending(numbers);

console.log('Original array:', numbers);
console.log('Sorted array (descending):', sortedNumbers); 
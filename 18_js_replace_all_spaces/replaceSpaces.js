/**
 * Replaces all spaces in a string with dashes
 * @param {string} str - The input string
 * @returns {string} The string with spaces replaced by dashes
 */
function replaceSpacesWithDashes(str) {
    return str.replace(/\s+/g, '-');
}

// Example usage
const example1 = "Hello World";
const example2 = "This is a test string";
const example3 = "Multiple   spaces   here";

console.log(replaceSpacesWithDashes(example1)); // Output: "Hello-World"
console.log(replaceSpacesWithDashes(example2)); // Output: "This-is-a-test-string"
console.log(replaceSpacesWithDashes(example3)); // Output: "Multiple-spaces-here" 
const fs = require('fs');

try {
    const hello = require('./build/Release/hello');
    document.getElementById('output').innerHTML = `
        <h2>${hello.sayHello()}</h2>
        <p>C++ addon is working!</p>
    `;
} catch (err) {
    document.getElementById('output').innerHTML = `
        <h2>Error loading C++ addon:</h2>
        <p>${err.message}</p>
    `;
}
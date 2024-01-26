// app.js

// Fetch your JSON data (replace 'your-json-file.json' with your actual file path or API endpoint)
d3.json('examples/TensorBoard/dataset_test.json').then(data => {
    // Your code to process and visualize the JSON data using D3.js
    // For a simple example, you can log the data to the console
    console.log(data);
});

//Fetch your JSON data(replace 'your-json-file.json' with your actual file path or API endpoint)
d3.json('examples/TensorBoard/dataset_test.json').then(data => {
    // Check if data is loaded correctly
    console.log(data);

    // Assuming data is an array of objects with x and y properties
    const svg = d3.select("#json-track-graph").append("svg").attr("width", 400).attr("height", 200);
    const circles = svg.selectAll("circle").data(data.topping).enter().append("circle");

    circles
        .attr("cx", (d, i) => i * 50 + 25)
        .attr("cy", 100)
        .attr("r", 20)
        .style("fill", "blue");
});


// // Mocking the data since we can't fetch external files in this environment
// const data = {
//     "topping": [
//         { "id": "5001", "type": "None" },
//         { "id": "5002", "type": "Glazed" },
//         { "id": "5005", "type": "Sugar" },
//         { "id": "5007", "type": "Powdered Sugar" },
//         { "id": "5006", "type": "Chocolate with Sprinkles" },
//         { "id": "5003", "type": "Chocolate" },
//         { "id": "5004", "type": "Maple" }
//     ]
// };

// // Check if data is loaded correctly
// console.log(data);

// // Assuming data is an array of objects with id and type properties
// const svg = d3.select("#json-track-graph").append("svg").attr("width", 400).attr("height", 200);
// const circles = svg.selectAll("circle").data(data.topping).enter().append("circle");

// circles
//     .attr("cx", (d, i) => i * 50 + 25)
//     .attr("cy", 100)
//     .attr("r", 20)
//     .style("fill", "blue");

// // Add text labels to circles
// const labels = svg.selectAll("text").data(data.topping).enter().append("text");

// labels
//     .attr("x", (d, i) => i * 50 + 25)
//     .attr("y", 100)
//     .attr("text-anchor", "middle")
//     .attr("dy", "0.35em")
//     .style("fill", "white")
//     .text(d => d.type);

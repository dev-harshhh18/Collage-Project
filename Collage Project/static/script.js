document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input, index) => {
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                const nextInput = inputs[index + 1];
                if (nextInput) {
                    nextInput.focus();
                }
            }
        });
    });
});

function submitForm() {
    const form = document.getElementById('marksForm');
    const formData = new FormData(form);

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h2>Result</h2>
            <p>Roll Number: ${data.roll}</p>
            <p>Name: ${data.name}</p>
            <p>Physics Marks: ${data.m1}</p>
            <p>Mathematics Marks: ${data.m2}</p>
            <p>Chemistry Marks: ${data.m3}</p>
            <p>Cricket Marks: ${data.sm1}</p>
            <p>Hockey Marks: ${data.sm2}</p>
            <p>Chess Marks: ${data.sm3}</p>
            <p>Total Subject Marks: ${data.tot}</p>
            <p>Subject Percentage: ${data.per}%</p>
            <p>Total Sports Marks: ${data.stot}</p>
            <p>Sports Percentage: ${data.sper}%</p>
            <p>Sports Grade: ${data.grade}</p>
        `;
    })
    .catch(error => {
        document.getElementById('result').innerHTML = `
            <h2>Error</h2>
            <p>There was an error processing your request. Please try again.</p>
        `;
        console.error('Error:', error);
    });
}

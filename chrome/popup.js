function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message')
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    document.getElementById('responses').appendChild(messageElement);
    document.getElementById('prompt').value = '';
}

async function sendPrompt() {
    const endpointUrl = 'http://localhost:5000/chat';
    const headers = {
        'Content-Type': 'application/json',
    };

    const message = document.getElementById('prompt').value;
    const messageJson = JSON.stringify({prompt: message});
    console.log("Sending: " + messageJson);

    fetch(endpointUrl, {
        method: 'POST',
        headers,
        body: messageJson,
    })
    .then((response) => response.json())
    .then((data) => {
        const gpt_response = data.response;
        appendMessage('User', message);
        appendMessage('GPT', gpt_response);
    })
    .catch((error) => {
        console.log('Error: ' + error);
    });
};

window.onload = function() {
    document.getElementById('send').onclick = sendPrompt;
};

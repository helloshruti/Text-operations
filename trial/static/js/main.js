document.getElementById('summarizer-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const content = document.getElementById('content').value;
    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `content=${encodeURIComponent(content)}`,
    });

    const data = await response.json();
    const summaryTextElement = document.getElementById('summary-text');
    if (data.summary) {
        summaryTextElement.innerText = data.summary;
    } else {
        summaryTextElement.innerText = data.error || 'An error occurred!';
    }
});

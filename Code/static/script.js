document.addEventListener('DOMContentLoaded', () => {
    const sentenceContainer = document.querySelector('.sentence');
    const generateButton = document.getElementById('generate-btn');

    const initialSentence = sentenceContainer.getAttribute('data-sentence');
    sentenceContainer.textContent = initialSentence; // Display the initial sentence

    // Function to fetch a new sentence from app.py
    const fetchNewSentence = async () => {
        try {
            const response = await fetch('/');
            const data = await response.json();
            sentenceContainer.textContent = data.sentence;
        } catch (error) {
            console.error('Error fetching sentence:', error);
        }
    };

    generateButton.addEventListener('click', () => {
        fetchNewSentence();
    });
});



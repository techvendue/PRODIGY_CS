<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caesar Cipher</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Use Inter as the default font */
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 dark:bg-gray-900 flex items-center justify-center min-h-screen p-4">

    <div class="w-full max-w-2xl bg-white dark:bg-gray-800 rounded-2xl shadow-lg p-6 md:p-8">
        
        <!-- Header -->
        <div class="text-center mb-8">
            <h1 class="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white">Caesar Cipher</h1>
            <p class="text-gray-500 dark:text-gray-400 mt-2">Encrypt and decrypt messages with a simple shift.</p>
        </div>

        <!-- Input Form -->
        <div class="space-y-6">
            <!-- Message Input -->
            <div>
                <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Your Message</label>
                <textarea id="message" rows="4" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200" placeholder="Enter the text you want to process..."></textarea>
            </div>

            <!-- Shift Key Input -->
            <div>
                <label for="shift" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Shift Key</label>
                <input type="number" id="shift" value="3" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200" placeholder="Enter a number">
            </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 mt-8">
            <button id="encrypt-btn" class="w-full bg-blue-600 text-white font-semibold py-3 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-800 transition duration-300">
                Encrypt
            </button>
            <button id="decrypt-btn" class="w-full bg-gray-600 text-white font-semibold py-3 px-4 rounded-lg hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-800 transition duration-300">
                Decrypt
            </button>
        </div>

        <!-- Result Display -->
        <div class="mt-8">
            <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Result</h2>
            <div id="result-box" class="mt-2 p-4 w-full h-32 bg-gray-100 dark:bg-gray-700 rounded-lg border border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 overflow-y-auto">
                <p id="result-text" class="whitespace-pre-wrap">Your processed text will appear here...</p>
            </div>
        </div>
    </div>

    <script>
        // --- DOM Element References ---
        const messageInput = document.getElementById('message');
        const shiftInput = document.getElementById('shift');
        const encryptBtn = document.getElementById('encrypt-btn');
        const decryptBtn = document.getElementById('decrypt-btn');
        const resultText = document.getElementById('result-text');
        const resultBox = document.getElementById('result-box');

        /**
         * Core Caesar Cipher logic.
         * Encrypts or decrypts a given text by shifting its letters.
         * @param {string} text - The input string.
         * @param {number} shift - The number of positions to shift letters.
         * @param {string} mode - 'encrypt' or 'decrypt'.
         * @returns {string} The processed string.
         */
        function caesarCipher(text, shift, mode) {
            let result = "";

            // Ensure shift is a positive integer for the modulo operation
            const shiftAmount = parseInt(shift, 10);
            if (isNaN(shiftAmount)) {
                alert('Shift key must be a number.');
                return 'Invalid shift key.';
            }
            
            // For decryption, we shift in the opposite direction
            const finalShift = mode === 'decrypt' ? -shiftAmount : shiftAmount;

            for (let i = 0; i < text.length; i++) {
                let char = text[i];

                if (char.match(/[a-z]/i)) { // Check if it's a letter (case-insensitive)
                    // Get ASCII code
                    const code = text.charCodeAt(i);
                    let start;

                    // Determine the starting point (A or a)
                    if (code >= 65 && code <= 90) { // Uppercase letters
                        start = 65;
                    } else if (code >= 97 && code <= 122) { // Lowercase letters
                        start = 97;
                    }
                    
                    // Calculate the shifted position
                    // The modulo operator in JS can be tricky with negative numbers,
                    // so we add 26 and then take the modulo to ensure it's always positive.
                    let shiftedCode = (code - start + finalShift) % 26;
                    if (shiftedCode < 0) {
                        shiftedCode += 26;
                    }
                    
                    result += String.fromCharCode(start + shiftedCode);

                } else {
                    // If not a letter, keep the character as is
                    result += char;
                }
            }
            return result;
        }

        // --- Event Listeners ---

        // Encrypt button click handler
        encryptBtn.addEventListener('click', () => {
            const message = messageInput.value;
            const shift = shiftInput.value;
            if (!message) {
                resultText.textContent = 'Please enter a message first.';
                return;
            }
            const encryptedText = caesarCipher(message, shift, 'encrypt');
            resultText.textContent = encryptedText;
        });

        // Decrypt button click handler
        decryptBtn.addEventListener('click', () => {
            const message = messageInput.value;
            const shift = shiftInput.value;
            if (!message) {
                resultText.textContent = 'Please enter a message first.';
                return;
            }
            const decryptedText = caesarCipher(message, shift, 'decrypt');
            resultText.textContent = decryptedText;
        });

    </script>
</body>
</html>

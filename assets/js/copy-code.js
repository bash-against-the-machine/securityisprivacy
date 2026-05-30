document.addEventListener('DOMContentLoaded', function() {
  const codeBlocks = document.querySelectorAll('pre.highlight');
  
  codeBlocks.forEach(block => {
    // Create button
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy code to clipboard');
    
    // Position button
    block.style.position = 'relative';
    block.appendChild(button);
    
    // Add click event
    button.addEventListener('click', () => {
      const code = block.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {
        button.textContent = 'Copied!';
        setTimeout(() => button.textContent = 'Copy', 2000);
      });
    });
  });
});   

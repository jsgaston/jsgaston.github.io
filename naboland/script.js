document.addEventListener('DOMContentLoaded', function() {
  
    const form = document.getElementById('messageSubmissionForm');
    const nameInput = document.getElementById('name');
    const messageInput = document.getElementById('message');
    const messagePreview = document.getElementById('messagePreview');
  
    // Live preview of message
    messageInput.addEventListener('keyup', function() {
      messagePreview.textContent = `Preview: ${messageInput.value}`;
    });
  
    // Form submission
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      if (nameInput.value.trim() && messageInput.value.trim()) {
        // Here we would normally send the data to a server
        console.log('Message sent:', nameInput.value, messageInput.value);
        alert('Thank you for your message!');
        // Reset form after submission
        form.reset();
        messagePreview.textContent = '';
      } else {
        alert('Please fill in all fields.');
      }
    });
  });
  
const handlesubmit = (e) => {
    e.preventdefault()
    
} 
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('translateButton');
    button.addEventListener('click', function () {
        alert('Button was clicked!');
        
    });
});

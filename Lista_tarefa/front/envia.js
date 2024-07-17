
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
      event.preventDefault();

      const taskName = document.getElementById('taskName').value;
      const taskDescription = document.getElementById('taskDescription').value;
      const dueDate = document.getElementById('dueDate').value;
      const completionDate = document.getElementById('completionDate').value;

      const formData = {
        taskName: taskName,
        taskDescription: taskDescription,
        dueDate: dueDate,
        completionDate: completionDate
      };

      // Assuming the API endpoint is http://127.0.0.1:8000/api/Lista/
      const apiUrl = 'http://127.0.0.1:8000/api/Lista/';

      fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        // Optionally, you can perform actions after successful submission
      })
      .catch((error) => {
        console.error('Error:', error);
        // Optionally, you can handle errors here
      });
    });
  });
</script>

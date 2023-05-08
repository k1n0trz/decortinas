document.getElementById('mySearchForm');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que el formulario se envíe
  const query = document.querySelector('input[type="search"]').value;
  // Ejecuta la búsqueda con la consulta "query"
  // ...
});
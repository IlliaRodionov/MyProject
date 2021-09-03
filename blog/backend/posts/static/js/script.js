var myModal = document.getElementById('myModal')

myModal.addEventListener('show.bs.modal', function (event) {
  if (!data) {
    return event.preventDefault() // останавливает отображение модального окна
  }
})
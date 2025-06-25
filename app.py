<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple CSS Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 20px;
    }

    h1 {
      color: #333;
      text-align: center;
    }

    p {
      color: #555;
      font-size: 16px;
    }

    .card {
      background-color: white;
      padding: 20px;
      margin: 20px auto;
      max-width: 500px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }

    .button {
      display: inline-block;
      padding: 10px 20px;
      color: white;
      background-color: #007BFF;
      text-decoration: none;
      border-radius: 5px;
      margin-top: 10px;
    }

    .button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <h1>Welcome to My Website</h1>

  <div class="card">
    <p>This is a simple card component styled with CSS.</p>
    <a href="#" class="button">Click Me</a>
  </div>

</body>
</html>

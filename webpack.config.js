const path = require('path');

module.exports = {
  entry: './src/index.js', // Ваш основной файл JavaScript
  output: {
    path: path.resolve(__dirname, 'dist'), // Путь к выходной директории
    filename: 'bundle.js', // Название итогового бандла
  },
  module: {
    rules: [
      // Правила для обработки JavaScript файлов
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader', // Используем babel-loader для обработки JavaScript файлов
          options: {
            presets: ['@babel/preset-env'], // Поддержка последних стандартов JavaScript
          },
        },
      },
      // Правила для обработки CSS/SCSS файлов
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          'style-loader', // Вставляет CSS в DOM при загрузке страницы
          'css-loader', // Импортирует CSS файлы
          'sass-loader', // Компилирует SCSS в CSS
        ],
      },
    ],
  },
};

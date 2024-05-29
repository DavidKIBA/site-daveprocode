const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  mode: "production", // Ajoutez le mode ici
  entry: {
    "bootstrap.min":
      "./static/bootstrap-footer-20/bootstrap-footer-20/js/bootstrap.min.js",
    popper: "./static/bootstrap-footer-20/bootstrap-footer-20/js/popper.js",
    lightbox: "./static/lib/lightbox/js/lightbox.min.js", // Ajoutez lightbox ici
  },
  output: {
    filename: "[name]",
    path: path.resolve(__dirname, "dist"),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
    }),
  ],
  devtool: "source-map", // Ceci génère les fichiers .map
  resolve: {
    alias: {
      jquery: path.resolve(__dirname, "node_modules/jquery/dist/jquery.js"),
      "popper.js": path.resolve(
        __dirname,
        "node_modules/popper.js/dist/popper.js"
      ),
    },
  },
};

module.exports = {
  transpileDependencies: ["vuetify"],
  publicPath: "/devlog/",
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.md$/,
          loader: "raw-loader", // npm install -D raw-loader
        },
      ],
    },
  },
};

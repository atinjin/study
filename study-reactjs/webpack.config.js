var path = require('path');

module.exports = {
    entry: "./src/index.js",
    mode: "development",
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, "public"),
    },
    devtool: 'source-map',
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                query: {
                    presets: ['env', 'stage-0', 'react']
                }
            }
        ]
    },
    devServer: {
        inline: true,
        hot: true,
        contentBase: __dirname + '/public/',
        proxy: {
            "/app" : "http://localhost:8080"
        }
    }
}
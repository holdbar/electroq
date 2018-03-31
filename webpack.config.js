const HtmlWebPackPlugin = require("html-webpack-plugin");
const BundleTracker = require('webpack-bundle-tracker');
module.exports = {
    module: {
        
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.html$/,
                use: [
                    {
                        loader: "html-loader",
                        options: { minimize: true }
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    'file-loader'
                ]
            }
        ]
    },
    externals: {
        jquery: 'jQuery',
        moment: 'moment'
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./src/index.html",
            filename: "./index.html"
        }),
        new BundleTracker({filename: './webpack-stats.json'}),
        ]
};
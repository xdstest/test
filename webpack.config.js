/* eslint no-var: 0 no-process-env: 0 */

var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var NODE_ENV = process.env.NODE_ENV;

var config = {
	entry: {
		index: './static/js/index.js',
		upload_photo: './static/js/upload_photo.js',
		vendor: ['react', 'react-router', 'flux', 'es6-promise', 'isomorphic-fetch']
	},
	output: {
		path: path.join(__dirname, 'static/dest'),
		filename: '[name].bundle.js',
		publicPath: '/static/'
	},
	plugins: [
		new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.bundle.js'),
		new ExtractTextPlugin('[name].bundle.css'),
		new webpack.HotModuleReplacementPlugin(),
		new webpack.NoErrorsPlugin(),
		new webpack.DefinePlugin({
			'process.env.NODE_ENV': JSON.stringify(NODE_ENV)
		})
	],
	resolve: {
		root: path.join(__dirname, 'static'),
		extension: ['', '.js', '.jsx', '.styl']
	},
	module: {
		loaders: [{
			test: /\.css$/,
			loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
		}, {
			test: /\.(otf|eot|jpg|jpeg|png|svg|ttf|woff|woff2)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
			loader: 'url-loader?limit=8192'
		}, {
			test: /\.html$/,
			loader: 'file?name=[name].[ext]'
		}]
	}
};


if (typeof process.env.NODE_ENV !== 'undefined' && process.env.NODE_ENV === 'production') {
	// Production config
	config.bail = true;
	config.debug = false;
	config.profile = false;
	config.devtool = '#source-map';

	config.output = {
		path: './static/dest',
		pathInfo: true,
		publicPath: '/static/',
		filename: '[name].bundle.js'
	};

	config.plugins = config.plugins.concat([
		new webpack.optimize.OccurenceOrderPlugin(true),
		new webpack.optimize.DedupePlugin(),
		new webpack.optimize.UglifyJsPlugin({ output: { comments: false } })
	]);

	config.module.loaders = config.module.loaders.concat([
		{
			test: /\.js$/,
			loaders: ['babel-loader'],
			exclude: /node_modules/
		}, {
			test: /\.styl$/,
			loader: ExtractTextPlugin.extract(
				'style-loader',
				'css-loader?sourceMap?minimize!autoprefixer?browsers=last 2 version!stylus-loader?sourceMap'
			)
		}
	]);
} else {
	// Development config
	config.devtool = '#inline-source-map';

	config.module.loaders = config.module.loaders.concat([{
		test: /\.js$/,
		loaders: ['react-hot', 'babel-loader'],
		exclude: /node_modules/
	}, {
		test: /\.styl$/,
		loader: ExtractTextPlugin.extract(
			'style-loader',
			'css-loader?sourceMap!autoprefixer?browsers=last 2 version!stylus-loader?sourceMap'
		)
	}]);
}

module.exports = config;

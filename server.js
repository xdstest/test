/* eslint no-var: 0, no-console: 0 */

var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config');

var entry = {};
var item;

for (item in config.entry) {
	if (config.entry.hasOwnProperty(item)) {
		if (item === 'vendor') {
			entry[item] = config.entry[item];
		} else {
			entry[item] = [
				'webpack-dev-server/client?http://localhost:3000',
				'webpack/hot/dev-server',
				config.entry[item]
			];
		}
	}
}

config.entry = entry;

config.output.publicPath = 'http://localhost:3000/';

new WebpackDevServer(webpack(config), {
	publicPath: config.output.publicPath,
	hot: true,
	historyApiFallback: true
}).listen(3000, 'localhost', function (err) {
	if (err) {
		console.log(err);
	}

	console.log('Listening at localhost:3000');
});

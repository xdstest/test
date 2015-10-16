/* global module, require */
/* eslint no-var: 0 */

module.exports = function (grunt) {
	grunt.initConfig({
		run: {
			build: {
				exec: require('os').platform() === 'win32' ? 'SET NODE_ENV=production && webpack -p' :
					'NODE_ENV=production webpack -p'
			},
			dev: {
				exec: 'webpack'
			},
			start: {
				exec: 'node server.js'
			}
		},
		clean: {
			default: 'static/dest/'
		},
		copy: {
			default: {
				files: [{
					expand: true,
					cwd: 'static/vendor/',
					src: ['**'],
					dest: 'static/dest/'
				}, {
					src: ['static/css/bootstrap/js/bootstrap.min.js'],
					dest: 'static/dest/bootstrap.min.js'
				}]
			}
		},
		compress: {
			default: {
				options: {
					mode: 'gzip',
					level: 6
				},
				files: [{
					expand: true,
					cwd: 'static/dest/',
					src: ['**/*.js', '**/*.map', '**/*.css'],
					dest: 'static/dest/',
					rename: function (_dest, _src) {
						return 'static/dest/' + _src + '.gz';
					}
				}]
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-copy');
	grunt.loadNpmTasks('grunt-contrib-compress');
	grunt.loadNpmTasks('grunt-run');

	grunt.registerTask('build', ['clean', 'copy', 'run:build', 'compress']);

	grunt.registerTask('dev', ['clean', 'copy', 'run:dev']);

	grunt.registerTask('start', ['run:start']);
};

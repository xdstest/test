import React, { Component, PropTypes } from 'react';

class Gallery extends Component {
	constructor(props) {
		super(props);
		this.onScroll = this.onScroll.bind(this);
	}

	onScroll(event) {
		console.log(event);
	}

	componentDidMount() {
		window.addEventListener('scroll', this.onScroll);
	}

	componentWillUnmount() {
		window.removeEventListener('scroll', this.onScroll);
	}

	render() {
		console.log('Gallery.render()', this.props);

		return (
			<PhotosList />
		);
	}
}

Gallery.propTypes = {
	userCanEditPhotos: PropTypes.bool.isRequired,
	apiEndpoint: PropTypes.string.isRequired
};

export default Gallery;
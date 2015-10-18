import React, { Component, PropTypes } from 'react';

import PhotosList from '../components/PhotosList';

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
		return (
			<PhotosList />
		);
	}
}

Gallery.propTypes = {
	userCanEditPhotos: PropTypes.bool.isRequired,
	apiEndpoint: PropTypes.string.isRequired
};
Gallery.defaultProps = {userCanEditPhotos: false};

export default Gallery;

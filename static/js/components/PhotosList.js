import React, { Component, PropTypes } from 'react';

import PhotosStore from '../stores/PhotosStore';

import PhotoItem from '../components/PhotoItem';

class PhotosList extends Component {
	constructor(props) {
		super(props);
		this.state = {
			photos: PhotosStore.getAll()
		};
		this.onChange = this.onChange.bind(this);
		this.photoOnClick = this.photoOnClick.bind(this);
	}

	componentDidMount() {
		PhotosStore.addChangeListener(this.onChange);
	}

	componentWillUnmount() {
		PhotosStore.removeChangeListener(this.onChange);
	}

	onChange() {
		this.setState({
			photos: PhotosStore.getAll()
		});
	}

	photoOnClick(photo) {
		if (typeof this.props.photoOnClick === 'function') {
			return this.props.photoOnClick(photo);
		}
	}

	render() {
		let content;

		content = this.state.photos.map(photo => {
			return (
				<PhotoItem key={photo.id} photo={photo} onClick={this.photoOnClick} />
			);
		});

		return (
			<div className="i-timeline">
				{content}
			</div>
		);
	}
}

PhotosList.propTypes = {
	photoOnClick: PropTypes.func
};

export default PhotosList;


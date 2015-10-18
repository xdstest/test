import React, { Component } from 'react';

import PhotosStore from '../stores/PhotosStore';

import PhotoItem from '../components/PhotoItem';

class PhotosList extends Component {
	constructor(props) {
		super(props);
		this.state = {
			photos: PhotosStore.getAll()
		};
		this.onChange = this.onChange.bind(this);
		this.photoClick = this.photoClick.bind(this);
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

	photoClick(photo) {
		console.log(photo);
	}

	render() {
		let content;

		content = this.state.photos.map(photo => {
			return (
				<PhotoItem key={photo.id} photo={photo} onClick={this.photoClick} />
			);
		});

		return (
			<div className="i-timeline">
				{content}
			</div>
		);
	}
}

export default PhotosList;

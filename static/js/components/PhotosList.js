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

	render() {
		let content;

		content = this.state.photos.map(photo => {
			return (
				<PhotoItem key={photo.id} photo={photo} />
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
import React, { Component, PropTypes } from 'react';

import PhotosStore from '../stores/PhotosStore';

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

		//content = flats.items.map(flat => {
		//	return (
		//		<FlatsListItem key={flat.id} currency={currency} flat={flat} staticURL={staticURL}/>
		//	);
		//});

		return (
			<div className="i-timeline">
				{content}
			</div>
		);
	}
}

export default PhotosList;
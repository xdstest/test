import React, { Component, PropTypes } from 'react';

class PhotosList extends Component {
	render() {
		let content;
		const { photos } = this.props;

		if (flats.isFetching) {
			content = (
				<li className="objects-list__more objects-list__more_mod_older objects-list__more_mod_wait">
					<div id="spinner"></div>
				</li>
			);
		} else {
			content = flats.items.map(flat => {
				return (
					<FlatsListItem key={flat.id} currency={currency} flat={flat} staticURL={staticURL} />
				);
			});
		}

		return (
			<ul id="objects" className="objects-list">
				{content}
			</ul>
		);
	}
}

PhotosList.propTypes = {
	photos: PropTypes.object.isRequired
};

export default PhotosList;
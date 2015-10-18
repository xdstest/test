import React, { Component, PropTypes } from 'react';

class PhotoItem extends Component {
	render() {
		let photo = this.props.photo;
		if (photo.photo_full_width > 300) {
			return (
				<div className="i-timeline__item__photo">
					<img src="{photo.photo_full}" width="100%" height="100%" alt=""
						srcset="{photo.photo_timeline} 1x, {photo.photo_timeline_2x} 2x"/>
				</div>
			);
		} else {
			return (
				<div className="i-timeline__item__photo">
					<img src="{photo.photo_full}" width="100%" height="100%" alt=""/>
				</div>
			);
		}
	}
}

export default PhotoItem;
import React, { Component, PropTypes } from 'react';

class PhotoItem extends Component {
	constructor(props) {
		super(props);
		this.onClick = this.onClick.bind(this);
	}

	onClick(event) {
		if (typeof this.props.onClick === 'function') {
			return this.props.onClick(this.props.photo.id);
		}
	}

	render() {
		let photo = this.props.photo;
		let srcSet;
		if (photo.width_photo_full > 300) {
			srcSet = `${photo.photo_timeline_url} 1x, ${photo.photo_timeline_2x_url} 2x`;
		}
		return (
			<div className="i-timeline__item">
				<div className="i-timeline__item__photo">
					<img src={photo.photo_timeline_url} width="100%" height="100%" alt="" srcSet={srcSet}
						onClick={this.onClick} />
				</div>
			</div>
			);
	}
}

PhotoItem.propTypes = {
	photo: PropTypes.object.isRequired,
	onClick: PropTypes.func
};

export default PhotoItem;

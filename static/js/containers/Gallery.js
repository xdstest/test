import React, { Component, PropTypes } from 'react';

import PhotosList from '../components/PhotosList';
import Button from '../components/Button';

class Gallery extends Component {
	constructor(props) {
		super(props);
		this.onScroll = this.onScroll.bind(this);
		this.clickLoadMore = this.clickLoadMore.bind(this);
	}

	componentDidMount() {
		window.addEventListener('scroll', this.onScroll);
	}

	componentWillUnmount() {
		window.removeEventListener('scroll', this.onScroll);
	}

	onScroll(event) {
		console.log(event);
	}

	clickLoadMore() {
		console.log(this);
	}

	render() {
		return (
			<div>
				<PhotosList />
				<div className="i-timeline__load-more">
					<Button text="Load more" onClick={this.clickLoadMore} btnClass="btn-default btn-lg" />
				</div>
			</div>
		);
	}
}

Gallery.propTypes = {
	userCanEditPhotos: PropTypes.bool.isRequired,
	apiEndpoint: PropTypes.string.isRequired
};

Gallery.defaultProps = {
	userCanEditPhotos: false
};

export default Gallery;

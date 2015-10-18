import {debounce} from 'lodash/function';
import React, { Component, PropTypes } from 'react';

import PhotosList from '../components/PhotosList';
import Button from '../components/Button';

class Gallery extends Component {
	constructor(props) {
		super(props);

		this.state = {
			showLoadMoreButton: true
		};

		this.onScroll = debounce(this.onScroll.bind(this), 200);
		this.clickLoadMore = this.clickLoadMore.bind(this);
	}

	componentDidMount() {
		window.addEventListener('scroll', this.onScroll);
	}

	componentWillUnmount() {
		window.removeEventListener('scroll', this.onScroll);
	}

	onScroll(event) {
		if (this.state.showLoadMoreButton) {
			return;
		}
		console.log(event);
	}

	clickLoadMore() {
		this.setState({
			showLoadMoreButton: false
		});
	}

	render() {
		let contentButtonLoadMore = '';
		if (this.state.showLoadMoreButton) {
			contentButtonLoadMore = (
				<div className="i-timeline__load-more">
					<Button text="Load more" onClick={this.clickLoadMore} btnClass="btn-default btn-lg" />
				</div>
			);
		}
		return (
			<div>
				<PhotosList />
				{contentButtonLoadMore}
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

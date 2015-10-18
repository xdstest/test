import 'isomorphic-fetch';
import { debounce } from 'lodash/function';
import { polyfill as promosePolyfill } from 'es6-promise';
import React, { Component, PropTypes } from 'react';

import GalleryApiActions from '../actions/GalleryApiActions';
import PhotosStore from '../stores/PhotosStore';

import PhotosList from '../components/PhotosList';
import Button from '../components/Button';

promosePolyfill();

class Gallery extends Component {
	constructor(props) {
		super(props);

		this.state = {
			showLoadMoreButton: true,
			canLoadMore: true,
			isFetching: false
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

		if (!this.state.isFetching) {
			let y = document.body.offsetHeight - (window.pageYOffset + window.innerHeight);
			if (y < 300) {
				this.fetchPhotos();
			}
		}
	}

	clickLoadMore() {
		this.setState({
			showLoadMoreButton: false
		});
		this.fetchPhotos();
	}

	fetchPhotos() {
		if (this.state.isFetching || !this.state.canLoadMore) {
			return;
		}

		this.setState({
			isFetching: true
		});

		let offset = PhotosStore.getAll().length;
		fetch(this.props.apiEndpoint + '?offset=' + offset, {
			headers: new Headers({
				'X-Requested-With': 'XMLHttpRequest'
			}),
			credentials: 'include'
		}).then(response => {
			this.setState({
				isFetching: false
			});

			if (response.headers.get('content-type') === 'application/json') {
				return response.json().then(json => {
					if (!json.photos.length) {
						this.setState({
							canLoadMore: false
						});
					}
					GalleryApiActions.recivePhotos(json.photos);
				});
			} else {
				let error = new Error(response.statusText);
				error.response = response;
				return Promise.reject(error);
			}
		}).catch(err => {
			alert(err);
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
		} else if (this.state.isFetching) {
			contentButtonLoadMore = (
				<div className="i-timeline__load-more">
					<span className="glyphicon glyphicon-refresh i-timeline__load-more__spin"></span>
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

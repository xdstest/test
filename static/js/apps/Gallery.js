import React from 'react';
import ReactDOM from 'react-dom';

import GalleryApiActions from '../actions/GalleryApiActions';

import Gallery from '../containers/Gallery';

export default function (options) {
	if (!options.photos) {
		return;
	}

	GalleryApiActions.reciveInitPhotos(options.photos);

	ReactDOM.render(
		<Gallery apiEndpoint={options.apiEndpoint} userCanEditPhotos={options.userCanEditPhotos} />,
		document.getElementsByClassName('i-timeline__wrap')[0]
	);
}
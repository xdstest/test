import React from 'react';
import ReactDOM from 'react-dom';

import GalleryApiActions from '../actions/GalleryApiActions';

export default function (options) {
	if (!options.photos) {
		return;
	}

	GalleryApiActions.reciveInitPhotos(options.photos);

	ReactDOM.render(
		<Gallery />,
		document.getElementsByClassName('i-timeline')[0]
	);
}
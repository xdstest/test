import '../css/index.styl';

// import React from 'react'; window.React = React;
import UploadPhotoApp from './apps/UploadPhoto';
import GalleryApp from './apps/Gallery';

window.apps = {
	UploadPhoto: UploadPhotoApp,
	Gallery: GalleryApp
};
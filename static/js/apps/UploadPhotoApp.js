import UploadPhotoForm from './components/UploadPhotoForm';
import React from 'react';
import ReactDOM from 'react-dom';

export default function () {
	ReactDOM.render(
		<UploadPhotoForm />,
		document.getElementById(document.getElementsByClassName('i-upload-photo')[0])
	);
}
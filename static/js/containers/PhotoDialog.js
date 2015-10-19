import 'dialog-polyfill';

import React, { Component, PropTypes } from 'react';

class PhotoDialog extends Component {
	constructor(props) {
		super(props);
		this.close = this.close.bind(this);
		this.dialog = null;
	}

	componentDidMount() {
		this.dialog = document.getElementsByClassName('i-dialog-photo')[0];
		if (!this.dialog.showModal) {
			window.dialogPolyfill.registerDialog(this.dialog);
		}
		this.dialog.addEventListener('close', this.close);
		this.dialog.showModal();
	}

	componentWillUnmount() {
		if (this.dialog) {
			try {
				// Catch exception
				// Uncaught InvalidStateError: Failed to execute 'close' on 'HTMLDialogElement':
				// The element does not have an 'open' attribute, and therefore cannot be closed.
				this.dialog.close();
			} catch (e){}
		}
		this.dialog.removeEventListener('close', this.close);
	}

	close() {
		this.props.onClose();
	}

	render() {
		let photo = this.props.photo;
		return (
			<dialog>
				<div className="i-dialog-photo">
					<div className="i-dialog-photo__image">
						<img src={photo.photo_full_url} width="100%" height="100%" alt="" />
					</div>
					<div class="i-dialog-photo__caption">
						<h3><a href={photo.user_url}>{photo.user_username}</a></h3>
						{photo.caption}
					</div>
				</div>
			</dialog>
		);
	}
}

PhotoDialog.propTypes = {
	photo: PropTypes.object.isRequired,
	onClose: PropTypes.func.isRequired
};

export default PhotoDialog;

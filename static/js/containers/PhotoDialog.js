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
			<dialog className="i-dialog-photo">
				I'm a dialog!
				<form method="dialog">
					<input type="submit" value="Close"/>
				</form>
			</dialog>
		);
	}
}

PhotoDialog.propTypes = {
	photo: PropTypes.object.isRequired,
	onClose: PropTypes.func.isRequired
};

export default PhotoDialog;

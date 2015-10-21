import 'dialog-polyfill';

import React, { Component, PropTypes } from 'react';

import Button from '../components/Button';

class PhotoDialog extends Component {
	constructor(props) {
		super(props);
		this.close = this.close.bind(this);
		this.clickEditButton = this.clickEditButton.bind(this);
		this.dialog = null;
	}

	componentDidMount() {
		this.dialog = document.getElementsByClassName('i-dialog-photo__wrap')[0];
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

	clickEditButton() {
		window.location.pathname = '/photo/edit/' + this.props.photo.id + '/';
	}

	render() {
		let photo = this.props.photo;
		let contentEditButton = '';
		if (photo.user_username === this.props.requestUser || this.props.requestUserIsModerator) {
			contentEditButton = (
				<div className="i-dialog-photo__edit-btn">
					<Button text="Edit" onClick={this.clickEditButton} btnClass="btn-default" />
				</div>
			);
		}
		return (
			<dialog className="i-dialog-photo__wrap">
				<div className="i-dialog-photo">
					<div className="i-dialog-photo__image">
						<img src={photo.photo_full_url} width="100%" alt="" />
					</div>
					<div className="i-dialog-photo__caption">
						<span className="glyphicon glyphicon-remove i-dialog-photo__close" onClick={this.close}></span>
						<h3><a href={photo.user_url}>{photo.user_username}</a></h3>
						{contentEditButton}
						<div dangerouslySetInnerHTML={{__html: photo.caption}} />
					</div>
				</div>
			</dialog>
		);
	}
}

PhotoDialog.propTypes = {
	requestUser: PropTypes.string.isRequired,
	requestUserIsModerator: PropTypes.bool.isRequired,
	photo: PropTypes.object.isRequired,
	onClose: PropTypes.func.isRequired
};

export default PhotoDialog;

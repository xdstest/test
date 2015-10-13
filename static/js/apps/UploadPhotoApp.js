/*
 * Обработчик формы для отправки по xhr
 *
 */

import 'isomorphic-fetch';

let UploadPhotoForm = class {
	constructor(wrapper) {
		this.btn = wrapper.getElementsByClassName('i-upload-photo__btn')[0];
		this.formWrap = wrapper.getElementsByClassName('i-upload-photo__wrap')[0];
		this.form = this.formWrap.getElementsByTagName('form')[0];
		this.onBtnClick = this.onBtnClick.bind(this);
		this.onFormSubmit = this.onFormSubmit.bind(this);
		this.formSubmitSuccess = this.formSubmitSuccess.bind(this);
		this.formSubmitError = this.formSubmitError.bind(this);
		this.addEvents();
	}

	addEvents() {
		this.btn.addEventListener('click', this.onBtnClick);
		this.form.addEventListener('submit', this.onFormSubmit);
	}

	removeEvents() {
		this.btn.removeEventListener('click', this.onBtnClick);
		this.form.removeEventListener('submit', this.onFormSubmit);
	}

	onBtnClick() {
		if (this.formWrap.classList.contains('i-upload-photo__wrap_mod_hidden')) {
			this.showForm();
		} else {
			this.hideForm();
		}
	}

	onFormSubmit(e) {
		e.preventDefault();
		if (!this.form.querySelector('input[type="file"]').value) {
			return false;
		}
		fetch(this.form.getAttribute('action') || window.location.href, {
			method: this.form.getAttribute('method') || 'post',
			headers: new Headers({
				"X-Requested-With": "XMLHttpRequest"
			}),
			credentials: 'include',
			body: new FormData(this.form)
		}).then(this.formSubmitSuccess).catch(this.formSubmitError);
	}

	formSubmitSuccess(response) {
		this.form.reset();
		this.hideForm();
	}

	formSubmitError(err) {
		alert(err);
	}

	showForm() {
		this.formWrap.classList.remove('i-upload-photo__wrap_mod_hidden');
		this.btn.classList.add('i-upload-photo__btn_mod_hidden');
	}

	hideForm() {
		this.formWrap.classList.add('i-upload-photo__wrap_mod_hidden');
		this.btn.classList.remove('i-upload-photo__btn_mod_hidden');
	}
};

export default function () {
	return new UploadPhotoForm(...arguments);
}
import EventEmitter from 'events';

import { ActionTypes } from '../constants/GalleryConstants';
import GalleryAppDispatcher from '../dispatcher/GalleryAppDispatcher';

const CHANGE_EVENT = 'change';

class _PhotosStore extends EventEmitter {
	constructor() {
		super();
		this.photos = [];
		this.photosIds = [];
	}

	emitChange() {
		this.emit(CHANGE_EVENT);
	}

	addChangeListener(callback) {
		this.on(CHANGE_EVENT, callback);
	}

	removeChangeListener(callback) {
		this.removeListener(CHANGE_EVENT, callback);
	}

	getAll() {
		return this.photos;
	}

	reset() {
		this.photos = [];
		this.photosIds = [];
	}

	addPhotos(photos) {
		photos.forEach(photo => {
			if (this.photosIds.indexOf(photo.id) === -1) {
				this.photos.push(photo);
			}
		});
	}
}

_PhotosStore.dispatchToken = null;

let PhotosStore = new _PhotosStore();

PhotosStore.dispatchToken = GalleryAppDispatcher.register(action => {
	switch (action.type) {
	case ActionTypes.RECEIVE_INIT_PHOTOS:
		PhotosStore.reset();
		PhotosStore.addPhotos(action.photos);
		PhotosStore.emitChange();
		break;

	default:
		// do nothing
	}
});

export default PhotosStore;

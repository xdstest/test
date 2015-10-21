import { ActionTypes } from '../constants/GalleryConstants';
import GalleryAppDispatcher from '../dispatcher/GalleryAppDispatcher';

export default {
	reciveInitPhotos: function (photos) {
		GalleryAppDispatcher.dispatch({
			type: ActionTypes.RECEIVE_INIT_PHOTOS,
			photos: photos
		});
	},

	recivePhotos: function (photos) {
		GalleryAppDispatcher.dispatch({
			type: ActionTypes.RECEIVE_PHOTOS,
			photos: photos
		});
	},

	clearPhotos: function () {
		GalleryAppDispatcher.dispatch({
			type: ActionTypes.CLEAR_PHOTOS
		});
	}
};
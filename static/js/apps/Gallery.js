import ReactDOM from 'react-dom';

export default function (options) {
	ReactDOM.render(
		<Gallery />,
		document.getElementsByClassName('i-timeline')[0]
	);
}
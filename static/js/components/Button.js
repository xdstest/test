import React, { Component, PropTypes } from 'react';

class Button extends Component {
	render() {
		let btnClass = `btn ${this.props.btnClass}`;
		return (
			<button className={btnClass} onClick={this.props.onClick}>{this.props.text}</button>
		);
	}
}

Button.propTypes = {
	text: PropTypes.string.isRequired,
	btnClass: PropTypes.string.isRequired,
	onClick: PropTypes.func.isRequired
};

Button.defaultProps = {
	btnClass: 'btn-default'
};

export default Button;

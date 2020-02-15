import React, { Component } from 'react';
import Login from './view/Login';
import Header from './view/Header';

class App extends Component {
	render() {
		return (
            <>
                <Header/>
                <Login />
            </>
        );
	}
}

export default App;

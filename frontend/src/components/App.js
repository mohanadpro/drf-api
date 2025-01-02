import React, {Component} from 'react'
import { render } from 'react-dom';
import {createRoot} from 'react-dom/client';
import Books from './books';
export default class App extends Component{
    constructor(props){
        super(props)
    }
    render(){
        return <div>
            <h1>Hello world</h1>
            <h4>My Life would be very good</h4>
            <Books/>
        </div>
    }
}

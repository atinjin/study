"use strict"

//REACT
import React from 'react';
import {render} from 'react-dom';

import logger from 'redux-logger';
import {applyMiddleware, createStore} from 'redux';

const reducer = function(state=0,action) {
    switch(action.type) {
        case "POST_COUNSELLING":
        return state + action.payload;
    }
    return state;
};
const middleware = applyMiddleware(logger);
const store = createStore(reducer);

store.subscribe(function(){
    console.log('current state is:' + store.getState());
})  ;

import Counsel from './components/pages/counsellList';

render(
    <Counsel />, document.getElementById('app')
);

store.dispatch({
    type:"POST_COUNSELLING",
    payload: 1
});

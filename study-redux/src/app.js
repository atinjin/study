"use strict"

import {createStore} from 'redux';

const reducer = function(state=[],action) {
    switch(action.type) {
        case "POST_COUNSELLING":
            return state + action.payload;
        default:
            break;
    }
    return state;
}

const store = createStore(reducer);

store.subscribe(function(){
    console.log('current state is:' + store.getState());
    console.log('상담 내용: ', store.getState()[1].title);
}) 

store.dispatch({
    type:"POST_COUNSELLING",
    payload: [{
        id:1,
        title: '2018년 2월 24일 일요일 미나리 상담 내역',
        time: '25m',
        purchase: [
            "유산균",
            "비타민 D"
        ]
    },
    {
        id:2,
        title: '2018년 2월 24일 일요일 까나리 상담 내역',
        time: '25m',
        purchase: [
            "유산균",
            "비타민 D"
        ]
    }
    ]
})

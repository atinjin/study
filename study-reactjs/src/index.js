import React from 'react'
import { render } from 'react-dom'
import Menu from './components/Menu'
import data from './data/data'

windows.React = React

render (
    <Menu recipes={data}/>,
    document.getElementById("react-countainer")
)
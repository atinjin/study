import React from 'react'
import { render } from 'react-dom'
import fetch from 'isomorphic-fetch'

class Ingredient extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: null,
            loading: false
        }
    }

    componentDidMount() {
        this.setState({loading: true})
        fetch('/app/jobs')
            .then(response => response.json())
            .then(d => this.setState({data: response}))
        this.setState({loading: false})
    }

    render() {
        const {data, loading} = this.state
        console.log(data + loading)
        return (loading) ?
            <div>로딩 중</div>:
            <div>{data}</div>
    }

}

// const Ingredient = ({amount, measurement, name}) =>
//     <li>
//         <span className="amount">{amount}</span>
//         <span className="measurement">{measurement}</span>
//         <span className="name">{name}</span>
//     </li>

export default Ingredient
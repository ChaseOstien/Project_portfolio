import { useState } from "react";
import './App.css';

export default function Api() {
    const [apiData, setApiData] = useState(null);

    async function getJoke() {
    try {
        const response = await fetch('https://icanhazdadjoke.com/', {
            headers: {
                'Accept': 'application/json'
            }
        });
        const data = await response.json();
        setApiData(data.joke);
        
    } catch (error) {
        console.log(error);
    }
}

    return (
        <div className="container">
            <button className='button' onClick={getJoke}>Get a Joke!</button>
            {apiData === null && <h3 className="joke">No jokes yet!</h3>}
            <h3 className="joke">
                {apiData}
            </h3>
        </div>
    )
}

import axios from "axios"

const baseUrl = "http://localhost:5000/";

const postQuery = (queryParameter)=>{
    axios.post(baseUrl+"search_movies", {query: queryParameter})
    .then(response=>{
        console.log(response.data);
    })
    .catch(error=>{
        console.log(error);
    })
}

export {postQuery}
import React from "react";
import { useState, useEffect } from "react";
import SearchBar from "./SearchBar";
import "./App.css";
import { Box, Flex, Text, Link, Spacer } from "@chakra-ui/react";

const baseUrl = process.env.REACT_APP_BACKEND;

function App() {
  const [results, setResults] = useState([]);
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    fetch(baseUrl + "load_authors")
      .then((response) => response.json())
      .then((data) => {
        setAuthors(data["message"]);
        console.log(data)
      });
  }, []);

  return (
    <div className=" h-screen flex flex-col">
      <div className="flex items-center justify-center">
        <SearchBar setresults={setResults} />
      </div>
      <div className="search-results flex-grow flex  justify-center">
        <Box p={4} position={"fixed"} top={100} left={3}>
          <Flex direction={"column"} align="left" justify={"left"} h="100%" w="100%" alignContent={"left"} alignItems={"left"}>
            <Text fontSize="2xl" className="font-bold">
              {"Made by"}
            </Text>
            {authors.map((author) => {
              return (<>
                <Text fontSize="xl" >
                  {author.name}
                </Text>
                <Spacer>  </Spacer>
                <Text fontSize="sm" >
                  {author.roll}
                </Text>
              </>)
            })}
          </Flex>
        </Box>
        <Box>
          {results.length > 0 && results.map((result) => (
            <Box
              key={result.id}
              borderWidth="1px"
              borderRadius="lg"
              maxW={"lg"}
              p={4}
              my={2}
            >
              <Link href={result.link} isExternal>
                <Text fontSize="lg" fontWeight="bold" >
                  {result.title}
                </Text>
              </Link>

              <Text mt={2}>{result.description}</Text>
            </Box>
          ))}
          {results.length <= 0 && <>
            <Flex direction="row" align="center" justify="center" h="100%" w="100%" alignContent={"center"} alignItems={"center"}>
              <Text fontSize="4xl" >
                {"Nothing to show :("}
              </Text>

            </Flex>
          </>}
        </Box>
      </div>

    </div>
  );
}

export default App;

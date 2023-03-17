import React from "react";
import { useState } from "react";
import { Button, Flex, Input, Spacer, Text, Grid } from "@chakra-ui/react";
import axios from "axios";
import { SearchIcon } from '@chakra-ui/icons'

import { FaGithub } from 'react-icons/fa';


const SearchBar = ({ setresults }) => {
  const [searchQuery, setsearchQuery] = useState("");
  const baseUrl = process.env.REACT_APP_BACKEND;

  const searchArticles = () => {
    console.log("here")
    axios
      .post(baseUrl + "search_articles", { query: searchQuery }, { headers: { 'Content-Type': 'application/json' } })
      .then((response) => {
        console.log(response.data.hits);
        setresults(response.data.hits)
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const handleSearchChange = (e) => {
    const val = e.target.value;
    setsearchQuery(val);
  };

  return (
    <Grid templateColumns={"repeat(3,1fr)"} h="100%" w="100%" className="py-4 bg-blue-50" alignItems={"center"}>
      <Text className="text-xl text-zinc-500 font-bold px-4">
        News Search
      </Text>
      <Flex>
        <Input
          type="text"
          value={searchQuery}
          onChange={handleSearchChange}
          variant="filled"
          placeholder="Search"
          className="bg-orange-700 border-orange-300"
        />
        <Button bgColor="#00df9a" ml={2} onClick={searchArticles}>
          <SearchIcon color={"white.500"} className="" />
        </Button>
      </Flex>

      <Text justifySelf={"end"} className="text-xl text-zinc-500 font-bold px-4 mr-4">
        <FaGithub />
      </Text>
    </Grid>
  );
};

export default SearchBar;

import React from 'react';
import { Button, Flex, Input, Spacer, Text } from '@chakra-ui/react'

const SearchBar = () => {
  return (
    <Flex direction="column" align="center" justify="center" h="100%" w="100%">
      <Text className='text-2xl text-zinc-400 font-bold pb-5'>Search any Movie you want</Text>
      <Flex>
        <Input variant='filled' placeholder="Search" className="bg-white text-gray-600 h-10 px-5 pr-10 rounded-full text-sm focus:outline-none" />
        <Button bgColor='#00df9a' ml={2}>
          <Text className='px-3 py-2 text-black'>Search</Text>
        </Button>
      </Flex>
    </Flex>
  );
};

export default SearchBar;

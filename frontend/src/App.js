import React from 'react';
import SearchBar from './SearchBar';
import ContactFooter from './ContactFooter';
import './App.css';

function App() {
  return (
    <div className="bg-gray-800 h-screen flex flex-col">
      <div className="flex-grow flex items-center justify-center">
        <SearchBar />
      </div>
      <div className="mt-auto">
        <ContactFooter />
      </div>
    </div>
  );
}

export default App;

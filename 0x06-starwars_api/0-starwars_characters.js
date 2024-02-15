#!/usr/bin/node
// Request and print characters
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <id>');
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  // console.log(data.characters);
  await FetchCharactersName(data.characters);
});

async function FetchCharactersName (characters) {
  for (const characterUrl of characters) {
    try {
      const character = await fetchCharacter(characterUrl);
      console.log(character.name);
    } catch (error) {
      console.error(error);
    }
  }
}

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        // reject(`Error: ${response.statusCode}`);
        reject(new Error(error));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

'use strict';

const Promise = require('promise');
const scraper = require('./utils/scraper');

function upcoming (platform) {
  return new Promise(function (fulfill, reject) {
    scraper('http://www.ign.com/games/upcoming/' + platform, 'div.gameList div.gameList-gameShort', [{
      title: 'div.game-title a | removeNonAsciiCharacters | trim',
      platform: 'span.game-platform',
      genres: 'div.game-details | removeDuplicateWhitespace | trim | split: " , "',
      publisher: 'div.publisher | trim',
      releaseDate: 'div.releaseDate | trim | asDate',
      gameUrl: 'div.game-title a@href'
    }])(function (err, res) {
      if (err) {
        reject(err);
      } else {
        fulfill(res);
      }
    });
  });
}

module.exports = upcoming;
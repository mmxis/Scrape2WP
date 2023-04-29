'use strict';

const Promise = require('promise');
const scraper = require('./utils/scraper');
const qs = require("querystring");

function search (searchString) {
  return new Promise(function (fulfill, reject) {
    var queryString = qs.stringify({
      q: searchString,
      type: 'object',
      objectType: 'game'
    });
    
    scraper('http://www.ign.com/search?' + queryString, {
      totalResults: 'div#search-list@data-total',
      games: scraper('div#search-list div.search-item', [{
        title: 'div.search-item-title a | removeDuplicateWhitespace | removeNonAsciiCharacters | trim',
        gameUrl: 'div.search-item-title a@href',
        publisher: 'div.search-item-sub-title a:nth-of-type(1) | trim',
        platform: 'div.search-item-sub-title a:not(:first-child) | trim'
        /* platforms: ['div.search-item-sub-title a:not(:first-child) | trim'] */
      }])
    })(function (err, res) {
      if (err) {
        reject(err);
      } else {
        fulfill(res);
      }
    });
  });
}

module.exports = search;
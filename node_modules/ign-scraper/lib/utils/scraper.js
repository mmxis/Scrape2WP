'use strict';

const Xray = require('x-ray');

const scraper = new Xray({
  filters: {
    trim: function (value) {
      return typeof value === 'string' ? value.trim() : value;
    },
    withoutLeading: function (value, startsWithString) {
      if (typeof value === 'string' && value.startsWith(startsWithString)) {
        return value.substring(startsWithString.length);
      } else {
        return value;
      }
    },
    removeDuplicateWhitespace: function (value) {
      return typeof value === 'string' ? value.replace(/\s+/g, ' ') : value;
    },
    removeNonAsciiCharacters: function (value) {
      return typeof value === 'string' ? value.replace(/[^\x00-\x7F]/g, "") : value;
    },
    asDate: function (value) {
      return typeof value === 'string' && !value.startsWith('TBA') && !isNaN(Date.parse(value)) ? new Date(value) : value;
    },
    asFloat: function (value) {
      return typeof value === 'string' && !isNaN(parseFloat(value)) ? parseFloat(value) : value;
    },
    split: function (value, separator) {
      return typeof value === 'string' ? value.split(separator) : value;
    }
  }
});

module.exports = scraper;
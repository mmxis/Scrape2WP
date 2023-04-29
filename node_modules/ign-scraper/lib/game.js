'use strict';

const Promise = require('promise');
const scraper = require('./utils/scraper');

function game (url) {
  return new Promise(function (fulfill, reject) {
    scraper(url, {
      title: 'h1 a | removeNonAsciiCharacters | trim',
      platform: 'div.contentPlatformsText span:nth-child(1) a',
      otherPlatformNames: ['div.contentPlatformsText span:not(:first-child) a'],
      otherPlatformUrls: ['div.contentPlatformsText span:not(:first-child) a@href'],
      summary: ['div#summary div.gameInfo p | removeDuplicateWhitespace | removeNonAsciiCharacters | trim'],
      features: ['div#features ul li | removeDuplicateWhitespace | removeNonAsciiCharacters | trim'],
      genre: 'div.gameInfo-list:nth-of-type(2) div:nth-child(1) a | trim | removeDuplicateWhitespace | removeNonAsciiCharacters | trim',
      publisher: 'div.gameInfo-list:nth-of-type(2) div:nth-child(2) a | removeNonAsciiCharacters | trim',
      developer: 'div.gameInfo-list:nth-of-type(2) div:nth-child(3) a | removeNonAsciiCharacters | trim',
      releaseDate: 'div.gameInfo-list.leftColumn div:nth-child(1) | trim | withoutLeading: "Release Date:" | trim | asDate',
      editions: scraper('div#editions ul', [{
        region: 'li.editions-region | trim',
        title: 'li.editions-info div.editions-details a | removeDuplicateWhitespace | removeNonAsciiCharacters | trim',
        releaseDate: 'li.editions-info div.editions-details div:contains(Release Date:) | trim | withoutLeading: "Release Date:" | trim | asDate',
        publisher: 'li.editions-info div.editions-details div:contains(Publisher:) | trim | withoutLeading: "Publisher:" | trim'
      }]),
      ignRatingValue: 'div.ignRating div.ratingValue:not(div:has(span.noRating)) | trim | asFloat',
      ignRatingText: 'div.ignRating div.ratingText:not(div:has(span.noRating)) | trim',
      communityRatingValue: 'div.communityRating div.ratingValue:not(div:has(span.noRating)) | trim | asFloat',
      communityRatingText: 'div.communityRating div.ratingText:not(div:has(span.noRating)) | trim',
      boxArtImageUrl: 'div.mainBoxArt img@src',
      reviewUrl: '#mainArticleContainer div[itemprop="itemReviewed"] h3 a.reviewTitle@href',
      reviewSummary: '#mainArticleContainer div.articlesubHeadline span.text | removeDuplicateWhitespace | removeNonAsciiCharacters | trim'
    })(function (err, res) {
      if (err) {
        reject(err);
      } else {
        // some manual shifting around required here because x-ray currently doesn't handle arrays in nested scrapers right
        var otherPlatforms = [];

        res.otherPlatformNames.forEach(function (platform, index) {
          var otherPlatform = [];
          otherPlatform.platform = platform;
          otherPlatforms.push(otherPlatform);
        });

        res.otherPlatformUrls.forEach(function (url, index) {
          otherPlatforms[index].url = url;
        });

        res.otherPlatforms = otherPlatforms;
        delete res.otherPlatformNames;
        delete res.otherPlatformUrls;

        fulfill(res);
      }
    });
  });
}

module.exports = game;
Data
====

This repository contains various corpora and textual data that I often use
while experimenting with various statistical models (see
https://github.com/jlund3/modelt). Storing data like this in git isn't ideal,
but it is convenient.

Bible
=====

This dataset is the King James version of The Holy Bible. Each line consists of
a single verse of text. The line format is as follows:

Book.Chapter.Verse VerseText

The dataset also contains cross references within the bible from
http://www.openbible.info/labs/cross-references/, along with some slight
cleanup and reformatting. Each line in the cross reference file contains a cross
reference of the format:

Book.Chapter.Verse Book.Chapter.Verse

Stopwords
=========

Stopwords contains various stopword lists. Each list gives one stopword per
line. Each stopword has been lowercased and stripped of punctuation.

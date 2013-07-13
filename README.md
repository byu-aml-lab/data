Data
====

This repository contains various corpora and textual data that I often use
while experimenting with various statistical models (see
https://github.com/jlund3/modelt). Storing data like this in git isn't ideal,
but it is convenient.

Newsgroups
==========

20 Newsgroups is a well known (perhaps even over used) dataset consisting of
20,000 usenet postings from the early 90's. The documents are equally
distributed from 20 different newsgroups on a variety of topics. Note though
that many of the newsgroups are similar in nature (e.g. talk.region.misc and
soc.religion.christian).

Each subdirectory of the dataset names a specific newsgroup. Each file in the
subdirectory is a posting. Note that each file has a header that describes the
document metadata in more detail. This header should not be included as part of
the posting, and can be skipped by reading the file after the first blank line.

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

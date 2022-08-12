

from typing import Optional, List, Any

from nltk import TreebankWordTokenizer


class NltkTokenizer(TreebankWordTokenizer):

    def __init__(self,
                 punctuation: Optional[List[Any]] = None,
                 starting_quotes: Optional[Any] = None):
        super().__init__()
        self.punctuation = punctuation or self.PUNCTUATION
        self.starting_quotes = starting_quotes or self.STARTING_QUOTES

    def tokenize(self, text, convert_parentheses=False, return_str=False):
        for regexp, substitution in self.starting_quotes:
            text = regexp.sub(substitution, text)

        for regexp, substitution in self.punctuation:
            text = regexp.sub(substitution, text)

        # Handles parentheses.
        regexp, substitution = self.PARENS_BRACKETS
        text = regexp.sub(substitution, text)
        # Optionally convert parentheses
        if convert_parentheses:
            for regexp, substitution in self.CONVERT_PARENTHESES:
                text = regexp.sub(substitution, text)

        # Handles double dash.
        regexp, substitution = self.DOUBLE_DASHES
        text = regexp.sub(substitution, text)

        # add extra space to make things easier
        text = " " + text + " "

        for regexp, substitution in self.ENDING_QUOTES:
            text = regexp.sub(substitution, text)

        for regexp in self.CONTRACTIONS2:
            text = regexp.sub(r' \1 \2 ', text)
        for regexp in self.CONTRACTIONS3:
            text = regexp.sub(r' \1 \2 ', text)


        return text if return_str else text.split()

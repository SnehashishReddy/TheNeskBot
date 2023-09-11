from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer


def summarize(text_article: str) -> str:
    return LexRankSummary(text_article)


def LexRankSummary(text_article: str) -> str:
    parser = PlaintextParser.from_string(text_article, Tokenizer("english"))
    summarizer = LexRankSummarizer(stemmer=Stemmer('english'))

    try:
        summary = summarizer(parser.document, 3)

        answer = []

        for sentence in summary:
            answer.append(sentence.__str__())

        return (' '.join(answer))
    except RuntimeError:
        return "The given text could not be summarized."

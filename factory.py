from abc import ABC, abstractmethod
from googletrans import Translator


class ILanguage(ABC):

    def __init__(self, message=None):
        self.message = message

    @abstractmethod
    def translate(self):
        """Interface Method"""
        raise NotImplementedError('Method must be implemented by subclass')


class EnglishClass(ILanguage):

    def translate(self):
        translator = Translator()
        translated = translator.translate(self.message)
        return translated.text


class JapanClass(ILanguage):

    def translate(self):
        translator = Translator()
        translated = translator.translate(self.message, dest='ja')
        return translated.text


class TurkishClass(ILanguage):

    def translate(self):
        translator = Translator()
        translated = translator.translate(self.message, dest='Turkish')
        return translated.text


class LanguageFactory:

    @staticmethod
    def get_language(language, msg=None):
        if language == 'english':
            return EnglishClass(msg)

        if language == 'turkish':
            return TurkishClass(msg)

        if language == 'japan':
            return JapanClass(msg)
        else:
            raise ValueError


if __name__ == '__main__':

    language = LanguageFactory.get_language(
        'japan',
        'hi every one'
    )
    print(language.translate())

    language = LanguageFactory.get_language(
        'english',
        'こんにちは、元気ですか'
    )
    print(language.translate())








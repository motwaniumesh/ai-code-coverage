class StringUtils:
    @staticmethod
    def reverse_string(text: str) -> str:
        return text[::-1]
    
    @staticmethod
    def count_vowels(text: str) -> int:
        return sum(1 for char in text.lower() if char in 'aeiou')
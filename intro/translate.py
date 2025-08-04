text = "hello world"
# Create translation table: 'h' → 'H', 'l' → 'L'
translation_table = str.maketrans('hl', 'HL')
result = text.translate(translation_table)
print(result)  # Output: HeLLo worLd

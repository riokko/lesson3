with open('referat.txt', 'r', encoding='utf-8') as text:
	text = text.read()

length = len(text)
print(length)

word_count = text.split(' ')
print(len(word_count))

new_text = text.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as t:
	t.write(new_text)
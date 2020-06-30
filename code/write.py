predictions, actuals = ['a'] * 5 + ['<EOS>'], ['b'] * 5 + ['<EOS>']
with open('predictions', 'w') as p, open('actuals', 'w') as a:
	p.write('\n'.join(predictions).replace('<EOS>', '.'))
	a.write('\n'.join(actuals))
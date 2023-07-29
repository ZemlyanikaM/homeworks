names = ['Mary', 'Mike', 'Olga', 'Ivan']
salaries = [30000, 40000, 25000, 35000]
awards = ['10.75%', '6.15%', '8%', '9.55%']

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})

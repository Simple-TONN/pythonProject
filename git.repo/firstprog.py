import pprint

person = int(input("введите количество гостей: "))
pprint(f"Для обеда  на {person} человек. Требуется:")
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ],
  ['тест',
      [
        ['хурма', 60, 'гр.'],
        ['шмиви', 60, 'т.'],
        ['творог_тест', 690, 'гр.'],
      ]
  ]

]

 for dish in cook_book:
    pprint()
    pprint(f"{dish[0]}:")
    for ingredient in dish[1]:
        pprint(f"{ingredient[0]}, {ingredient[1] * person}{ingredient[2]}")

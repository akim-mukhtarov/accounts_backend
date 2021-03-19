class Categories():
    BASE = 250
    BOYAR = 500
    RICH = 1000
    MECENAT = 2000

    choices = (
        (BASE, 'базовый'),
        (BOYAR, 'боярин'),
        (RICH, 'богач'),
        (MECENAT, 'меценат')
    )

    conditions = (
        {
            'required_amount': BASE,
            'name': 'базовый'
        },
        {
            'required_amount': BOYAR,
            'name': 'боярин'
        },
        {
            'required_amount': RICH,
            'name': 'богач'
        },
        {
            'required_amount': MECENAT,
            'name': 'меценат'
        }
    )

    presents_variants = {
        BASE: [
            'Час за ПК',
            'Полчаса за PS',
            'Полчаса за ПК'
            ],
        BOYAR: [
            'Батончик',
            '1.5 часа за ПК',
            'Кола 0.5',
            'Ночной пакет (стандарт)'
            ],
        RICH: [
            'Утренний пакет (VIP)',
            'Кола и батончик',
            '3 часа за PS'
            ],
        MECENAT: [
            'Абонемент на посещение клуба (все выходные)',
            'Кальян',
            'Ночной пакет (VIP)'
            ]
    }

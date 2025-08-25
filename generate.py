"""
<details class="tiles-container menu-tiles-container" name="menu">
  <summary onclick="getElementById('Напитки').scrollIntoView({behavior: 'instant', block: 'start', inline: 'nearest'})" id="Напитки">Напитки</summary>
  <div class="tile">
    <img src="./static/menu-greendrink.webp" alt="Тестовое изображение меню">
    <div class="menu-text">
      <h3>Воин Дракона</h3>
      <p class="menu-price">440₽</p>
    </div>
  </div>
  <div class="tile">
    <img src="./static/menu-bluedrink.webp" alt="Тестовое изображение меню">
    <div class="menu-text">
      <h3>великое<br>Зелье Маны</h3>
      <p class="menu-price">8008₽</p>
    </div>
  </div>
</details>
"""

import csv

start_line = """
          <details class="tiles-container menu-tiles-container pop-tile">
            <summary id="{category}">
              {category}<br>
              <img src="./static/menu/{category}.webp" alt="Иллюстрация к категории меню &quot{category}&quot ">
            </summary>
""".strip("\n")
tile = """
            <div class="tile pop-tile">
              <img src="./static/menu/{id}.webp" alt="Иллюстрация к блюду {pretty_name}">
              <div class="menu-text">
                <h3>{pretty_name}</h3>
                <p class="menu-price">{price}₽</p>
              </div>
            </div>
""".strip("\n")

end_line = """
          </details>
""".strip("\n")

menu_map = dict()


def main():
    res = list()

    with open("menu.csv", "r") as menu_file:
        menu_reader = csv.reader(menu_file, delimiter=" ", quotechar="|")
        next(menu_reader)

        for category, ID, pretty_name, price in menu_reader:
            if category not in menu_map:
                menu_map[category] = list()
            menu_map[category].append(
                {"id": ID, "pretty_name": pretty_name, "price": price}
            )

    for category in menu_map.keys():
        res.append(start_line.format(category=category))

        for item in menu_map[category]:
            res.append(tile.format_map(item))

        res.append(end_line)

    return res


if __name__ == "__main__":
    print('\n'.join(main()))

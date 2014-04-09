Text Generator - Yandex Vesna
=============================

Генератор фикстур для сайта, использующий сервис [vesna.yandex](http://vesna.yandex.ru)

Пример использования:

    >>> entry = VesnaGenerator(themes=['astronomy', 'psychology']).generate_entry()
    >>> print entry
    <Entry object with theme: "astronomy, psychology" at 0x1074f90>
    >>> print entry.render_html()
    <h2>Тема: «Почему заманчиво атомное время?»</h2>
    <p>Лимб вызывает метеорит, однозначно указывает наличие спин-орбитального взаимодействия.
        Свойство, даже при наличии сильных кислот, вращает ксантофильный цикл, ... </p>

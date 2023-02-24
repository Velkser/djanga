page1 = '''
<!DOCTYPE HTML>
<html>

<head>
    <title>Мой заголовок</title>
    <link rel="stylesheet" href="styls.css">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="description" content="Это моя самая интересная страница о HTML" />
</head>

<body>
    <h1 class="test">Test</h1>
    <div id="Первый_блок">
        <h4 id="Верх">
            <a href="#Низ">Верхняя точка страницы</a>
        </h4>
        <p class = "test">Это моя первая веб-страница.</p>
        <p class = "test">Я люблю программировать!</p>
        <p>Если декодирование в JSON не удалось, <em>r.json()</em> вернет исключение. Например, если ответ с кодом 204
            (No Content), или на случай если ответ содержит не валидный JSON, попытка обращения к <em>r.json()</em>
            будет возвращать <strong>ValueError: No JSON object could be decoded.</strong></p>
        <p>
            Это текст<br />
            Для проверки работы br
        </p>
    </div>

    <h1>Моя первая веб-страница</h1>
    <h2>Что это такое</h2>
    <br /><br /><br /><br />
    <ul>
        <li>Чтобы изучить HTML</li>
        <li>Чтобы похвастать</li>
        <li>Потому что я обожаю свой компьютер и хочу привить ему любовь к HTML</li>
    </ul>
    <br><br>
    <ol>
        <li>
            <ol>
                <li>Чтобы изучить HTML</li>
                <li>Чтобы похвастать</li>
                <li>Потому что я обожаю свой компьютер и хочу привить ему любовь к HTML</li>
            </ol>
        </li>
        <li>
            <ol>
                <li>Чтобы изучить HTML</li>
                <li>Чтобы похвастать</li>
                <li>Потому что я обожаю свой компьютер и хочу привить ему любовь к HTML</li>
            </ol>
        </li>
        <li>
            <ol>
                <li>Чтобы изучить HTML</li>
                <li>Чтобы похвастать</li>
                <li>Потому что я обожаю свой компьютер и хочу привить ему любовь к HTML</li>
            </ol>
        </li>
    </ol>
    <br><br>
    <p><a href="http://www.msiter.ru">MSITER.RU</a></p>


    <img src="img/img1.jpg" width="400" height="200" alt="My image" />

    <br>

    <table class="table">
        <tr>
            <th>Строка 1, ячейка 1</th>
            <th>Строка 1, ячейка 2</th>
            <th>Строка 1, ячейка 3</th>
        </tr>
        <tr>
            <th>Строка 2, ячейка 1</th>
            <th>Строка 2, ячейка 2</th>
            <th>Строка 2, ячейка 3</th>
        </tr>
        <tr>
            <th>Строка 3, ячейка 1</th>
            <th>Строка 3, ячейка 2</th>
            <th><img src="img/img1.jpg" width="120" height="90" alt="My image" /></th>
        </tr>
    </table>

    <table class="table">
        <tr>
            <th>Заголовок столбца 1</th>
            <th>Заголовок столбца 2</th>
            <th>Заголовок столбца 3</th>
        </tr>
        <tr>
            <th>Строка 2, ячейка 1</th>
            <th colspan="2">Строка 2, ячейка 2, также захватывается Строка 2, ячейка 3</th>
        </tr>
        <tr>
            <th rowspan="2">Строка 3, ячейка 1, также захватывается Строка 4, ячейка 1</th>
            <th>Строка 3, ячейка 2</th>
            <th>Строка 3, ячейка 3</th>
        </tr>
        <tr>
            <th>Строка 4, ячейка 2</th>
            <th>Строка 4, ячейка 3</th>
        </tr>
    </table>

    <br /><br />
    <form action='processingscript.php'>
        <input type="text" />
        <br />
        <input type="password" />
        <br />
        <textarea rows="5" cols="20">Здесь вводят много текстовой информации</textarea>
        <br />
        <select>
            <option value="first option">Младше 18</option>
            <option value="second option">От 18 до 28</option>
            <option value="third option">Старше 28</option>
        </select>
    </form>

    <div id="scissors">
        <p>Это мой случайный текст. Я хочу выделить только  это</span> слово и больше никакое.</p>
    </div>

    <h1>Несколько случайных словарных статей</h1>
    <dl>
        <dt>HTML</dt>
        <dd>Аббревиатура от HyperText Markup Language – язык для создания веб-страниц.</dd>

        <dt>Собака</dt>
        <dd>Любое хищное животное из семейства Canidae.</dd>
        <dd>Одомашненная разновидность животного семейства Canidae, Canis lupus familiaris.</dd>

        <dt>Молоко</dt>
        <dt>Кошачье пиво</dt>
        <dd>Белая жидкость, которую производят коровы и которую люди использую в пищу.</dd>
    </dl>


    <h1>Работа с сылками и JavaScript</h1>

    <script type="text/javascript">
        function opennastypopup() {
            window.open("test.html", "", "toolbar=no,height=1000,width=700");
            return false;
        }
    </script>

    <a href='https://msiter.ru/tutorials/html-prodvinutogo-urovnya/dostupnye-ssylki' accesskey="s">Другая страница</a>

    ////////////////////////////////
    <a href="#" onclick="opennastypopup()" onkeypress="opennastypopup()" title="Открывает что-то">Монстр</a>

    ////////////////////////////////
    <a href='test.html' onclick="return opennastypopup()" onkeypress="return opennastypopup()">Монстр</a>


    <h1>Обработка текста</h1>
    <p>
        Этот вебсайт посвящен <abbr title="HyperText Markup Language">HTML</abbr>
        <acronym title="Телеграфное агентство Советского Союза">ТАСС</acronym>.
    </p>



    <p>
        Я спросил Сергея о цитатах, и он ответил
        <cite>О цитатах я знаю столько же сколько и о мышлении птиц</cite>.
        А затем добавил:
        <q>Так что я ничем не могу помочь.</q>
        К счастью я нашел хороший учебник...
    </p>


    <blockquote title="Из учебника">
        <p>
            Теги blockquote, q и cite используются для определения цитат.
            Тег blockquote создает блочный элемент и используется для определения больших цитат,
            в то время как тег q создает строчный элемент и используется для цитат небольшого размера.
        </p>
    </blockquote>


    <code>
        <var>Bool</var> = true;
    </code>

    <pre>
        &lt;div id="intro"&gt;
        &lt;h1&gt;Заголовок&lt;/h1&gt;
        &lt;p&gt;Параграфный параграф.&lt;/p&gt;
        &lt;/div&gt;
    </pre>


    <p>
        <dfn
            title="Мутация, при которой сочетается два или больше наборов хромосом представителей разных видов">Аллополиплоид</dfn>
        - это…
    </p>

    <address>
        г. Гдеград<br />
        ул. Кудыкина<br />
        д. 160, кв. 8
    </address>

    <p>
        Теперь введите: <kbd>Ваше имя</kbd>
    </p>

    <br /><br />
    <h1>Таблици версия №3</h1>
    <table class="table">
        <colgroup>
            <col />
            <col class="paper" />
            <col />
        </colgroup>
        <tr>
            <td>Это</td>
            <td>То</td>
            <td>Другое</td>
        </tr>
        <tr>
            <td>Птичка</td>
            <td>Крокодил</td>
            <td>Завтрак</td>
        </tr>
    </table>
    <br /><br /><br /><br />

    <table class="table">
        <thead>
            <tr>
                <th>Заголовок 1</th>
                <th>Заголовок 2</th>
                <th>Заголовок 3</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Нижний колонтитул 1</th>
                <th>Нижний колонтитул 2</th>
                <th>Нижний колонтитул 3</th>
            </tr>
        </tfoot>
        <tbody>
            <tr>
                <th>Ячейка 1</th>
                <th>Ячейка 2</th>
                <th>Ячейка 3</th>
            </tr>
            <tr>
                <th>Ячейка 4</th>
                <th>Ячейка 5</th>
                <th>Ячейка 6</th>
            </tr>
            <tr>
                <th>Ячейка 7</th>
                <th>Ячейка 8</th>
                <th>Ячейка 9</th>
            </tr>
            <tr>
                <th>Ячейка 10</th>
                <th>Ячейка 11</th>
                <th>Ячейка 12</th>
            </tr>
        </tbody>
    </table>

    <br /><br /><br /><br />

    <div class="scroll-table">
        <table>
            <thead>
                <tr>
                    <th>Название блюда</th>
                    <th>Белки</th>
                    <th>Жиры</th>
                    <th>Углеводы</th>
                    <th>Ккал</th>
                </tr>
            </thead>
        </table>	
        <div class="scroll-table-body">
            <table>
                <tbody>
                    <tr>
                        <td>Азу</td>
                        <td>11,9</td>
                        <td>14,2</td>
                        <td>10,2</td>
                        <td>214</td>
                    </tr>
                    <tr>
                        <td>Бефстроганов из говядины</td>
                        <td>16,7</td>
                        <td>11,3</td>
                        <td>5,9</td>
                        <td>193</td>
                    </tr>
                    <tr>
                        <td>Бифштекс</td>
                        <td>27,8</td>
                        <td>29,6</td>
                        <td>1,7</td>
                        <td>384</td>
                    </tr>
                    <tr>
                        <td>Блины</td>
                        <td>6,1</td>
                        <td>12,3</td>
                        <td>26</td>
                        <td>233</td>
                    </tr>
                    <tr>
                        <td>Борщ украинский</td>
                        <td>1,1</td>
                        <td>2,2</td>
                        <td>6,7</td>
                        <td>49</td>
                    </tr>
                    <tr>
                        <td>Буженина вареная</td>
                        <td>16,4</td>
                        <td>18,3</td>
                        <td>1</td>
                        <td>233</td>
                    </tr>
                    <tr>
                        <td>Вареники с картофелем</td>
                        <td>4,4</td>
                        <td>3,7</td>
                        <td>18,5</td>
                        <td>125</td>
                    </tr>
                    <tr>
                        <td>Говяжий гуляш</td>
                        <td>14</td>
                        <td>9,2</td>
                        <td>2,6</td>
                        <td>148</td>
                    </tr>
                    <tr>
                        <td>Запеканка творожная</td>
                        <td>17,6</td>
                        <td>4,2</td>
                        <td>14,2</td>
                        <td>168</td>
                    </tr>
                    <tr>
                        <td>Зразы картофельные с капустой</td>
                        <td>3,3</td>
                        <td>3,9</td>
                        <td>15</td>
                        <td>108</td>
                    </tr>
                    <tr>
                        <td>Клецки</td>
                        <td>5</td>
                        <td>4,8</td>
                        <td>25,8</td>
                        <td>160</td>
                    </tr>
                    <tr>
                        <td>Котлеты из курицы</td>
                        <td>18,2</td>
                        <td>10,4</td>
                        <td>13,8</td>
                        <td>222</td>
                    </tr>
                    <tr>
                        <td>Куриное филе вареное</td>
                        <td>30,4</td>
                        <td>3,5</td>
                        <td>0</td>
                        <td>153</td>
                    </tr>
                    <tr>
                        <td>Куриные бедра</td>
                        <td>21,3</td>
                        <td>11</td>
                        <td>0,1</td>
                        <td>185</td>
                    </tr>
                    <tr>
                        <td>Лагман</td>
                        <td>4,3</td>
                        <td>8,9</td>
                        <td>13,3</td>
                        <td>158</td>
                    </tr>
                    <tr>
                        <td>Макароны вареные с жиром</td>
                        <td>3,4</td>
                        <td>5</td>
                        <td>19</td>
                        <td>135</td>
                    </tr>
                    <tr>
                        <td>Овощное рагу (4 сезона)</td>
                        <td>0,5</td>
                        <td>0,1</td>
                        <td>3,8</td>
                        <td>38</td>
                    </tr>
                    <tr>
                        <td>Окрошка мясная с квасом</td>
                        <td>2,1</td>
                        <td>1,7</td>
                        <td>6,3</td>
                        <td>52</td>
                    </tr>
                    <tr>
                        <td>Пельмени</td>
                        <td>11,9</td>
                        <td>12,4</td>
                        <td>29</td>
                        <td>275</td>
                    </tr>
                    <tr>
                        <td>Плов с бараниной (4 сезона)</td>
                        <td>4,2</td>
                        <td>6</td>
                        <td>14,9</td>
                        <td>150</td>
                    </tr>
                    <tr>
                        <td>Рассольник</td>
                        <td>1,4</td>
                        <td>2</td>
                        <td>5</td>
                        <td>42</td>
                    </tr>
                    <tr>
                        <td>Салат крабовый</td>
                        <td>9,2</td>
                        <td>7,4</td>
                        <td>5,9</td>
                        <td>128</td>
                    </tr>
                    <tr>
                        <td>Салат Мимоза</td>
                        <td>5,7</td>
                        <td>14,8</td>
                        <td>7,2</td>
                        <td>183</td>
                    </tr>
                    <tr>
                        <td>Салат Цезарь</td>
                        <td>15</td>
                        <td>10</td>
                        <td>9</td>
                        <td>190</td>
                    </tr>
                    <tr>
                        <td>Самса с курицей</td>
                        <td>11</td>
                        <td>24</td>
                        <td>17</td>
                        <td>325</td>
                    </tr>
                    <tr>
                        <td>Свекольник</td>
                        <td>0,5</td>
                        <td>2</td>
                        <td>4,2</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Свинина тушеная</td>
                        <td>9,8</td>
                        <td>20,3</td>
                        <td>3,2</td>
                        <td>235</td>
                    </tr>
                    <tr>
                        <td>Солянка домашняя</td>
                        <td>3,5</td>
                        <td>3,5</td>
                        <td>4,3</td>
                        <td>64</td>
                    </tr>
                    <tr>
                        <td>Суп гороховый</td>
                        <td>4,4</td>
                        <td>2,4</td>
                        <td>8,9</td>
                        <td>66</td>
                    </tr>
                    <tr>
                        <td>Суп молочный с макаронами</td>
                        <td>2,2</td>
                        <td>1,9</td>
                        <td>7,9</td>
                        <td>58</td>
                    </tr>
                    <tr>
                        <td>Суп харчо с мясом</td>
                        <td>3,1</td>
                        <td>4,5</td>
                        <td>5,5</td>
                        <td>75</td>
                    </tr>
                    <tr>
                        <td>Сырник творожный</td>
                        <td>18,6</td>
                        <td>3,6</td>
                        <td>18,2</td>
                        <td>183</td>
                    </tr>
                    <tr>
                        <td>Тефтели свиные</td>
                        <td>7</td>
                        <td>10</td>
                        <td>12</td>
                        <td>172</td>
                    </tr>
                    <tr>
                        <td>Уха</td>
                        <td>3,4</td>
                        <td>1</td>
                        <td>5,5</td>
                        <td>46</td>
                    </tr>
                    <tr>
                        <td>Чахохбили с фасолью (4 сезона)</td>
                        <td>6,2</td>
                        <td>5,5</td>
                        <td>3,4</td>
                        <td>87</td>
                    </tr>
                    <tr>
                        <td>Щи из свежей капусты с картофелем</td>
                        <td>1</td>
                        <td>3,8</td>
                        <td>2,1</td>
                        <td>38</td>
                    </tr>
                    <tr>
                        <td>Эскалоп</td>
                        <td>19</td>
                        <td>42,8</td>
                        <td>6,8</td>
                        <td>487</td>
                    </tr>
                </tbody>
            </table>
        </div>	
    </div>



    <script type="text/javascript">
        function display_weather(){
            let pass = document.getElementById('password').value;
            if (pass == "Mupalu"){
                let res = "Вы указали правильрый пароль";
            } else{
                let res = "Вы указали не правильрый пароль";
            }
            return res;
        }
    </script>
    <form action='display_weather.js' >
        <fieldset>
           <legend>ФИО</legend>
           <p>Имя <input type="text" name="firstName" /></p>
           <p>Фамилия <input type="text" name="lastName" /></p>
        </fieldset>
        <fieldset>
           <legend>Адрес</legend>
           <p>Адрес <textarea name="address" ></textarea></p>
           <p>Индекс <input type="text" name="postcode" /></p>
        </fieldset>
        <fieldset>
            <legend>Предпочтения</legend>
            <p>Введите пароль: </p>
            <input type="password" id="password"/>
            <p>Выберите язык:</p>
            <select>
                <option value="first option">Python Core</option>
                <option value="second option">Java</option>
                <option value="third option">C++</option>
            </select>
            <p>You:</p>
            <p><input type="radio" name="areyou" value="male" /> Male</p>
            <p><input type="radio" name="areyou" value="female" /> Female</p>
            <p><input type="radio" name="areyou" value="hermaphrodite" />I dont know</p>

            <p><input type="submit" /></p>
            <p><input type="reset" /></p>
        </fieldset>
    <h2 id="Низ">
        <a href="#Верх" onclick="alert ('Сейчас вас перебросит на верх!')">Нижняя точка страницы</a>
    </h2>
</body>

</html>

'''
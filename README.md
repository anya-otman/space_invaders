# Space invaders game :space_invader:
_____
# Цель игры
В игре 3 уровня. На каждом уровне нужно убить всех врагов и при этом не погибнуть от их пуль.
# Ход игры
:black_medium_small_square: Изначально у игрока 3 жизни, если в игрока попадает пуля, то отнимается одна жизнь.
Также можно получить одну жизнь, если попасть в привидение, пролетающее несколько раз за игру наверху экрана.   
![Image alt](https://github.com/anya-otman/space_invaders/blob/main/images/extra.png)   
:black_medium_small_square: В игре есть бонусы: фиолетовые и голубые шарики.    
Фиолетовый бонус даёт возможность ускоренно стрелять. ![Image alt](https://github.com/anya-otman/space_invaders/blob/task4/images/bonus_f.png)    
Поймав голубой бонус, вы получаете защиту от вражеских пуль. ![Image alt](https://github.com/anya-otman/space_invaders/blob/task4/images/bonus_pr.png)   
Время действия бонусов ограничено :)  
Если один из бонусов уже взят, и время его действия не вышло, а игрок поймал еще один бонус другого вида, действие первого бонуса аннулируется и заменяется на действие пойманного бонуса.   
:black_medium_small_square: При проигрыше игра начинается заново с 1 уровня.    
:black_medium_small_square: Если вам не понравился ход игры, то можно перезапустить текущий уровень с начала, нажав на клавишу R
# Управление
:arrow_left: двигаться влево    
:arrow_right: двигаться вправо    
`space` стрелять прямо    
:arrow_up: стрелять под углом вправо    
:arrow_down: стрелять под углом влево   
`R` перезапуск текущего уровня
# Подготовка к запуску
В проекте используется модуль `Pygame`, поэтому перед запуском необходимо установить его через терминал:
```
pip install pygame
```
_____
`Creators`: Отман Анна, Трубецких Валерия КН-201

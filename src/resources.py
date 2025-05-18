# resources.py
#
# Copyright 2025 Nathan Perlman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

related_words = {
    (_('ICE CREAM FLAVORS')): [(_('berry')), (_('cream')), (_('ice')), (_('vanilla')), (_('choco')), (_('sweet')), (_('cold')), (_('treat')), (_('scoop')), (_('cone'))],
    (_('FRUITS')): [(_('fruit')), (_('apple')), (_('banana')), (_('peach')), (_('grape')), (_('citrus')), (_('plum')), (_('melon')), (_('mango')), (_('kiwi'))],
    (_('VEGETABLES')): [(_('greens')), (_('carrot')), (_('beans')), (_('pea')), (_('beet')), (_('onion')), (_('cabbage')), (_('squash')), (_('radish')), (_('turnip'))],
    (_('BREAKFAST FOODS')): [(_('bacon')), (_('toast')), (_('waffle')), (_('pancake')), (_('egg')), (_('meal')), (_('bagel')), (_('cereal')), (_('fruit')), (_('hash'))],
    (_('ANIMALS')): [(_('dog')), (_('cat')), (_('fish')), (_('horse')), (_('mouse')), (_('tiger')), (_('lion')), (_('bat')), (_('shark')), (_('sheep'))],
    (_('VEHICLES')): [(_('truck')), (_('car')), (_('bus')), (_('train')), (_('plane')), (_('boat')), (_('bike')), (_('jeep')), (_('scooter')), (_('wagon'))],
    (_('COLORS')): [(_('blue')), (_('grey')), (_('red')), (_('green')), (_('pink')), (_('white')), (_('brown')), (_('teal')), (_('black')), (_('beige'))],
    (_('SPORTS')): [(_('ball')), (_('match')), (_('game')), (_('goal')), (_('swim')), (_('tennis')), (_('run')), (_('golf')), (_('coach')), (_('track'))],
    (_('MUSIC GENRES')): [(_('jazz')), (_('blues')), (_('rock')), (_('pop')), (_('rap')), (_('folk')), (_('punk')), (_('dance')), (_('opera')), (_('metal'))],
    (_('MOVIES')): [(_('movie')), (_('comedy')), (_('drama')), (_('horror')), (_('thrill')), (_('crime')), (_('action')), (_('family')), (_('scary')), (_('spy'))],
    (_('BOOKS')): [(_('book')), (_('novel')), (_('story')), (_('essay')), (_('paper')), (_('author')), (_('poetry')), (_('title')), (_('genre')), (_('pages'))],
    (_('CITIES')): [(_('city')), (_('town')), (_('metro')), (_('block')), (_('plaza')), (_('square')), (_('urban')), (_('park')), (_('village')), (_('court'))],
    (_('MOUNTAINS')): [(_('hill')), (_('peak')), (_('rock')), (_('ridge')), (_('trail')), (_('stone')), (_('path')), (_('summit')), (_('cliff')), (_('crag'))],
    (_('OCEANS')): [(_('sea')), (_('wave')), (_('beach')), (_('coast')), (_('tide')), (_('shore')), (_('water')), (_('island')), (_('reef')), (_('bay'))],
    (_('WEATHER')): [(_('rain')), (_('wind')), (_('cloud')), (_('snow')), (_('storm')), (_('hail')), (_('fog')), (_('breeze')), (_('frost')), (_('chill'))],
    (_('SPACE')): [(_('space')), (_('moon')), (_('star')), (_('comet')), (_('orbit')), (_('nova')), (_('planet')), (_('rocket')), (_('asteroid')), (_('ring'))],
    (_('COMPUTERS')): [(_('laptop')), (_('coding')), (_('data')), (_('logic')), (_('files')), (_('mouse')), (_('click')), (_('input')), (_('server')), (_('error'))],
    (_('SOCIAL MEDIA')): [(_('tweet')), (_('post')), (_('chat')), (_('likes')), (_('viral')), (_('trend')), (_('story')), (_('share')), (_('video')), (_('reels'))],
    (_('FASHION')): [(_('style')), (_('pants')), (_('shirt')), (_('boots')), (_('dress')), (_('scarf')), (_('jeans')), (_('skirt')), (_('belt')), (_('glove'))],
    (_('FOOD')): [(_('meal')), (_('snack')), (_('candy')), (_('pizza')), (_('bread')), (_('chips')), (_('fruit')), (_('toast')), (_('soup')), (_('nuts'))],
    (_('TECHNOLOGY')): [(_('app')), (_('phone')), (_('robot')), (_('gadget')), (_('cloud')), (_('tablet')), (_('logic')), (_('server')), (_('screen')), (_('data'))],
    (_('ECONOMICS')): [(_('money')), (_('trade')), (_('stock')), (_('price')), (_('market')), (_('value')), (_('profit')), (_('cost')), (_('tax')), (_('goods'))],
    (_('POLITICS')): [(_('vote')), (_('party')), (_('court')), (_('policy')), (_('power')), (_('reform')), (_('bills')), (_('debate')), (_('leader')), (_('rights'))],
    (_('HISTORY')): [(_('past')), (_('event')), (_('war')), (_('era')), (_('peace')), (_('reign')), (_('nation')), (_('empire')), (_('king')), (_('queen'))],
    (_('HEALTH')): [(_('diet')), (_('fit')), (_('sleep')), (_('heal')), (_('virus')), (_('meds')), (_('doctor')), (_('pill')), (_('nurse')), (_('clinic'))],
    (_('EDUCATION')): [(_('learn')), (_('study')), (_('grade')), (_('tests')), (_('books')), (_('essay')), (_('math')), (_('class')), (_('teach')), (_('notes'))],
    (_('ART')): [(_('paint')), (_('craft')), (_('draw')), (_('color')), (_('shape')), (_('sketch')), (_('design')), (_('image')), (_('canvas')), (_('line'))],
    (_('PHOTOGRAPHY')): [(_('photo')), (_('frame')), (_('lens')), (_('scene')), (_('focus')), (_('angle')), (_('light')), (_('flash')), (_('shot')), (_('view'))],
    (_('ARCHITECTURE')): [(_('build')), (_('house')), (_('tower')), (_('brick')), (_('urban')), (_('plans')), (_('roof')), (_('rooms')), (_('stone')), (_('wall'))],
    (_('NATURE')): [(_('plant')), (_('river')), (_('trees')), (_('grass')), (_('flora')), (_('field')), (_('woods')), (_('stone')), (_('bush')), (_('vine'))],
    (_('CRAFTS')): [(_('sew')), (_('paint')), (_('knit')), (_('mold')), (_('lace')), (_('thread')), (_('bead')), (_('stitch')), (_('diy')), (_('craft'))],
    (_('BOARD GAMES')): [(_('chess')), (_('dice')), (_('clue')), (_('cards')), (_('risk')), (_('pawn')), (_('check')), (_('move')), (_('jenga')), (_('board'))],
    (_('VIDEO GAMES')): [(_('games')), (_('enemy')), (_('score')), (_('level')), (_('play')), (_('pixel')), (_('quest')), (_('shoot')), (_('jump')), (_('fight'))],
    (_('GARDENING')): [(_('plant')), (_('grow')), (_('prune')), (_('tools')), (_('soil')), (_('water')), (_('seeds')), (_('weeds')), (_('herbs')), (_('pots'))],
    (_('HOBBIES')): [(_('read')), (_('paint')), (_('dance')), (_('sew')), (_('knit')), (_('bake')), (_('craft')), (_('draw')), (_('play')), (_('write'))],
    (_('DANCE')): [(_('ballet')), (_('tap')), (_('jazz')), (_('spin')), (_('twirl')), (_('moves')), (_('rhythm')), (_('break')), (_('step')), (_('tango'))],
    (_('TRAVEL')): [(_('trip')), (_('hotel')), (_('map')), (_('roads')), (_('guide')), (_('train')), (_('plane')), (_('beach')), (_('visit')), (_('camp'))],
    (_('FITNESS')): [(_('run')), (_('walk')), (_('yoga')), (_('cycle')), (_('bench')), (_('track')), (_('pullup')), (_('squat')), (_('pushup')), (_('fit'))],
    (_('COOKING')): [(_('chef')), (_('cook')), (_('bake')), (_('grill')), (_('slice')), (_('stir')), (_('toast')), (_('boil')), (_('dough')), (_('steam'))],
    (_('BEAUTY')): [(_('style')), (_('nails')), (_('skin')), (_('spa')), (_('hair')), (_('lip')), (_('face')), (_('gloss')), (_('cream')), (_('brush'))],
    (_('MYTHOLOGY')): [(_('myth')), (_('god')), (_('beast')), (_('lore')), (_('hero')), (_('magic')), (_('curse')), (_('fate')), (_('oracle')), (_('troll'))],
    (_('PHILOSOPHY')): [(_('logic')), (_('truth')), (_('mind')), (_('faith')), (_('value')), (_('moral')), (_('ideal')), (_('ideas')), (_('reason')), (_('thought'))],
    (_('SCIENCE')): [(_('cells')), (_('atoms')), (_('study')), (_('light')), (_('tests')), (_('force')), (_('brain')), (_('field')), (_('virus')), (_('data'))],
    (_('HOLIDAYS')): [(_('party')), (_('gifts')), (_('cards')), (_('feast')), (_('snow')), (_('elves')), (_('candy')), (_('tree')), (_('cheer')), (_('sled'))],
    (_('FLOWERS')): [(_('rose')), (_('lily')), (_('daisy')), (_('tulip')), (_('bloom')), (_('petal')), (_('violet')), (_('poppy')), (_('orchid')), (_('bud'))],
    (_('DRINKS')): [(_('water')), (_('juice')), (_('soda')), (_('shake')), (_('cider')), (_('tea')), (_('tonic')), (_('latte')), (_('mocha')), (_('milk'))],
    (_('CLOTHING')): [(_('shirt')), (_('pants')), (_('dress')), (_('skirt')), (_('scarf')), (_('hat')), (_('vest')), (_('socks')), (_('boots')), (_('jeans'))],
    (_('INSECTS')): [(_('bee')), (_('ant')), (_('moth')), (_('fly')), (_('gnat')), (_('roach')), (_('wasp')), (_('spider')), (_('beetle')), (_('tick'))],
    (_('JOBS')): [(_('pilot')), (_('nurse')), (_('chef')), (_('clerk')), (_('actor')), (_('guard')), (_('miner')), (_('coach')), (_('agent')), (_('judge'))],
    (_('TOOLS')): [(_('hammer')), (_('screw')), (_('blade')), (_('nails')), (_('drill')), (_('plier')), (_('saw')), (_('level')), (_('ruler')), (_('wrench'))],
    (_('GAMES')): [(_('cards')), (_('dice')), (_('poker')), (_('clue')), (_('chess')), (_('risk')), (_('bingo')), (_('go')), (_('jenga')), (_('board'))],
    (_('HOUSES')): [(_('home')), (_('cabin')), (_('loft')), (_('barn')), (_('tower')), (_('villa')), (_('castle')), (_('ranch')), (_('rooms')), (_('roof'))],
    (_('DESERTS')): [(_('dunes')), (_('cactus')), (_('sands')), (_('rocks')), (_('dust')), (_('oasis')), (_('heat')), (_('dry')), (_('wind')), (_('sun'))],
    (_('BIRDS')): [(_('crow')), (_('swan')), (_('robin')), (_('eagle')), (_('finch')), (_('crane')), (_('parrot')), (_('pigeon')), (_('sparrow')), (_('heron'))],
    (_('BEACHES')): [(_('sand')), (_('reef')), (_('shore')), (_('coast')), (_('tide')), (_('waves')), (_('ocean')), (_('breeze')), (_('sun')), (_('shell'))],
    (_('FURNITURE')): [(_('chair')), (_('table')), (_('sofa')), (_('bench')), (_('stool')), (_('desk')), (_('lamp')), (_('bed')), (_('shelf')), (_('couch'))],
    (_('JEWELRY')): [(_('ring')), (_('brace')), (_('pearl')), (_('beads')), (_('stone')), (_('chain')), (_('gold')), (_('gem')), (_('watch')), (_('band'))],
    (_('LANGUAGES')): [(_('latin')), (_('greek')), (_('hindi')), (_('hebrew')), (_('dutch')), (_('swahili')), (_('korean')), (_('arabic')), (_('french')), (_('spanish'))],
    (_('PLANETS')): [(_('mars')), (_('venus')), (_('earth')), (_('pluto')), (_('orbit')), (_('ring')), (_('jupiter')), (_('saturn')), (_('neptune')), (_('moon'))],
    (_('CAMPING')): [(_('tent')), (_('fire')), (_('trail')), (_('camp')), (_('lamp')), (_('gear')), (_('sleep')), (_('hike')), (_('tools')), (_('grill'))],
    (_('MUSIC')): [(_('piano')), (_('lyric')), (_('vocal')), (_('drums')), (_('bass')), (_('guitar')), (_('notes')), (_('flute')), (_('violin')), (_('horn'))],
    (_('WONDERS')): [(_('ruins')), (_('temple')), (_('tower')), (_('stone')), (_('castle')), (_('bridge')), (_('garden')), (_('pyramid')), (_('palace')), (_('statue'))],
    (_('MYTHICAL CREATURES')): [(_('elf')), (_('fairy')), (_('hydra')), (_('troll')), (_('phoenix')), (_('dragon')), (_('sprite')), (_('beast')), (_('mermaid')), (_('giant'))],
    (_('SHAPES')): [(_('circle')), (_('square')), (_('sphere')), (_('cone')), (_('cube')), (_('oval')), (_('hexagon')), (_('rhombus')), (_('prism')), (_('arc'))],
    (_('DESSERTS')): [(_('cake')), (_('pie')), (_('cookie')), (_('tart')), (_('fudge')), (_('mousse')), (_('sorbet')), (_('gelato')), (_('pudding')), (_('donut'))],
    (_('BEVERAGES')): [(_('coffee')), (_('mojito')), (_('squash')), (_('sprite')), (_('tonics')), (_('cocoa')), (_('smooth')), (_('latte')), (_('seltz')), (_('chai'))],
    (_('HORROR')): [(_('ghost')), (_('haunt')), (_('spirit')), (_('scream')), (_('crypt')), (_('knife')), (_('curse')), (_('beast')), (_('zombie')), (_('creepy'))],
    (_('ASTRONOMY')): [(_('nebula')), (_('cosmos')), (_('galaxy')), (_('comets')), (_('planet')), (_('lunar')), (_('space')), (_('stars')), (_('orbit')), (_('nova'))],
    (_('FANTASY')): [(_('castle')), (_('dragon')), (_('wizard')), (_('magic')), (_('elves')), (_('troll')), (_('realm')), (_('sword')), (_('giants')), (_('knight'))],
    (_('PIRATES')): [(_('parrot')), (_('swords')), (_('golden')), (_('rum')), (_('ships')), (_('shanty')), (_('cannon')), (_('mutiny')), (_('booty')), (_('pegleg'))],
    (_('KITCHEN')): [(_('knife')), (_('spices')), (_('plates')), (_('spoons')), (_('mixers')), (_('aprons')), (_('utens')), (_('mixer')), (_('dishes')), (_('gloves'))],
    (_('MONSTERS')): [(_('zombie')), (_('witch')), (_('ghoul')), (_('kraken')), (_('goblin')), (_('beast')), (_('hydra')), (_('slime')), (_('ghosts')), (_('fiends'))],
    (_('GARDENS')): [(_('roses')), (_('weeds')), (_('hedges')), (_('herbs')), (_('shrubs')), (_('vines')), (_('seeds')), (_('blooms')), (_('roots')), (_('petals'))],
    (_('TRAINS')): [(_('engine')), (_('tracks')), (_('cargos')), (_('ticket')), (_('rails')), (_('wagon')), (_('diesel')), (_('signal')), (_('horns')), (_('switch'))],
    (_('LEGENDS')): [(_('heroes')), (_('mythos')), (_('quests')), (_('scroll')), (_('runes')), (_('giants')), (_('lore')), (_('epics')), (_('tales')), (_('swords'))],
    (_('HIKING')): [(_('trails')), (_('climbs')), (_('packs')), (_('water')), (_('boots')), (_('rocks')), (_('views')), (_('camped')), (_('poles')), (_('steps'))],
    (_('PLANTS')): [(_('fern')), (_('bamboo')), (_('ivy')), (_('shrub')), (_('bark')), (_('leaf')), (_('bud')), (_('stem')), (_('roots')), (_('moss'))],
    (_('UNDERWATER LIFE')): [(_('fish')), (_('shrimp')), (_('coral')), (_('shark')), (_('whale')), (_('tuna')), (_('crab')), (_('squid')), (_('angler')), (_('urchin'))],
    (_('WILDLIFE')): [(_('deer')), (_('fox')), (_('wolf')), (_('bear')), (_('owl')), (_('eagle')), (_('snake')), (_('frog')), (_('moose')), (_('otter'))],
    (_('SEASONS')): [(_('summer')), (_('winter')), (_('autumn')), (_('spring')), (_('fall')), (_('season')), (_('harvest')), (_('snow')), (_('breeze')), (_('blossom'))],
    (_('GEMS')): [(_('diamond')), (_('ruby')), (_('lapis')), (_('opal')), (_('jasper')), (_('emerald')), (_('topaz')), (_('garnet')), (_('pearl')), (_('onyx'))],
    (_('EMOTIONS')): [(_('happy')), (_('sad')), (_('angry')), (_('excited')), (_('fear')), (_('love')), (_('joy')), (_('angst')), (_('grief')), (_('relief'))],
    (_('CANDY')): [(_('sugar')), (_('fudge')), (_('candy')), (_('mint')), (_('gummy')), (_('sweet')), (_('treats')), (_('choco')), (_('caramel')), (_('nougat'))],
    (_('TOOLS')): [(_('screw')), (_('drill')), (_('wrench')), (_('plier')), (_('knife')), (_('saw')), (_('level')), (_('ruler')), (_('blade')), (_('bolts'))],
    (_('ALIENS')): [(_('alien')), (_('ufo')), (_('mars')), (_('green')), (_('ship')), (_('probe')), (_('beam')), (_('space')), (_('zoom')), (_('zap'))],
    (_('CASTLES')): [(_('tower')), (_('moat')), (_('stone')), (_('arch')), (_('court')), (_('king')), (_('queen')), (_('walls')), (_('draw')), (_('gate'))],
    (_('ISLANDS')): [(_('palm')), (_('sands')), (_('reef')), (_('coast')), (_('beach')), (_('sea')), (_('cove')), (_('boats')), (_('docks')), (_('tropic'))],
    (_('CLOWNS')): [(_('clown')), (_('mime')), (_('wig')), (_('mask')), (_('red')), (_('nose')), (_('balloon')), (_('laugh')), (_('joke')), (_('prank'))],
    (_('GHOSTS')): [(_('ghost')), (_('haunt')), (_('spook')), (_('ghoul')), (_('scare')), (_('crypt')), (_('eerie')), (_('fright')), (_('wail')), (_('chill'))],
    (_('CAVES')): [(_('stone')), (_('bats')), (_('rocks')), (_('dark')), (_('stalag')), (_('depth')), (_('troll')), (_('echo')), (_('gloom')), (_('vault'))],
    (_('ROBOTS')): [(_('servo')), (_('logic')), (_('cog')), (_('bolt')), (_('brain')), (_('cable')), (_('metal')), (_('tools')), (_('arm')), (_('gear'))],
    (_('TREES')): [(_('oak')), (_('pine')), (_('bark')), (_('leaves')), (_('roots')), (_('twig')), (_('shade')), (_('apple')), (_('fruit')), (_('moss'))],
    (_('WIZARDS')): [(_('magic')), (_('spell')), (_('cloak')), (_('staff')), (_('potion')), (_('witch')), (_('runes')), (_('charm')), (_('wand')), (_('books'))],
    (_('VOLCANO')): [(_('lava')), (_('smoke')), (_('ash')), (_('crust')), (_('rock')), (_('fire')), (_('erupts')), (_('earth')), (_('crack')), (_('magma'))],
    (_('DRAGONS')): [(_('scales')), (_('wings')), (_('fire')), (_('tail')), (_('claws')), (_('roar')), (_('flame')), (_('fangs')), (_('beast')), (_('lair'))],
    (_('MIRRORS')): [(_('glass')), (_('frame')), (_('look')), (_('shine')), (_('image')), (_('reflect')), (_('ghost')), (_('room')), (_('angle')), (_('clean'))],
    (_('FAIRIES')): [(_('pixie')), (_('tiny')), (_('wings')), (_('spark')), (_('magic')), (_('light')), (_('dust')), (_('charm')), (_('lore')), (_('elf'))],
    (_('MARKETS')): [(_('trade')), (_('stalls')), (_('fruit')), (_('value')), (_('goods')), (_('crowd')), (_('money')), (_('sales')), (_('deals')), (_('price'))],
    (_('TUNNELS')): [(_('earth')), (_('dark')), (_('shaft')), (_('mines')), (_('train')), (_('pipes')), (_('crawl')), (_('route')), (_('gates')), (_('dig'))]
}

css = """
        .green_button {
            background-color: @green_5;
            outline: 3px solid @green_5;
            outline-offset: -2px;
        }

        .red1 {
            background-color: @red_1;
        }

        .red2 {
            background-color: @red_2;
        }

        .red3 {
            background-color: @red_3;
        }

        .orange3 {
            background-color: @orange_3;
        }

        .purple2 {
            background-color: @purple_2;
        }

        .blue1 {
            background-color: @blue_1;
            color: black;
        }

        .blue2 {
            background-color: @blue_2;
        }

        .blue3 {
            background-color: @blue_3;
        }

        .blue4 {
            background-color: @blue_4;
        }

        .blue5 {
            background-color: @blue_5;
        }

        .yellow1 {
            background-color: @yellow_1;
            color: black;
        }

        .yellow2 {
            background-color: @yellow_2;
            color: black;
        }

        .yellow3 {
            background-color: @yellow_3;
            color: black;
        }

        .yellow4 {
            background-color: @yellow_4;
            color: black;
        }

        .green1 {
            background-color: @green_1;
            color: black;
        }

        .box {
          background-color: @borders;
          border: none;
        }

        .frame {
          border: none;
          background-color: @card_bg_color;
          border-radius: 10px;
        }

        .dim-label {
            opacity: 0.75;
            color: var(--window-fg-color);
        }

        .contrast-label {
            color: var(--window-fg-color);
            font-weight: bold;
        }

        .small_game {
            color: var(--accent-green);
        }

        .medium_game {
            color: var(--accent-yellow);
        }

        .large_game {
            color: var(--accent-red);
        }

        .custom {
            color: var(--accent-blue);
        }

        .shake {
            animation: shake_animation 0.35s ease;
        }

        .outline-red1 { outline: 3px solid @red_1; outline-offset: -2px;}
        .outline-red2 { outline: 3px solid @red_2; outline-offset: -2px;}
        .outline-red3 { outline: 3px solid @red_3; outline-offset: -2px;}
        .outline-orange3 { outline: 3px solid @orange_3; outline-offset: -2px;}
        .outline-purple2 { outline: 3px solid @purple_2; outline-offset: -2px;}
        .outline-blue1 { outline: 3px solid @blue_1; outline-offset: -2px;}
        .outline-blue2 { outline: 3px solid @blue_2; outline-offset: -2px;}
        .outline-blue3 { outline: 3px solid @blue_3; outline-offset: -2px;}
        .outline-blue4 { outline: 3px solid @blue_4; outline-offset: -2px;}
        .outline-blue5 { outline: 3px solid @blue_5; outline-offset: -2px;}
        .outline-yellow1 { outline: 3px solid @yellow_1; outline-offset: -2px;}
        .outline-yellow2 { outline: 3px solid @yellow_2; outline-offset: -2px;}
        .outline-yellow3 { outline: 3px solid @yellow_3; outline-offset: -2px;}
        .outline-yellow4 { outline: 3px solid @yellow_4; outline-offset: -2px;}
        .outline-green1 { outline: 3px solid @green_1; outline-offset: -2px;}

        @keyframes shake_animation {
            0% { transform: translateX(0px); background-color: @green_5;}
            20% { transform: translateX(-4px);}
            40% { transform: translateX(4px); background-color: @green_5;}
            60% { transform: translateX(-4px); }
            80% { transform: translateX(4px); background-color: @green_5;}
            100% { transform: translateX(0px); }
        }

        /* BottomSheet wordlist */
        grid.wrap-box > box.tag {
          background-color: color(srgb 0 0 0.0235294 / 0.08);
          border-radius: 99px;
          padding: 6px 12px;
          outline-color: rgba(0,0,6,0.8);
        }
"""
letters = {
    'en_US.UTF-8': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    'ru_RU.UTF-8': "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    'fr_FR.UTF-8': "AÀÂBCÇDEÈÉÊFGHIÎJKLMNOÔPQRSTUÙÛVWXYZ"
}

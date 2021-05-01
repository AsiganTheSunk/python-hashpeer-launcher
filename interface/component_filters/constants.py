import time
from typing import Any, Callable, List, Tuple

# lambda constant functions
DECORATE_OPT_SELECTION: Callable[[str, str, str, int, str], str] = \
    lambda h_char, t_char, text, n, space: f' {h_char}{DECORATE_OPT(text, n, space)}{t_char} '

DECORATE_OPT: Callable[[str, int, str], str] = \
    lambda text, n, space: f'{space * n}{text}{space * n}'

DEFAULT_OPT_TOOLTIP: Callable[[str, str, str], str] = \
    lambda filter_opt, filter_type, filter_category: f'{filter_category} Filter:\n - ' \
                                                     f'This will select the {filter_opt} {filter_type} ' \
                                                     f'configuration for the current search.'

DEFAULT_STRICT_TOOLTIP: Callable[[str, str], str] = \
    lambda filter_opt, filter_type: f'Strict Filter:\n - This will select the {filter_opt} {filter_type} ' \
                                    f'configuration for the current search.'

DEFAULT_OPTIONAL_TOOLTIP: Callable[[List[str], str, str], List[Tuple[str, str]]] = \
    lambda opt_filter, filter_type, filter_category: [
        (opt_filter[index], item)
        for index, item in enumerate(list(map(
            DEFAULT_OPT_TOOLTIP, [filter_type] * len(opt_filter), opt_filter, [filter_category] * len(opt_filter)
        )))
    ]

OLD_DEFAULT_TEXT_COLOR = '#80B1B5'
DEFAULT_TEXT_COLOR = '#87939A'
DEFAULT_SELECTED_TEXT_COLOR = 'white'
DEFAULT_DIMMED_TEXT_COLOR = '#BBBBBB'

DEFAULT_BUTTON_MOUSE_OVER = '#4F5254'
DEFAULT_SELECTED_TREE_VIEW = '#0D293E'
DEFAULT_MOUSE_OVER_OPTION_MENU = '#4B6EAF'

DEFAULT_NOTIFICATION_AND_SCROLLBAR_COLOR = '#4E5052'
DEFAULT_BACKGROUND_COLOR = '#3C3F41'
DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR = '#313335'
DEFAULT_DARK_BACKGROUND_COLOR = '#2B2B2B'
DEFAULT_DARK_BORDER = '#3C3F41'

DEFAULT_MOUSE_OVER_TAB = '#27292A'
DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB = '#747A80'
DEFAULT_SELECTED_UNDER_SCORE_TAB = '#4A88C7'

DEFAULT_MOUSE_OVER_BUTTON = '#4F5254'

DEFAULT_TITLE_BAR = '#3C3C3C'

#DEFAULT_BACKGROUND_COLOR_V2 = '#91B6CE'
#DEFAULT_BACKGROUND_COLOR_V4 = '#9CBFDE'
#DEFAULT_HIGHLIGHT_COLOR = 'LightSteelBlue1'
#DEFAULT_BACKGROUND_COLOR_V3 = '#848482'
#DEFAULT_BUTTON_COLOR = 'LightSteelBlue4'
#DEFAULT_ENTRY_BACKGROUND_COLOR = 'white'

DEFAULT_PAD_X = 1
DEFAULT_PAD_Y = 1

DEFAULT_INNER_PAD_X = 2
DEFAULT_INNER_PAD_Y = 2

DEFAULT_FONT_SIZE = 10
DEFAULT_FONT_STYLE = 'calibri'
DEFAULT_TOOLTIP_PLACEHOLDER = 'Tooptip: Text\n - Data: This does something!'

AUDIO_OPT = ['5.1', '7.1', 'Dolby Surround']
UPLOADER_FILM_OPT = ['RARBG']
UPLOADER_SHOW_OPT = ['RARBG']
UPLOADER_ANIME_OPT = ['Horrible Subs', 'RG Anime']
CODEC_OPT = ['x264', 'h264', 'x265']
CATEGORY_LABEL = DECORATE_OPT_SELECTION('<', '>', 'Category', 2, ' ')

print(CATEGORY_LABEL)
YEARS = [str(year) for year in range(1990, int(time.strftime("%Y")) + 1, 1)]

STRICT_SHOW = ['Season', 'Episode']
STRICT_FILM = ['Year']

SEASON_PATTERN = r'[0-9]{1,2}'
EPISODE_PATTERN = r'[0-9]{1,3}'
YEAR_PATTERN = r'[0-9]{4}'


DEFAULT_FILTER_LABELS = {
    'Category': {
        'Show': {
            'strict': {
                'Season': [SEASON_PATTERN, DEFAULT_STRICT_TOOLTIP('Season', 'filter')],
                'Episode': [EPISODE_PATTERN, DEFAULT_STRICT_TOOLTIP('Episode', 'filter')],
            },
            'opt': {
                'Audio': DEFAULT_OPTIONAL_TOOLTIP(AUDIO_OPT, 'Audio', 'Optional'),
                'Uploader': DEFAULT_OPTIONAL_TOOLTIP(UPLOADER_SHOW_OPT, 'Uploader', 'Optional'),
                'Year': YEARS
            }
        },
        'Film': {
            'strict': {
                'Year': [YEAR_PATTERN, DEFAULT_STRICT_TOOLTIP('Year', 'filter')]
            },
            'opt': {
                'Audio': DEFAULT_OPTIONAL_TOOLTIP(AUDIO_OPT, 'Audio', 'Optional'),
                'Uploader': DEFAULT_OPTIONAL_TOOLTIP(UPLOADER_FILM_OPT, 'Uploader', 'Optional'),
            }
        },
        'Anime': {
            'strict': {
                'Season': [SEASON_PATTERN, DEFAULT_STRICT_TOOLTIP('Season', 'filter')],
                'Episode': [EPISODE_PATTERN, DEFAULT_STRICT_TOOLTIP('Episode', 'filter')],
            },
            'opt': {
                'Audio': DEFAULT_OPTIONAL_TOOLTIP(AUDIO_OPT, 'Audio', 'Optional'),
                'Uploader': DEFAULT_OPTIONAL_TOOLTIP(UPLOADER_ANIME_OPT, 'Uploader', 'Optional'),
                'Year': YEARS,
            }
        }
    }
}


# if __name__ == '__main__':
#     import json
#     print(json.dumps(DEFAULT_FILTER_LABELS, sort_keys=True, indent=4))

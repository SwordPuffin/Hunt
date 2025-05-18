application_id = 'io.github.swordpuffin.hunt'

scalable_dir = 'hicolor' / 'scalable' / 'apps'
install_data(
  scalable_dir / ('@0@.svg').format(application_id),
  install_dir: get_option('datadir') / 'icons' / scalable_dir
)

symbolic_dir = 'hicolor' / 'symbolic' / 'apps'
install_data(
  symbolic_dir / ('@0@-symbolic.svg').format(application_id),
  install_dir: get_option('datadir') / 'icons' / symbolic_dir
)

actions_dir = 'hicolor' / 'scalable' / 'actions'
actions_icons = [
  actions_dir / 'external-link-symbolic.svg',
  actions_dir / 'wrench-wide-symbolic.svg',
  actions_dir / 'update-symbolic.svg',
  actions_dir / 'question-round-outline-symbolic.svg',
  actions_dir / 'dice3-symbolic.svg',
  actions_dir / 'camera-flash-symbolic.svg',
  actions_dir / 'playlist-infinite-symbolic.svg',
  actions_dir / 'timer-symbolic.svg',
  actions_dir / 'branch-compare-arrows-symbolic.svg',
  actions_dir / 'gamepad-symbolic.svg',
  actions_dir / 'lightbulb-symbolic.svg',
  actions_dir / 'gamepad-symbolic.svg',
  actions_dir / 'soup-symbolic.svg',
]
install_data(
  actions_icons,
  install_dir: get_option('datadir') / 'icons' / actions_dir
)
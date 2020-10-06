import os
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, images
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus down in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Move window up in current stack "),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Programs
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod, "shift"], "Return",
        lazy.spawn("dmenu_run"),
        desc="Launch dmenu"),
    Key([mod], "q",
        lazy.window.kill(),
        desc="Kill Focused Window"),
    Key([mod], "w",
        lazy.spawn("brave"),
        desc="Launch Brave"),
    Key([mod], "v",
        lazy.spawn(terminal+" -e nvim"),
        desc="Launch NVIM"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Qtile commands
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile")
]

groups = [Group(i) for i in "123"]

for i in groups:
    keys.extend([
        # mod4 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod4 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod4 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "#e1acff",
    "border_normal": "#1D2330"
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(**layout_theme),
    # layout.Zoomy(),
]

colors = [["#292d3e", "#292d3e"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name

widget_defaults = dict(
    font='Hack Regular Nerd Font Complete',
    fontsize=12,
    padding=3,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.TextBox(
                    text='⌨',
                    background=colors[0],
                    foreground=colors[3],
                    padding=0,
                    fontsize=10,
                    mouse_callbacks={
                        'Button1': lambda qtile: qtile.cmd_spawn('onboard')}
                ),
                widget.GroupBox(
                    fontsize=9,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[3],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.Sep(
                    linewidth=0,
                    padding=40,
                    foregaound=colors[2],
                    background=colors[0]
                ),
                widget.WindowName(
                    foreground=colors[6],
                    background=colors[0],
                    padding=0
                ),
                widget.TextBox(
                    text='',
                    background=colors[0],
                    foreground=colors[5],
                    padding=-7,
                    fontsize=40
                ),
                widget.TextBox(
                    text=" ⟳",
                    padding=2,
                    foreground=colors[2],
                    background=colors[5],
                    fontsize=14
                ),
                widget.Pacman(
                    update_interval=1800,
                    foreground=colors[2],
                    mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                        terminal + ' -e yay -Syu')},
                    background=colors[5]
                ),
                widget.TextBox(
                    text="Updates",
                    padding=5,
                    mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                        terminal + ' -e yay -Syu')},
                    foreground=colors[2],
                    background=colors[5]
                ),
                widget.TextBox(
                    text='',
                    background=colors[5],
                    foreground=colors[4],
                    padding=-7,
                    fontsize=40
                ),
                widget.Net(
                    interface="enp0s3",
                    format='{down} ↓↑ {up}',
                    foreground=colors[2],
                    background=colors[4],
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    background=colors[4],
                    foreground=colors[5],
                    padding=-7,
                    fontsize=40
                ),
                widget.TextBox(
                    text=" Vol:",
                    foreground=colors[2],
                    background=colors[5],
                    padding=0
                ),
                widget.Volume(
                    foreground=colors[2],
                    background=colors[5],
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    background=colors[5],
                    foreground=colors[4],
                    padding=-7,
                    fontsize=40
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors[0],
                    background=colors[4],
                    padding=0,
                    scale=0.7
                ),
                widget.CurrentLayout(
                    foreground=colors[2],
                    background=colors[4],
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    background=colors[4],
                    foreground=colors[5],
                    padding=-7,
                    fontsize=40
                ),
                widget.Clock(
                    foreground=colors[2],
                    background=colors[5],
                    format="%A, %B %d  [ %H:%M ]"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors[0],
                    background=colors[5]
                ),
                widget.Systray(
                    background=colors[0],
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors[0],
                    background=colors[5]
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'onboard'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

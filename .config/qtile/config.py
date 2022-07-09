# -*- coding: utf-8 -*-
import subprocess, os
from libqtile.layout.bsp import Bsp
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import Canta_dark

mod = "mod4"
terminal = guess_terminal()

keys = [
    #custom shurtcuts
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch web browser"),
    Key([mod], "z", lazy.spawn('librewolf'), desc="Launch private web browser"),
    Key([mod], "d", lazy.spawn("dmenu_run -fn Vazirmatn:size=9")),
    Key([mod], "s", lazy.spawn('gnome-screenshot'), desc="Take a screenshot"),
    Key([mod], "i", lazy.spawn('./backlight -i'), desc="Light Up"),
    Key([mod], "u", lazy.spawn('./backlight -d'), desc="Light Down"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "t", lazy.spawn('/home/rashed/Desktop/Telegram/Telegram -workdir /home/rashed/.local/share/TelegramDesktop/ -- %u'), desc="Launch telegram"),
    Key([mod], "o", lazy.spawn('obs'), desc="Launch obs studio"),
    Key([mod], "m", lazy.spawn('clementine'), desc="Launch music player"),
    Key([mod], "f", lazy.spawn('thunar'), desc="Launch file manager"),
    Key([mod], "v", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating mode"),
    Key([mod], "c", lazy.spawn('code'), desc="Launch visual studio code"),
    Key([mod], "e", lazy.spawn('env GTK_IM_MODULE=cedilla /home/rashed/eclipse/embedcpp-2022-06/eclipse/eclipse'), desc="Launch eclipse ide"),
    Key([mod, "shift"], "v", lazy.spawn('pavucontrol'), desc="Launch volume"),


    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.spawn('reboot'), desc="Restart System"),
    Key([mod, "shift"], "p", lazy.spawn('poweroff'), desc="Shutdown System"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
   # Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
    #    dmenu_prompt=">",
     #   dmenu_font="sans",
      #  background="#15181a",
       # foreground="#00ff00",
        #selected_background="#079822",
       # selected_foreground="#fff",
      #  dmenu_height=24,  # Only supported by some dmenu forks
     #))),
]



groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    Bsp(
        border_focus=Canta_dark["Focus Decoration"],
        border_normal=Canta_dark["Button Background"],
        margin=5,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='FantasqueSansMono Nerd Font',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    fontsize=16,
                ),
                widget.GroupBox(
                    fontsize=16,
                ),
                widget.Prompt(
                    fontsize=16,
                ),
                widget.WindowName(
                    fontsize=16,
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ffac00", "#999999"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CPU(
                    format=' {load_percent}%',
                    fontsize=16,
                ),
                widget.Memory(
                    format='{MemUsed: .0f}{mm}{MemTotal: .0f}{mm}',
                    fontsize=16,
                ),
                widget.Battery(
                    format='  {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
                    fontsize=16,
                ),
                widget.Systray(),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    fontsize=16,
                ),
            ],
            background=Canta_dark["Hide Background"],
            size=24,
            opacity=0.8,
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
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
wl_input_rules = None
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

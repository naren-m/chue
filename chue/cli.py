#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import click
import phue

import utils

BRIDGE_IP = "10.0.1.2"


def action_on_light_by_id(bridge, light_id, action):
    """
    Action on one light by light_id.
    """
    if action == 'on':
        bridge.set_light(light_id, 'on', True)
    elif action == 'off':
        bridge.set_light(light_id, 'on', False)
    elif action == 'toggle':
        current_state = bridge.get_light(light_id, 'on')
        bridge.set_light(light_id, 'on', not current_state)
    click.secho(
        'Turning  %s light %s!' % (bridge.get_light(light_id, 'name'),
                                   get_state(not current_state)),
        fg='green')

    return


def valid_id(id):
    if id == "" or id is None:
        click.secho('Invalid device id', fg='red')
        return False
    return True


def get_state(state_bool):
    state = None
    if state_bool:
        state = "on"
    else:
        state = "off"

    return state


@click.group()
def main():
    pass


@main.command(name="lights")
@click.option('--id', help='ID of light.')
@click.option('--all', help='All lights.', default=False, is_flag=True)
@click.option(
    '--connect', help='Connect to hue bridge.', default=False, is_flag=True)
@click.option('--info', help='Details of light.', default=False, is_flag=True)
@click.option(
    '--action',
    type=click.Choice(['on', 'off', 'toggle']),
    help='Runs the specified action on light(s)')
@click.option('--bri', help='Increase/Decrease brightness of light(s).')
def lights(id, all, connect, info, action, bri):
    """
    Actions to control hue lights
    """
    try:
        bridge = phue.Bridge(BRIDGE_IP)
    except Exception:
        click.secho(
            "Press the bridge buttom and call the connect again", fg='red')

    if connect:
        # If the app is not registered and the button is not pressed,
        # press the button and call connect()
        # (this only needs to be run a single time)
        try:
            bridge = phue.Bridge(BRIDGE_IP)
        except Exception:
            click.secho(
                "Press the bridge buttom and call the connect again", fg='red')
        else:
            click.secho("Already connected", fg='green')

        return

    if info:
        # TODO: Print details of all lights
        click.secho('Light details', fg='green')
        for l in bridge.lights:

            click.secho(
                '\t %d: %s is %s' % (l.light_id, l.name, get_state(l.on)),
                fg='green')

    if all:
        # TODO: Add api to Run action on all
        click.secho('TODO ADD: Run action on all', fg='green')
        for l in bridge.lights:
            action_on_light_by_id(bridge, l.light_id, action)

    else:
        if not valid_id(id):
            return
        action_on_light_by_id(bridge, int(id), action)


if __name__ == '__main__':
    main()
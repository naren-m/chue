#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import click
import utils


def print_details_of_light_by_id(light_id):
    status, light = h.getLightDetails(light_id)
    if status != 200:
        click.secho('Failed to get light with id %s!' % id, fg='red')
    utils.print_json_obj(light)


def action_on_light_by_id(light_id, action):
    """
    Action on one light by light_id.
    """
    if action == h.STATE_ON:
        h.turn(light_id, h.STATE_ON)
    elif action == h.STATE_OFF:
        h.turn(light_id, h.STATE_OFF)
    elif action == 'toggle':
        h.toggle(light_id)

    click.secho('Turning %s light %s!' % (light_id, action), fg='green')

    return


def valid_id(id):
    if id == "" or id is None:
        click.secho('Invalid device id', fg='red')
        return False
    return True


@click.group()
def main():
    pass


@main.command(name="lights")
@click.option('--id', help='ID of light.')
@click.option('--all', help='All lights.', default=False, is_flag=True)
@click.option('--info', help='Details of light.', default=False, is_flag=True)
@click.option(
    '--action',
    type=click.Choice(['on', 'off', 'toggle']),
    help='Runs the specified action on light(s)')
def lights(id, all, info, action):
    """
    Actions to control hue lights
    """
    if all:
        # TODO: Add api to Run action on all
        click.secho('TODO ADD: Run action on all', fg='green')
        if info:
            # TODO: Print details of all lights
            click.secho('TODO: Print details of all lights', fg='green')
    else:
        if not valid_id(id):
            return

        action_on_light_by_id(id, action)

        if info:
            # Print details of one light
            click.secho('Print details of one light', fg='green')
            print_details_of_light_by_id(id)


if __name__ == '__main__':
    main()
import dearpygui.dearpygui as dpg
import uitheme
import asyncio
import pyrcrack
import sys
import wlanutils
from enum import Enum

print("Creating window context")
dpg.create_context()

global dpgWindowStack
dpgWindowStack = [] #Clear array

def setMonIface(sender, app_data, user_data):
    print("Setting monitor interface to " + app_data)
    global monIface
    monIface = app_data

def testInterface(sender, app_data, user_data):
    print("Testing monitor interface...")
    print(monIface)
    success = asyncio.run(wlanutils.testMonInterface(monIface))
    if (success):
        print("Exiting monitor mode on " + monIface)

def bringUpInterfaceSetup():
    print("Bringing up interface setup")
    if(1):
        availableInterfaces = asyncio.run(wlanutils.getInterfaces())
        with dpg.window(label="Monitor Interface Setup", pos=(0, 0), width=300, height=320) as wIfaceSetup:
            dpgWindowStack.append(wIfaceSetup)
            dpg.add_text(default_value="Select 80211 monitor interface")
            dpg.add_radio_button(items=availableInterfaces, callback=setMonIface)
            b1 = dpg.add_button(label="Test interface", callback=testInterface)
            dpg.add_text(default_value="Output Log")
            with dpg.child_window(height=170) as outputLogWindow:
                global ifaceSetupOutputLogWindow
                ifaceSetupOutputLogWindow = outputLogWindow
                dpg.add_text(default_value="")

def bringUpDeauthAgentWindow():
    print("Bringing up deauth agent")
    if(1):
        with dpg.window(label="Deauth Agent", pos=(300,0), width=450, height=320) as wDeauthAgent:
            dpgWindowStack.append(wDeauthAgent) #Add the window to the window stack
            with dpg.tab_bar(label="tb1") as tb1:
                with dpg.tab(label="Targets"):
                    dpg.add_text(default_value="Enter a station's mac address:")
                    dpg.add_input_text(hint="aa:bb:cc:dd:ee:ff")
                with dpg.tab(label="Access Points"):
                    dpg.add_text(default_value="APs")

def defaultLayout():
    print("Layout: Default")
    bringUpInterfaceSetup()
    bringUpDeauthAgentWindow()

def bringUpStyleEditor():
    dpg.show_style_editor()

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save device list")
    with dpg.menu(label="Actions"):
        dpg.add_menu_item(label="Interface Setup", callback=bringUpInterfaceSetup)
        dpg.add_menu_item(label="Deauth Agent", callback=bringUpDeauthAgentWindow)
    with dpg.menu(label="View"):
        with dpg.menu(label="Layouts"):
            dpg.add_menu_item(label="Default Layout", callback=defaultLayout)
    with dpg.menu(label="Development"):
        dpg.add_menu_item(label="Dear PyGui Style Editor", callback=bringUpStyleEditor)

uitheme.setBaseColorTheme()
defaultLayout()

dpg.create_viewport(title='Phoenix', width=1280, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
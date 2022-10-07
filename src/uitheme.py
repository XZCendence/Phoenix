import dearpygui.dearpygui as dpg




#baseThemeColor = (230,150,10)  #True Yellow
#baseThemeColor = (255,100,0)   #Red-Orange
baseThemeColor=(200, 0, 255)    #Purple

#Set up a global theme using the base color
def setBaseColorTheme():
    with dpg.theme() as theme_monochrome:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Border, baseThemeColor, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (baseThemeColor[0]*0.25, baseThemeColor[1]*0.25, baseThemeColor[2]*0.25), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, baseThemeColor, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, baseThemeColor, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, baseThemeColor, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Tab, baseThemeColor + (100, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, baseThemeColor + (25,0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, baseThemeColor + (100,0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, baseThemeColor , category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, baseThemeColor + (100, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, baseThemeColor + (140, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, baseThemeColor + (255, 0), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, baseThemeColor , category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0,0,0,0) , category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (baseThemeColor[0]*0.25, baseThemeColor[1]*0.25, baseThemeColor[2]*0.25) + (150,0) , category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg,(baseThemeColor[0]*0.25, baseThemeColor[1]*0.25, baseThemeColor[2]*0.25) + (150,0) , category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg,(baseThemeColor[0]*0.25, baseThemeColor[1]*0.25, baseThemeColor[2]*0.25) + (230,0) , category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(theme_monochrome)
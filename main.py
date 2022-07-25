from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# Init airtest and connect to android device via adb.
if not cli_setup():
    # auto_setup(__file__, logdir=None, devices=["Android:///",], project_root="PUT_ROOT_HERE")
    auto_setup(__file__, logdir=None, devices=["Android:///"])

# Init poco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# This method shows how to use the __iter__ method to set up a generator which we iterate through.
# Makes it simple to deal with multiple matches.
def find_promos():
    if frozen_poco("com.razer.cortex:id/tv_progress").exists():
        obj_gen = frozen_poco("com.razer.cortex:id/tv_progress").__iter__()
        for matches in obj_gen:
            if matches.get_text() != r'CLAIMED':
                label_text = matches.get_text().encode("utf-8")
                print(f'Found {label_text} quest card. Clicking')
            match_text = matches.get_text().encode('utf-8')
            print(match_text)
            if match_text == 'WATCH':
                matches.click()
                print(f'WATCH keyword found in quest cards. Clicking')
            if match_text == ('CLAIM'):
                print(f'CLAIM keyword found in quest cards. Clicking')
                matches.click()
                return   # We only need to click one card so return.

# Drive it like you stole it
while True:

    # Utilize freeze() to snapshot UI hierarchy making searching through it for multiple items much faster. We only
    # need 1 snapshot per pass unless a screen element changes mid-pass.
    with poco.freeze() as frozen_poco:
        
        find_promos()
        
        if frozen_poco("com.razer.cortex:id/tv_tooltip_body").exists():
            frozen_poco("com.razer.cortex:id/tv_tooltip_body").click()
        
        # Open daily quest cards 1st step
        if frozen_poco("com.razer.cortex:id/open_button").exists():
            frozen_poco("com.razer.cortex:id/open_button").click()
            print('com.razer.cortex:id/open_button')
            
        # Open daily quest cards 2nd step
        if frozen_poco("com.razer.cortex:id/btn_open_now").exists():
            frozen_poco("com.razer.cortex:id/btn_open_now").click()
            print('com.razer.cortex:id/btn_open_now')
            
        # Daily quest cards
        if frozen_poco("com.razer.cortex:id/btn_dqc_view_go").exists():
            frozen_poco("com.razer.cortex:id/btn_dqc_view_go").click()
            print('razer.cortex:id/btn_dqc_view_go')
        
        # Level up pop up
        if frozen_poco("com.razer.cortex:id/btn_black_positive_button").exists():
            frozen_poco("com.razer.cortex:id/btn_black_positive_button").click()
            print('com.razer.cortex:id/btn_black_positive_button')
        
        # Close video ad method 1
        if frozen_poco("com.razer.cortex:id/ia_tv_close_button").exists():
            frozen_poco("com.razer.cortex:id/ia_tv_close_button").click()
            print('com.razer.cortex:id/ia_tv_close_button')
            
        # Close video ad method 2
        if frozen_poco("close-icon").exists():
            frozen_poco("close-icon").click()
            print('close-icon')
        
        # Get ad time remaining
        if frozen_poco("ia_tv_remaining_time").exists():
            time_left = frozen_poco("ia_tv_remaining_time").get_text()
            print(f'Ad playing. Time remaining: {time_left}')
                    
        # Start watching ad    
        if frozen_poco("com.razer.cortex:id/btn_watch").exists():
            frozen_poco("com.razer.cortex:id/btn_watch").click()
            print('com.razer.cortex:id/btn_watch_ad')
        
        # Continue button
        if frozen_poco("com.razer.cortex:id/btn_positive").exists():
            frozen_poco("com.razer.cortex:id/btn_positive").click()
            print('com.razer.cortex:id/btn_positive')

        # Claim button
        if frozen_poco("com.razer.cortex:id/btn_claim").exists():
            frozen_poco("com.razer.cortex:id/btn_claim").click()
            print('com.razer.cortex:id/btn_claim')

        print(frozen_poco("com.razer.cortex:id/btn_green").get_text().encode('utf-8'))
        # Doesn't work properly. Need to revisit this.'
        if frozen_poco("com.razer.cortex:id/btn_green").get_text().encode('utf-8') == 'CLAIM':
        # if frozen_poco("com.razer.cortex:id/btn_green").exists():
            if frozen_poco("com.razer.cortex:id/btn_green").get_text().encode('utf-8') == 'CLAIM':
                frozen_poco("com.razer.cortex:id/btn_green").click()
                print('com.razer.cortex:id/btn_green text = CLAIM. Clicking.')
        
        # Another pop up claim button
        if frozen_poco("com.razer.cortex:id/btn_green_positive_button").exists():
            frozen_poco("com.razer.cortex:id/btn_green_positive_button").click()
            print('com.razer.cortex:id/btn_green_positive_button')
            
        # Closes window asking for Google Play Review
        if frozen_poco("com.razer.cortex:id/subtitle").exists():
            if frozen_poco("com.razer.cortex:id/subtitle").get_text() == 'SEND US FEEDBACK ON GOOGLE PLAY STORE':
                keyevent("BACK")
                print(f'com.razer.cortex:id/subtitle.get_text() = {frozen_poco("com.razer.cortex:id/subtitle").get_text()}')

        if frozen_poco("android.view.View").offspring("android.widget.Button").exists():
            frozen_poco("android.view.View").offspring("android.widget.Button").click()
            print('android.view.View.offspring .. android.widget.Button')





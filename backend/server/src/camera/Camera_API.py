from amcrest import AmcrestCamera
import requests
import re

class Camera_API(object):
    def __init__(self, host, user='default', password='default', port=80):
        self.camera = AmcrestCamera(host, port, user, password).camera
        self.camera.modify_password('admin','newpass','default')
        self.change_ip('192.168.1.20')

    def change_ip(self, new_ip, subnet_mask='255.255.255.0'):
        ret = self.camera.command(
            'configManager.cgi?action=setConfig&Network.interface.IPAddress={new_ip}&Network.interface.SubnetMask={subnet_mask}'.format(
                new_ip=new_ip, subnet_mask=subnet_mask,
            ))
        self.camera._host = new_ip
        return ret.content.decode('utf-8')

    def set_dhcp(self, dhcp_enable):
        ret = self.camera.command(
            'configManager.cgi?action=setConfig&Network.interface.DhcpEnable={dhcp_enable}'.format(
                dhcp_enable=dhcp_enable,
            ))
        return ret.content.decode('utf-8')

    def set_time(self,):
        ret = self.camera.command(
        'global.cgi?action=setCurrentTime&time=2016-01-01%2021:02:32'
        )
        return ret.content.decode('utf-8')

    def set_focus(self, scale):
        ret = self.camera.command(
        'devVideoInput.cgi?action=adjustFocus&focus={scale}'.format(
        scale=scale,
        ))
        return ret.content.decode('utf-8')

    def set_zoom(self, scale):
        ret = self.camera.command(
        'devVideoInput.cgi?action=adjustFocus&zoom={scale}'.format(
        scale=scale,
        ))
        return ret.content.decode('utf-8')

    def auto_focus(self):
        ret = self.camera.command(
        'devVideoInput.cgi?action=autoFocus'
        )
        return ret.content.decode('utf-8')

    def ptz_command(self, code, move_speed=3):
        moves = ['Up', 'Down', 'Left', 'Right']
        zooms = ['ZoomWide', 'ZoomTele', 'FocusNear', 'FocusFar']
        # ZoomWide = Zoom out        ZoomTele = Zoom in
        code_sensitive = re.findall(code, str(moves + zooms), re.IGNORECASE)
        
        if code_sensitive in zooms:
            arg1,arg2,arg3 = 0
        elif code_sensitive in moves:
            arg1,arg3 = 0
            arg2 = move_speed
        else:
            return

        ret = self.camera.command(
        'ptz.cgi?action=start&channel=0&code={code}&arg1={arg1}&arg2={arg2}&arg3={arg3}'.format(
        code=code_sensitive, arg1=arg1, arg2=arg2, arg3=arg3,
        ))
        return ret.content.decode('utf-8')

    def move_up(self):
        return self.ptz_command('Up')
    def move_down(self):
        return self.ptz_command('Down')
    def move_left(self):
        return self.ptz_command('Left')
    def move_right(self):
        return self.ptz_command('Right')
    def zoom_in(self):
        return self.ptz_command('ZoomTele')
    def zoom_out(self):
        return self.ptz_command('ZoomWide')

    def software_information(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getSoftwareVersion'
        )
        swinfo = ret.content.decode('utf-8')
        if ',' in swinfo:
            version, build_date = swinfo.split(',')
        else:
            version, build_date = swinfo.split()
        return (version, build_date)

    def hardware_version(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getHardwareVersion'
        )
        return ret.content.decode('utf-8')

    def device_type(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getDeviceType'
        )
        return ret.content.decode('utf-8')

    def serial_number(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getSerialNo'
        )
        return ret.content.decode('utf-8').split('=')[-1]

    def machine_name(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getMachineName'
        )
        return ret.content.decode('utf-8')

    def system_information(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getSystemInfo'
        )
        return ret.content.decode('utf-8')

    def vendor_information(self):
        ret = self.camera.command(
            'magicBox.cgi?action=getVendor'
        )
        return ret.content.decode('utf-8')

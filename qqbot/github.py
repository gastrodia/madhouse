# -*- coding: utf-8 -*-
import subprocess
def onQQMessage(bot, contact, member, content):
    if 'exec:' in content:
        project_uri = content.split(':')[1].strip()
        git_repo = 'https://github.com/' + project_uri + '.git'
        project_name =  content.split('/')[1].strip();
        cmd = 'git clone ' + git_repo + '& cd ' + project_name + '& exec;'
        print(cmd)
        output = subprocess.check_output(cmd,shell=True) 
        subprocess.check_output('rm ' + project_name + ' -rf',shell=True)        
        print(output)
        # proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        # stdout, stderr = proc.communicate('dir c:\\')
        # stdout
        bot.SendTo(contact, output)
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
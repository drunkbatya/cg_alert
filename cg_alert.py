import requests;
import datetime;
import sys;

def sendtext(bot_msg):
	bot_token = 'TOCKEN';
	bot_chatID = 'ID';
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_msg;
	response = requests.get(send_text);
	return response.json();

now = datetime.datetime.now();

header = "Centrogas Office LAN Alert BOT.\n\n";
footer = "\n\nWritten by DrunkBatya.\n";

msg_oracle = header + "Warning!\nCG ORACLE server doesn't reply to ping!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;
msg_asterisk = header + "Warning!\nCG Asterisk VOIP server doesn't reply to ping!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;
msg_cctv = header + "Warning!\nCG CCTV server doesn't reply to ping!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;
msg_ser = header + "Warning!\nCG Samba file storage doesn't reply to ping!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;
msg_www = header + "Warning!\nCG WWW server doesn't reply to ping!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;
msg_reboot = header + "Critical ERROR!\nCG Core GateWay was rebooted from re0 down!!\n\nDate: " + now.strftime("%d-%m-%Y %H:%M") + footer;

if (sys.argv[1] == "ora"):
	sendtext(msg_oracle);
elif (sys.argv[1] == "www"):
	sendtext(msg_www);
elif (sys.argv[1] == "ser"):
	sendtext(msg_ser);
elif (sys.argv[1] == "asterisk"):
	sendtext(msg_asterisk);
elif (sys.argv[1] == "cctv"):
	sendtext(msg_cctv);
elif (sys.argv[1] == "reboot"):
	sendtext(msg_reboot);

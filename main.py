import os
from datetime import datetime as dt
import pandas as pd
from pyautogui import click, locateOnScreen as los
from getChannelName import get_channel_name


excelFilePath = 'resources/bonusChannelPointsTracking.xlsx'


def channelPointsGoBrrrr():
	bonusPointsSymbolLocation = los('resources/button.png', confidence=0.9)
	if bonusPointsSymbolLocation is not None:
		click(bonusPointsSymbolLocation[0], bonusPointsSymbolLocation[1])
		return 0
	else:
		return 1


try:
	while True:
		if os.path.exists(excelFilePath):
			xlFile = pd.read_excel(excelFilePath)
			channelName = get_channel_name()
			# print(channelName)
			if channelName not in xlFile['Channel'].values:
				# print("1")
				new_channel = pd.DataFrame({'Channel': [channelName], 'Times button clicked': 0, 'Points gained': 0,
				                            'Last updated at': 0})
				xlFile = pd.concat([xlFile, new_channel], ignore_index=True)
				xlFile.to_excel(excelFilePath, index=False)
				if channelPointsGoBrrrr() == 0:
					# print("1.1")
					xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] = \
						xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] + 1
					xlFile.loc[xlFile['Channel'] == channelName, 'Points gained'] = \
						xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] * 50
					xlFile.loc[xlFile['Channel'] == channelName, 'Last updated at'] = dt.now()
					xlFile.to_excel(excelFilePath, index=False)
			else:
				# print("2")
				if channelPointsGoBrrrr() == 0:
					xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] = \
						xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] + 1
					xlFile.loc[xlFile['Channel'] == channelName, 'Points gained'] = \
						xlFile.loc[xlFile['Channel'] == channelName, 'Times button clicked'] * 50
					xlFile.loc[xlFile['Channel'] == channelName, 'Last updated at'] = dt.now()
					xlFile.to_excel(excelFilePath, index=False)
		else:
			df = pd.DataFrame(data={'Channel': [], 'Times button clicked': [], 'Points gained': [], 'Last updated at': []})
			df.to_excel(excelFilePath)

except KeyboardInterrupt:
	print("Finished program execution")

from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RyouToppaAssets: 


	# Click Rule Assets
	# 选择第一个寮 
	C_SELECT_FIRST_RYOU = RuleClick(roi_front=(1148,138,21,22), roi_back=(1148,138,21,22), name="select_first_ryou")


	# Image Rule Assets
	# 寮突 
	I_RYOU_TOPPA = RuleImage(roi_front=(1191,352,78,116), roi_back=(1191,352,78,116), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_ryou_toppa.png")
	# 寮突选择阴阳寮按钮 
	I_SELECT_RYOU_BUTTON = RuleImage(roi_front=(560,577,156,46), roi_back=(560,577,156,46), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_select_ryou_button.png")
	# 开始寮突按钮 
	I_START_TOPPA_BUTTON = RuleImage(roi_front=(812,497,171,55), roi_back=(812,497,171,55), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_start_toppa_button.png")
	# 寮击破奖励 
	I_RYOU_REWARD = RuleImage(roi_front=(134,417,241,40), roi_back=(134,417,241,40), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_ryou_reward.png")
	# 勋章奖励标题 
	I_GUILD_ORDERS_REWARDS = RuleImage(roi_front=(1123,31,115,56), roi_back=(1123,31,115,56), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_guild_orders_rewards.png")
	# 攻破阴阳寮 
	I_SUCCESS_PENETRATION = RuleImage(roi_front=(206,149,100,100), roi_back=(206,149,100,100), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_success_penetration.png")
	# 个人突破刷新按钮 
	I_REAL_RAID_REFRESH = RuleImage(roi_front=(963,569,174,60), roi_back=(963,569,174,60), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_real_raid_refresh.png")


	# Ocr Rule Assets
	# 寮突破进攻机会数 
	O_NUMBER = RuleOcr(roi=(271,560,48,31), area=(271,560,48,31), mode="DigitCounter", method="Default", keyword="", name="number")



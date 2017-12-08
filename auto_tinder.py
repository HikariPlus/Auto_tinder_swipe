# -*- coding: utf-8 -*-

# Tinderで自動右スワイプするためのコード
# 2017/12/8: Hikariplus

import pynder
import sys

#Facebookから閲覧したTinderのユーザID
usrid = "your_fb_id" #FacebookのID(findmyfbid.comで取得)
token = "your_fb_token" # アクセストークン(tinder_auth_fetcherで取得)

session = pynder.Session(facebook_id = usrid, facebook_token = token) # Tinderアカウントへのログイン
users = session.nearby_users() #近くに居るユーザの情報を取得

print "右スワイプ可能な回数：",session.likes_remaining

for usr in users:
    if session.likes_remaining == 0:
        print "右スワイプ終わり！"
        break
    #顔写真以外のプロフィール情報を表示
    print "======================================"
    print usr.name,"||",usr.age
    print usr.gender
    print usr.schools
    print usr.jobs
    print usr.bio
    print "======================================"
    if usr.gender=="male":　#自分の性的嗜好に合わせてフィルタを設定
        usr.dislike() # 左スワイプ
    else:
        usr.like() # 右スワイプ
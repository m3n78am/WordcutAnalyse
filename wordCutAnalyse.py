#!/usr/bin/env python
# -*- coding: utf8 -*-


import os
import sys
import json

from flask import Flask,Blueprint,request
import logging,logging.handlers



WordCutAnalyse = Blueprint('WordCutAnalyse',__name__)

currentPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(currentPath + "/../../app")

import jiebav2
import jiebav2.posseg

# 常用词库
jiebav2.load_userdict("../../app/dict/brands.dic")
jiebav2.load_userdict("../../app/dict/goods.dic")
jiebav2.load_userdict("../../app/dict/idiom.dic")
jiebav2.load_userdict("../../app/dict/product.dic")
jiebav2.load_userdict("../../app/dict/pre_product.dic")
jiebav2.load_userdict("../../app/dict/word.dic")
jiebav2.load_userdict("../../app/dict/userdict.dic")

logPath = currentPath + "/logs/wordCutAnalyse.log"

fileHandler = logging.handlers.RotatingFileHandler(logPath,mode="a",encoding="utf8",delay=False,maxBytes = 100 * 1024 * 1024,backupCount= 5)

fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)sd]'))
fileHandler.setLevel(logging.DEBUG)
logger = logging.getLogger('root')
logger.addHandler(fileHandler)

@WordCutAnalyse.route('/wordcut_analyse/',methods=['GET'])
def wordcut_analyse():

	logger.info(request)

	if "query_str" not in request.args:
		return "lack of parameter [?query_str=<>]"
	else:
		resultDict = {}
		i = 1
		query_str = request.args.get("query_str")
		words = jiebav2.posseg.cut(query_str)
		words = [(w.word,w.flag) for w in words]
		#for x in words:
		#	print x[0].encode("utf8") + "\t" + x[1].encode("utf8")

		for x in words:
			resultDict[i] = x[0] + " <=> " + x[1]
			i += 1

		return json.dumps(resultDict)
		#return json.dumps(dict([(w[0],w[1]) for w in words]))

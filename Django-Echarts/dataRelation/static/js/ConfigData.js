var ConfigData = {
	CreateDataOfInvestmentRelatio:function(option_,companyDict_,companyName_) {
		createLegendData = []
		createCategories = []
		createNodes = []
		createLinks = []

		tmpNodeObj = {}
		tmpNodeObj.category = 0;
		tmpNodeObj.name = companyName;
		tmpNodeObj.value = 10;
		tmpNodeObj.label = companyName+'\n'+'（公司）'
		createNodes.push(tmpNodeObj)

		tmpCategoryObj = {}
		tmpCategoryObj.name = '公司'
		createCategories.push(tmpCategoryObj)
		
		totalStyleOfGetStock = 1;
		for(style in companyDict){
			createLegendData.push(style)
			tmpobj = {}
			tmpobj.name = style
			createCategories.push(tmpobj)
			//获取到这一类型下的所有的公司名称，及数组。
			styleArray = companyDict[style]
			for (var i = 0; i < styleArray.length; i++) {
				nodeObj = {}
				nodeObj.category = totalStyleOfGetStock
				nodeObj.name = styleArray[i]
				nodeObj.value = totalStyleOfGetStock
				createNodes.push(nodeObj)

				linkObj = {}
				linkObj.source = styleArray[i]
				linkObj.target = companyName
				linkObj.weight = totalStyleOfGetStock
				linkObj.name = style

				createLinks.push(linkObj)
			}
			totalStyleOfGetStock  = totalStyleOfGetStock + 1

		}
		option_.legend = {
				        x: 'left',
				        data:createLegendData
				    };
		option_.series = [
				        {
				            type:'force',
				            name : "投资关系",
				            ribbonType: false,
				            categories : createCategories,
				            itemStyle: {
				                normal: {
				                    label: {
				                        show: true,
				                        textStyle: {
				                            color: '#333'
				                        }
				                    },
				                    nodeStyle : {
				                        brushType : 'both',
				                        borderColor : 'rgba(255,215,0,0.4)',
				                        borderWidth : 1
				                    },
				                    linkStyle: {
				                        type: 'curve'
				                    }
				                },
				                emphasis: {
				                    label: {
				                        show: false
				                    },
				                    nodeStyle : {
				                        //r: 30
				                    },
				                    linkStyle : {}
				                }
				            },
				            useWorker: false,
				            minRadius : 15,
				            maxRadius : 25,
				            gravity: 1.1,
				            scaling: 1.1,
				            roam: 'move',
				            nodes:createNodes,
				            links : createLinks
				        }
				    ];
				    
		return option_;
	},

	CreateDataOfKeyHotWords:function(option_,companyName_,keyWordsArray_){
		createCategories = []
		createNodes = []
		createLinks = []
		createLegendData = []

		companyName = companyName_
		keyWordsArray = keyWordsArray_

		tmpNodeObj = {}
		tmpNodeObj.category = 0
		tmpNodeObj.name = companyName
		tmpNodeObj.value =10
		tmpNodeObj.label = companyName + '\n' + '(公司)'
		createNodes.push(tmpNodeObj)
		
		for(i in keyWordsArray){
			word = keyWordsArray[i]
			tmpNodeObj = {}
			tmpNodeObj.name = word
			tmpNodeObj.value = 8
			createNodes.push(tmpNodeObj)
			tmpLinkObj = {}
			tmpLinkObj.source = companyName
			tmpLinkObj.target = word
			tmpLinkObj.weight = 10
			tmpLinkObj.name = word
			createLinks.push(tmpLinkObj)
		}
		option_.legend = {
				        x: 'left',
				        data:createLegendData
				    };
		option_.series = [
				        {
				            type:'force',
				            name : "关键热词",
				            ribbonType: false,
				            categories : createCategories,
				            itemStyle: {
				                normal: {
				                    label: {
				                        show: true,
				                        textStyle: {
				                            color: '#333'
				                        }
				                    },
				                    nodeStyle : {
				                        brushType : 'both',
				                        borderColor : 'rgba(255,215,0,0.4)',
				                        borderWidth : 1
				                    },
				                    linkStyle: {
				                        type: 'curve'
				                    }
				                },
				                emphasis: {
				                    label: {
				                        show: false
				                    },
				                    nodeStyle : {
				                        //r: 30
				                    },
				                    linkStyle : {}
				                }
				            },
				            useWorker: false,
				            minRadius : 15,
				            maxRadius : 25,
				            gravity: 1.1,
				            scaling: 1.1,
				            roam: 'move',
				            nodes:createNodes,
				            links : createLinks
				        }
				    ];
				    
		return option_;
	},

	CreateDataOfManagersOfCompany:function(option_,companyName_,directorsOfCompany_,executivesOfCompany_) {
		// 初始化一些基本信息，包括公司，董事会，和高管三个节点。
		createCategories = []
		createNodes = []
		createLinks = []
		createLegendData = []
		// 记录每一个职务对应的index，这样省的以后每次都查找。
		dictOfCategories = new Array()
		numOfPost = 1

		companyName = companyName_
		directorsOfCompany = directorsOfCompany_
		executivesOfCompany = executivesOfCompany_

		tmpCategoryObj = {}
		tmpCategoryObj.name = '公司'
		createCategories.push(tmpCategoryObj)

		tmpNodeObj = {}
		tmpNodeObj.category = 0
		tmpNodeObj.name = companyName
		tmpNodeObj.value =10
		tmpNodeObj.label = companyName + '\n' + '(公司)'
		createNodes.push(tmpNodeObj)

		tmpNodeObj1 = {}
		tmpNodeObj1.name = '董事会'
		tmpNodeObj1.value =10
		createNodes.push(tmpNodeObj1)

		tmpNodeObj2 = {}
		tmpNodeObj2.name = '高管'
		tmpNodeObj2.value =10
		createNodes.push(tmpNodeObj2)

		tmpLinkObj = {}
		tmpLinkObj.source = companyName
		tmpLinkObj.target ='董事会'
		tmpLinkObj.weight = 10
		tmpLinkObj.name = '董事会信息'
		createLinks.push(tmpLinkObj)

		tmpLinkObj1 = {}
		tmpLinkObj1.source = companyName
		tmpLinkObj1.target ='高管'
		tmpLinkObj1.weight = 10
		tmpLinkObj1.name = '高管信息'
		createLinks.push(tmpLinkObj1)
		
		for(name in directorsOfCompany){
			postArray = directorsOfCompany[name]
			// console.log(name)

			linkName = ''
			for ( i in postArray){
				postName = postArray[i]
				linkName = linkName + ' '+postName
				// console.log(postName)
				var index
				if (postName in dictOfCategories) {
					index = dictOfCategories[postName]
				}
				else{
					index = numOfPost
					dictOfCategories[postName] = numOfPost
					tmpCategoryObj = {}
					tmpCategoryObj.name = postName
					createCategories.push(tmpCategoryObj)
					createLegendData.push(postName)
					numOfPost = numOfPost + 1
				}
				// console.log(index)
				tmpNodeObj = {}
				tmpNodeObj.category = index
				tmpNodeObj.name = name
				tmpNodeObj.value = 8
				createNodes.push(tmpNodeObj)
			}
			tmpLinkObj = {}
			tmpLinkObj.source = "董事会"
			tmpLinkObj.target = name
			tmpLinkObj.weight = linkName.length
			tmpLinkObj.name = linkName
			createLinks.push(tmpLinkObj)
		}
		// console.log(createCategories)
		for (name in executivesOfCompany) {
			postArray = executivesOfCompany[name]
			linkName = ""
			for(i in postArray){
				postName = postArray[i]
				linkName = linkName + ' '+postName
				var index
				if (postName in dictOfCategories) {
					index = dictOfCategories[postName]
				}
				else {
					index = numOfPost
					dictOfCategories[postName] = numOfPost
					createLegendData.push(postName)
					tmpCategoryObj = {}
					tmpCategoryObj.name = postName
					createCategories.push(tmpCategoryObj)
					numOfPost = numOfPost + 1
				}
				tmpNodeObj = {}
				tmpNodeObj.category = index
				tmpNodeObj.name = name
				tmpNodeObj.value = 7
				createNodes.push(tmpNodeObj)
			}
			tmpLinkObj = {}
			tmpLinkObj.source = "高管"
			tmpLinkObj.target = name
			tmpLinkObj.weight = linkName.length
			tmpLinkObj.name = linkName
			createLinks.push(tmpLinkObj)
		}


		option_.legend = {
				        x: 'left',
				        data:createLegendData
				    };
		option_.series = [
				        {
				            type:'force',
				            name : "所任职务",
				            ribbonType: false,
				            categories : createCategories,
				            itemStyle: {
				                normal: {
				                    label: {
				                        show: true,
				                        textStyle: {
				                            color: '#333'
				                        }
				                    },
				                    nodeStyle : {
				                        brushType : 'both',
				                        borderColor : 'rgba(255,215,0,0.4)',
				                        borderWidth : 1
				                    },
				                    linkStyle: {
				                        type: 'curve'
				                    }
				                },
				                emphasis: {
				                    label: {
				                        show: false
				                    },
				                    nodeStyle : {
				                        //r: 30
				                    },
				                    linkStyle : {}
				                }
				            },
				            useWorker: false,
				            minRadius : 15,
				            maxRadius : 25,
				            gravity: 1.1,
				            scaling: 1.1,
				            roam: 'move',
				            nodes:createNodes,
				            links : createLinks
				        }
				    ];
				    
		return option_;
	}
}
var ConfigData = {
	CreateData:function(option_,companyName_,keyWordsArray_) {
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
			 console.log(word)
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
	}
}
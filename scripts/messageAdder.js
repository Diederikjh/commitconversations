

$(document).ready(function(){
  
	addRandomCommentsToMessageNode(3);
	$("button").click(function(){
		var m = $('#messages');
		m.empty();
		addRandomCommentsToMessageNode(3);
	});
});

var g_messageDict = {};

function postMessagesObjectToUrl()
{
	var dictAsArray = new Array()
	dictAsArray.push('message0=' + g_messageDict.message0)
	dictAsArray.push('message1=' + g_messageDict.message1)
	dictAsArray.push('message2=' + g_messageDict.message2)
	history.pushState(g_messageDict, "aabbcc", "?" + dictAsArray.join("&"));
//	TODO on popstate, inspect message dict, and display as appropriate
//  TODO read URL paramers on load  (share to a friend) 
}

function addRandomCommentToMessageNode(i)
{
	$.get("/api/1/getOneMessage",function(data,status){
		var rootElement = document.getElementById('messages')
        var m = $('#messages');
		var jsonData = eval('(' + data + ')');
		
		// TODO this is not used here, use fow URL parse.
		urlnow = document.URL
		var url = $.url(urlnow)
		urlParams = url.param()
		message0 = urlParams['message0']
		message1 = urlParams['message1']
		message2 = urlParams['message2']
		
		if (i == 0) {
			g_messageDict['message0'] = jsonData.insertCounter 
		}
		
		if (i == 1) {
			g_messageDict['message1'] = jsonData.insertCounter
		}
		
		if (i == 2) {
			g_messageDict['message2'] = jsonData.insertCounter
			postMessagesObjectToUrl()
		}
		
		m.append("<div>".concat(jsonData.message,'</div>'));
	});
}

function addRandomCommentsToMessageNode(n)
{
	for (var i=0; i<n; i++)
	{    
		addRandomCommentToMessageNode(i);
	}
}


function addRandomCommentsToMessageNodes()
{
	var m1 = $('#message1');
	m1.empty();
	var m2 = $('#message2');
	m2.empty();
	var m3 = $('#message3');
	m3.empty();
	addRandomCommentToMessageNode(m1);
	addRandomCommentToMessageNode(m2);
	addRandomCommentToMessageNode(m3);
}

$(document).ready(function(){
	addRandomCommentsToMessageNodes();
	$("#refresh_button").click(function(){
		addRandomCommentsToMessageNodes()
	});
});


function addRandomCommentToMessageNode(messageNode)
{
	$.get("/api/1/getOneMessage",function(data,status){
		var jsonData = eval('(' + data + ')');
		
		// TODO this is not used here, use fow URL parse.
//		urlnow = document.URL
//		var url = $.url(urlnow)
//		urlParams = url.param()
//		message0 = urlParams['message0']
//		message1 = urlParams['message1']
//		message2 = urlParams['message2']
//		
//		if (i == 0) {
//			g_messageDict['message0'] = jsonData.insertCounter 
//		}
//		
//		if (i == 1) {
//			g_messageDict['message1'] = jsonData.insertCounter
//		}
//		
//		if (i == 2) {
//			g_messageDict['message2'] = jsonData.insertCounter
//			postMessagesObjectToUrl()
//		}
		messageNode.append(jsonData.message);
	});
}

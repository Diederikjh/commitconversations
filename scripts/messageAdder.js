
function addRandomCommentsToMessageNodes()
{
	var m1 = $('#message1');
	m1.empty();
	var m2 = $('#message2');
	m2.empty();
	var m3 = $('#message3');
	m3.empty();
	addRandomCommentToMessageNode(m1, "m1");
	addRandomCommentToMessageNode(m2, "m2");
	addRandomCommentToMessageNode(m3, "m3");
}

$(document).ready(function(){
	m1 = $.url().param('m1');
	m2 = $.url().param('m2');
	m3 = $.url().param('m3');
	if (m1 && m2 && m3)
	{
		setRandomMessages(m1,m2,m3)
	}
	else
	{
		addRandomCommentsToMessageNodes();
	}
	$("#refresh_button").click(function() {
		addRandomCommentsToMessageNodes()
	});
});

function setRandomMessages(insertID1, insertID2, insertID3){
	var m1 = $('#message1');
	m1.empty();
	var m2 = $('#message2');
	m2.empty();
	var m3 = $('#message3');
	m3.empty();
	
	setCommentByIDToMessageNode(m1, insertID1, "m1");
	setCommentByIDToMessageNode(m2, insertID2, "m2");
	setCommentByIDToMessageNode(m3, insertID3, "m3");
}

function addRandomCommentToMessageNode(messageNode, stateID) {
	$.get("/api/1/getOneMessage", function(data, status) {
		// TODO check status
		setDataOnNodeAndSaveSate(messageNode, stateID, data)
	});
}

function setCommentByIDToMessageNode(messageNode, insertID, stateID){
	$.get("/api/1/getOneMessageById?id="+insertID, function(data, status) {
		// TODO check status
		setDataOnNodeAndSaveSate(messageNode, stateID, data)
	});
}

function setDataOnNodeAndSaveSate(messageNode, stateID, data)
{
	var jsonData = eval('(' + data + ')');
	var currentState = history.state;
	messageNode.append(jsonData.message);

	if (!currentState) {
		currentState = new Object();
	}
	currentState[stateID] = jsonData.insertCounter
	history.replaceState(currentState, "title", "");
}


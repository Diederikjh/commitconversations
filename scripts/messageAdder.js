
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


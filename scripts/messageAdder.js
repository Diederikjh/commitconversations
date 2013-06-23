
function addRandomCommentToMessageNode(messageNode, stateID) {
	$.ajax({
		url : "/api/1/getOneMessage",
		success : function(data, status) {
			// TODO check status
			setDataOnNodeAndSaveSate(messageNode, stateID, data)
		},
		cache : false,
		dataType : "json"
	});
	// .ajax script is for disable caching
}

function setCommentByIDToMessageNode(messageNode, insertID, stateID){
	$.get("/api/1/getOneMessageById?id="+insertID, function(data, status) {
		// TODO check status
		setDataOnNodeAndSaveSate(messageNode, stateID, data)
	});
}

function setDataOnNodeAndSaveSate(messageNode, stateID, data)
{
	var currentState = history.state;
	messageNode.append(data.message);

	if (!currentState) {
		currentState = new Object();
	}
	currentState[stateID] = data.insertCounter
	history.replaceState(currentState, "title", "");
}


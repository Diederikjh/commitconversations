$(document).ready(function() {
	
	hasValidURLParams = function(){
		insertID = $.url().param('m');
		return insertID
	}
	
	var m = $('#messages');
	if (hasValidURLParams()) {
		setCommentByIDToMessageNode(m, insertID, "m");
	} else {
		addRandomCommentToMessageNodeLocal();
	}

	$("#refresh_button").click(function() {
		addRandomCommentToMessageNodeLocal();
	});
	
	setupShareButton()
});

function addRandomCommentToMessageNodeLocal() {
	var m = $('#messages');
	m.empty();
	addRandomCommentToMessageNode(m, "m");
}

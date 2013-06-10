

$(document).ready(function() {
	m1 = $.url().param('m1');
	m2 = $.url().param('m2');
	m3 = $.url().param('m3');
	if (m1 && m2 && m3) {
		setRandomMessages(m1, m2, m3)
	} 
	else {
		addRandomCommentsToMessageNodes();
	}
	$("#refresh_button").click(function() {
		addRandomCommentsToMessageNodes()
	});
	
	setupShareButton()
});

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
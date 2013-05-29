

$(document).ready(function(){
	addRandomCommentToMessageNode();
	$("#refresh_button").click(function(){
		var m = $('#messages');
		m.empty();
		addRandomCommentToMessageNode();
	});
});

function addRandomCommentToMessageNode()
{
	$.get("/api/1/getOneMessage",function(data,status){
		var rootElement = document.getElementById('messages')
        var m = $('#messages');
		var jsonData = eval('(' + data + ')');
		m.append("<div>".concat(jsonData.message,'</div>'));
	});
}


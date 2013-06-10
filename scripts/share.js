function getStateAsUrlString()
{
	s = history.state
	var keys = Object.keys(s)
	var stringArray = []
	for (var i=0,len=keys.length; i<len; i++){
		stringArray.push(keys[i] + '=' + s[keys[i]])
	}
	return stringArray.join('&')
}

function setupShareButton()
{
	var m = $('#share_button');
	
	// setup popover attributes
	m.attr('data-original-title', 'Share URL')
	m.attr('data-content', "<input id='shareinput' class='input control-group' type='text'></input>")        
	m.attr('data-trigger', 'manual')
	m.attr('data-html', 'true')
	m.click(function(e) {
		m.popover('toggle')
		var i = $('#shareinput')
		var l = window.location.toString()	
		if (l.indexOf('?') != -1){
			var splitted = l.split('?')
			l = splitted[0]
		}		
		queryString = getStateAsUrlString()
		l = l + '?' + queryString
		i.val(l)
		i.select()
		i.focusout(function(){
			m.popover('hide')
		});
	});
	var p = m.popover()
}


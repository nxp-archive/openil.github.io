// <![CDATA[
var kind;
kind = 'HTML';

function get_header_html_text() {
	var html_text='';
	if (kind == 'HTML') {
		
		var sidePositionPanel = 'left',
			elements_body = 'body',
			elements_logo_style = '.logo, .logo span',
			//elements_heading_font_style - token from //head_html_default_block.js
			//elements_heading_font_style = '.logo, h1, h2',
			elements_h1_style = 'h1, h1 a',
			elements_h2_style = 'h2, h2 span, h2 a',
			elements_h3_style = 'h3, h3 a span, h3 a',
			elements_content_style = "body, code, input[type='text'], textarea",
			elements_content_href_style = 'a',
			elements_background_style = '.body_pattern',
			//logo_style
			st_logo_font_color="#262626",
			st_logo_font_size="30",
			//headers_style
			h1_font_color="#333333",
			h1_font_size="14",
			h2_font_color="#000000",
			h2_font_size="18",
			h3_font_color="#313131",
			h3_font_size="14",
			// global style
			content_font_style="Liberation sans",
			content_font_size="12",
			content_font_color="#a9a9a9",
			content_links_font_color="#12a4dc",
			//background style
			background_color="",
			background_img="images/background.png",
			background_rep = "repeat",
			//background_Full_Image = "background:#27262c url('http://www.pimg.co/backgrounds/u_backgraund/bg_2.png') no-repeat;",
			background_Full_Image = "background:#27262c url('images/background.png');",
			background_Image_Size = "auto auto",
			background_Image,
			background_Other = true; // false
			
		if (background_img == "") {
			background_Image= "none";
		} else if (background_Full_Image == '') {
			background_Image="http://cdn.pimg.co/backgrounds/u_backgraund/"+background_img;
		} else if (background_Other) {
			background_Image="http://cdn.pimg.co/backgrounds/u_backgraund/"+background_img;
		} else {
			background_Image="box_setting/images/bg_images/"+background_img;
		}
		
		html_text = '<link rel="stylesheet" type="text/css" href="box_setting/css/box-setting.css" />'+
			'\n<script type="text/javascript" src="box_setting/js/jquery.cookies.2.2.0.min.js"></script>'+
			'\n<script type="text/javascript" src="box_setting/js/box-setting.js"></script>'+
			'\n<script type="text/javascript" src="box_setting/colorpicker/js/jquery.animate-colors-min.js"></script>'+
			'\n<link rel="stylesheet" media="screen" type="text/css" href="box_setting/colorpicker/css/colorpicker.css" />'+
			'\n<script type="text/javascript" src="box_setting/colorpicker/js/colorpicker.js"></script>'+
			'\n<script type="text/javascript" src="box_setting/colorpicker/js/jquery.animate-colors-min.js"></script>'+
			'\n<script type="text/javascript">'+
			'\n$(function() {'+
			'\n	$.boxSettings({'+
			'\n		// header style settings'+
			'\n		sidePositionPanel :"'+sidePositionPanel+'",'+
			'\n		elements_heading_font_style :"'+elements_heading_font_style+'",'+
			'\n		elements_body :"'+elements_body+'",'+
			'\n		elements_logo_style :"'+elements_logo_style+'",'+
			'\n		elements_h1_style :"'+elements_h1_style+'",'+
			'\n		elements_h2_style :"'+elements_h2_style+'",'+
			'\n		elements_h3_style :"'+elements_h3_style+'",'+
			'\n		elements_content_style :"'+elements_content_style+'",'+
			'\n		elements_content_href_style :"'+elements_content_href_style+'",'+
			'\n		elements_background_style :"'+elements_background_style+'",'+
			'\n		header_google_font:"'+header_google_font+'",'+
			'\n		header_font_style:"'+header_font_style+'",	'+	
			'\n		st_logo_font_color:"'+st_logo_font_color+'",'+
			'\n		st_logo_font_size:"'+st_logo_font_size+'",'+
			'\n		h1_font_color:"'+h1_font_color+'",'+
			'\n		h1_font_size:"'+h1_font_size+'",'+
			'\n		h2_font_color:"'+h2_font_color+'",'+
			'\n		h2_font_size:"'+h2_font_size+'",'+
			'\n		h3_font_color:"'+h3_font_color+'",'+
			'\n		h3_font_size:"'+h3_font_size+'",'+
			'\n		content_font_style:"'+content_font_style+'",'+
			'\n		body_font_size:"'+content_font_size+'",'+
			'\n		body_line_spacing:"1.8", // em'+
			'\n		body_font_color:"'+content_font_color+'",'+
			'\n		body_links_font_color:"'+content_links_font_color+'",'+		
			'\n		background_overlay:"0.0",'+
			'\n		background_color:"'+background_color+'",'+
			'\n		background_Image: "'+background_Image+'",'+
			'\n		background_Full_Image: "'+background_Full_Image+'",'+
			'\n		background_Image_Size: "'+background_Image_Size+'",'+
			'\n		background_Image_Repeat: "'+background_rep+'"'+
			'\n		//background_Image: "none"'+
			'\n	});'+
			'\n})'+
			'\n</script>';
	}
	return (html_text);
}

document.writeln(get_header_html_text());


//script generating imgs
document.writeln('<script type="text/javascript" src="js/get_img.js"></script>');

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
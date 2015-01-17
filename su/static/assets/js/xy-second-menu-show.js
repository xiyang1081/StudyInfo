
         $(function(){
         	$(document).ajaxSend(function(event, xhr, settings) {
			    function getCookie(name) {
			        var cookieValue = null;
			        if (document.cookie && document.cookie != '') {
			            var cookies = document.cookie.split(';');
			            for (var i = 0; i < cookies.length; i++) {
			                var cookie = jQuery.trim(cookies[i]);
			                // Does this cookie string begin with the name we want?
			                if (cookie.substring(0, name.length + 1) == (name + '=')) {
			                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
			                    break;
			                }
			            }
			        }
			        return cookieValue;
			    }
			    function sameOrigin(url) {
			        // url could be relative or scheme relative or absolute
			        var host = document.location.host; // host + port
			        var protocol = document.location.protocol;
			        var sr_origin = '//' + host;
			        var origin = protocol + sr_origin;
			        // Allow absolute or scheme relative URLs to same origin
			        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
			            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
			            // or any other URL that isn't scheme relative or absolute i.e relative.
			            !(/^(\/\/|http:|https:).*/.test(url));
			    }
			    function safeMethod(method) {
			        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
			    }
			    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
			        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			    }
			});

         	$("div#navbar ul li a").click(function(){
         		$(this).parent().addClass("active").siblings().removeClass();
         		$("div#listcon").show();
                var s=$(this).attr("pre");
                $.post("/blog/show/",{"second_id":s},function(data){                  
                	var dataObj=eval("("+data+")");//转换为json对象
                    $("div#cons").empty();
                	var tmp='<ul class="nav nav-tabs" role="tablist">';
                	
                    $.each(dataObj,function(key,val){
                    	if(key==0)
                    	{
                    		tmp+='<li role="presentation" class="active"><a target="_bank" href="javascript:listviews('+val.second_id+')" >'+val.second_items+'</a></li>';	
                    		//tmp+='<li role="presentation"  class="active"><a href="#" >'+val.second_items+'</a></li>';
                    		listviews(val.second_id);
                    	}
                    	else
                    	{
                    		tmp+='<li role="presentation"><a target="_bank" href="javascript:listviews('+val.second_id+')">'+val.second_items+'</a></li>';
                    		//tmp+='<li role="presentation"><a href="#" >'+val.second_items+'</a></li>';
                    	}
                    	//onclick="listviews('+val.second_id+')"
                      //tmp+='<li role="presentation"><a href="#">'+val.second_items+'</a></li>';  
                    });
                    tmp+='</ul>';
                	$("div#cons").html(tmp);
                });
             });
         	
         	

         })
         
        
         function listviews(t){        	 
        	 var s =t;
        	 $.post("/blog/bloglist/",{"parent_id":s},function(data){
        		 //alert(data);
        		 var dataObj=eval("("+data+")");//转换为json对象
        		 $("div#bloglist").empty();
        		 var tmp="";
        		 $.each(dataObj,function(key,val){
        			 tmp+='<div class="blog-post"><h2 class="blog-post-title">'+val.bc_name+'</h2><h4 style="color:red;">About:</h4><p style="font-size: 18px;line-height: 1.5;">'+val.bc_Mark+'....<br/><a target="_bank" href="/blog/bloglist/'+val.bc_id+'/">More info ...</a></p><p class="blog-post-meta">'+val.bc_time+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;by XiYang</p></div>';
        			 /*
        			 tmp+='<div class="col-sm-4"><div class="panel panel-primary"> <div class="panel-heading"><h3 class="panel-title">'+val.bc_name+'</h3></div>';
        			 tmp+='<div class="panel-body">'+'<a href="#">Contents>>></a><br/>'+val.bc_time+'</div></div></div></div>';
        		 */
        		 });
        		 //alert(tmp);
        		 $("div#bloglist").html(tmp);
        	 });
         }
        
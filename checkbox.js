//jq判断checkbox是否被选中
function doSelectAll(node){
	if($(node).is(":checked")){
    //选中复选框
$("[name = SERNO]:checkbox").attr("checked", true);
	}else{
    //取消选中
    $("[name = SERNO]:checkbox").attr("checked", false);
	}
}

//根据name属性判断哪些被选中
$("[name=SERNO]").each(function(){
	alert($(this).is(":checked"))			
});



<input type="checkbox" onclick="doSelectAll(this)"/>

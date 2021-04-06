function status(){
    var status = document.getElementsByClassName("status-element-status").value;
    console.log(status);
    if(status=="request"){
        document.getElementsByClassName("status-element-status").style.color = "#B53F45";
    }
}
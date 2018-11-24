$("document").ready(function () {
    window.setInterval(function () {
        var life = 2500;
        var top = randNum();
        var left = randNum();
        var size = randomSize();
        var id = top.toString() + left.toString();
        $("#404wrap").append("<span id='" + id + "' style='color:" + randomColor() + ";font-size:" + size + "px;top:" + top + "%;left:" + left + "%;' class='boopText'>" + /*randomMessage()*/"Welcome..!!" + "</span>");
        setTimeout(function () {
            $("#" + id).remove();
        }, life);
    }, 200);

    /*function randomMessage() {
      messages = ['Oh No! 404', '404', 'aw snap, wrong page', '404 error!', 'We got lost!', "You're not supposed to be here!","You're lost!", 'Wrong page!', '404 - page not found', 'not found!','Whoops!'];
      return messages[Math.floor(Math.random() * messages.length)];
    }*/

    function randomColor() {
        return '#' + (Math.random() * 0xCCCCCC << 0).toString(16);
    }
    function randomSize() {
        return Math.floor(Math.random() * 29) + 20;
    }
    function randNum() {
        return Math.floor(Math.random() * 99) + 1;
    }
    $("#qbtn").on("click", function () {
        $("#cspinner").css("display", "block");
        $.getJSON($SCRIPT_ROOT + "agq", {
            para: $("#qdata").val()
        }, function (data) {
            $("#cspinner").css("display", "none");
            $("#adata").html();
            $("#adata").html(data);
            $("#feedbform").css("display", "block");
        });
        return false;
    });
    $("#submit_final").on("click", function () {
        $.getJSON($SCRIPT_ROOT + "submit_data", {
            name: $("#name").val(),
            email: $("#email").val(),
            para: $("#qdata").val(),
            ques: $("#adata").html(),
            feeds: $("#feeds").val()
        });
        Metro.dialog.create({
            title: "",
            content: "<p style='font-weight:100;font-size:36px;'>Thank you for your feedback</p>",
            actions: [
                {
                    caption: "OK",
                    cls: "js-dialog-close secondary",
                    onclick: function () {
                        $.ajax({
                            url: "",
                            context: document.body,
                            success: function (s) {
                                $('html[manifest=saveappoffline.appcache]').attr('content', '');
                                $(this).html(s);
                            }
                        });
                        window.location.replace("http://127.0.0.1:5000/about");
                    }
                }
            ]
        });
        return false;
    });
});
var shortened = 0;

$(document).ready(function() {
    $("form").submit(function(event) {
        if ($("#url").val() == "") {
            window.location.replace("/invalid");
        } else {
            $.ajax({
                type        : "POST",
                url         : "/shorten",
                data        : { "url": $("input[name=url]").val() },
                dataType    : "text",
                encode      : true
            }).done(function(data) {
                if (shortened == 0) {
                    $("#shortened-title").append("Shortened:");
                    shortened = 1;
                }

                $("#shortened").append( "<li>" + $("input[name=url]").val() + " -> <a href=\"https://vanilla.rocks/" + data + "\">https://vanilla.rocks/" + data + "</a></li>" );
            });
        }

        event.preventDefault();
    });

});
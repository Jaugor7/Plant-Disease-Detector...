    $('#predict').click(function (event) {
        event.preventDefault();
        var form_data = new FormData($('#upload_file')[0]);
        console.log("Sending Data To Backend...")
        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/check/',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                console.log('Success!');
                window.location.href = "/";

            }
        });
    });
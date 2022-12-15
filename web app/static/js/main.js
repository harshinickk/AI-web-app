$(document).ready(function () {
    // Init
    $('.cornimage-section').hide();
    $('.cornloader').hide();
    $('#cornresult').hide();
	$('.cottonimage-section').hide();
    $('.cottonloader').hide();
    $('#cottonresult').hide();
	$('.cucumberimage-section').hide();
    $('.cucumberloader').hide();
    $('#cucumberresult').hide();
	$('.potatoimage-section').hide();
    $('.potatoloader').hide();
    $('#potatoresult').hide();
	$('.riceimage-section').hide();
    $('.riceloader').hide();
    $('#riceresult').hide();

    // Upload Preview
    function cornreadURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#cornimagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#cornimagePreview').hide();
                $('#cornimagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
	function cottonreadURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#cottonimagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#cottonimagePreview').hide();
                $('#cottonimagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
	function cucumberreadURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#cucumberimagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#cucumberimagePreview').hide();
                $('#cucumberimagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
	function potatoreadURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#potatoimagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#potatoimagePreview').hide();
                $('#potatoimagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
	function ricereadURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#riceimagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#riceimagePreview').hide();
                $('#riceimagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#cornimageUpload").change(function () {
        $('.cornimage-section').show();
        $('#btn-cornpredict').show();
        $('#cornresult').text('');
        $('#cornresult').hide();
        cornreadURL(this);
    });
	$("#cottonimageUpload").change(function () {
        $('.cottonimage-section').show();
		$('#btn-cottonpredict').show();
        $('#cottonresult').text('');
        $('#cottonresult').hide();
        cottonreadURL(this);
    });
	$("#cucumberimageUpload").change(function () {
        $('.cucumberimage-section').show();
		$('#btn-cucumberpredict').show();
        $('#cucumberresult').text('');
        $('#cucumberresult').hide();
        cucumberreadURL(this);
    });
	$("#potatoimageUpload").change(function () {
        $('.potatoimage-section').show();
		$('#btn-potatopredict').show();
        $('#cucumberresult').text('');
        $('#cucumberresult').hide();
        potatoreadURL(this);
    });
	$("#riceimageUpload").change(function () {
        $('.riceimage-section').show();
		$('#btn-ricepredict').show();
        $('#riceresult').text('');
        $('#riceresult').hide();
        ricereadURL(this);
    });

    //Corn Predict
    $('#btn-cornpredict').click(function () {
        var form_data = new FormData($('#cornupload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.cornloader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/corn',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.cornloader').hide();
                $('#cornresult').fadeIn(600);
                $('#cornresult').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });
	
	//Cotton Predict
    $('#btn-cottonpredict').click(function () {
        var form_data = new FormData($('#cottonupload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.cottonloader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/cotton',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.cottonloader').hide();
                $('#cottonresult').fadeIn(600);
                $('#cottonresult').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });
	
	//Cucumber Predict
    $('#btn-cucumberpredict').click(function () {
        var form_data = new FormData($('#cucumberupload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.cucumberloader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/cucumber',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.cucumberloader').hide();
                $('#cucumberresult').fadeIn(600);
                $('#cucumberresult').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });
	
	//Potato Predict
    $('#btn-potatopredict').click(function () {
        var form_data = new FormData($('#potatoupload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.potatoloader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/potato',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.potatoloader').hide();
                $('#potatoresult').fadeIn(600);
                $('#potatoresult').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });
	
	//Rice Predict
    $('#btn-ricepredict').click(function () {
        var form_data = new FormData($('#riceupload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.riceloader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/rice',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.riceloader').hide();
                $('#riceresult').fadeIn(600);
                $('#riceresult').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });


});
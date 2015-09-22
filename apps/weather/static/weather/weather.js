$(document).ready(function() {

	for(i=0; i<9; i++) {

		var id = "#zip-" + i;

		$(id).on('click', function(e) {
			var zip = $(this).attr("data-zipcode");
			location.href = zip;
		});
	}
});

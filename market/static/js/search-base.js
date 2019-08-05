$(function() {

	// open and close the mobile search bar
	$("#mob_nav_search").click(function(e){
		e.preventDefault();
		e.stopPropagation();
		toggleMobileSearchBar();
	});

	$("#tab_nav_search").click(function(e){
		e.preventDefault();
		toggleMobileSearchBar();
	});

	function toggleMobileSearchBar(){
		if($("#mobile_search_dropdown").hasClass("collapse")){
			$("#mobile_search_dropdown").removeClass("collapse");
			$(".mobile_search_input").focus();
		}else{
			$("#mobile_search_dropdown").addClass("collapse");
		}
	}

	// Duplicate search suggestions for mobile search and make it full width.
	$(".search_suggestions").clone().appendTo("#mobile_search_dropdown form").css('width','100%').css('min-width', '300px');
	// prevent closing suggestions when clicking on them.
	$(".search_suggestions").click(function (e) {
		e.stopPropagation();
	})

	// Show suggested search
	$('input.search_input').on('focus click', function (e) {
		if(this.value === '') {
			$(this).closest('form').find(".search_suggestions").show();
			// prevent hiding suggestions when clicking on the search bar.
			e.stopPropagation();
		}
	});
	// Hide suggested search
	$('input.search_input').on('input', function () {
		hideSuggestions();
	});
	$('body').on('click', hideSuggestions);
	window.addEventListener('scroll', hideSuggestions);
	function hideSuggestions() {
		$(".search_suggestions").hide();
	}

	// analytics event for suggested search
	$("a.suggested_search_link").click(function(e) {
		var text = $(this).text().trim();
		ga("send", "event", "Search", "Suggested", text, 0, {transport: 'beacon'});
	});

});
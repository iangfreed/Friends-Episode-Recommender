$("#first-choice").change(function() {
   $("#second-choice").load("../static/textdata/" + $(this).val() + ".txt");
});

function abc(data){
    alert(data);
}

$(document).ready(function(){
    var search = {
        listeners: function(){
            $('.search-input').click(function(){
                alert('');
                try{
                    var searchTerm = $(this).val();
                    var minCharacters = 3;

                    // Check if characters are more than minCharacters
                    if (val.length >= minCharacters){
                        search.read(searchTerm);
                    }
                }
                catch(ex){
                    console.log(ex);
                }
            });
        },
        read: function(searchTerm){
            try{
                var data = {'searchTerm': searchTerm};
                var url = "/search"
                $.ajax({
                    url: url,
                    data: data,
                    type: 'GET',
                    success: function(response){
                        try{
                            response = JSON.parse(response);
                            if (response.length != 0){
                                // Now append search results
                                search.build(response);
                            }
                        }
                        catch(ex){
                            console.log(ex);
                        }
                    }
                });
            }
            catch(ex){
                console.log(ex);
            }
        },
        build: function(response){
            var data = response;
            var target = '.search-results';
            var appendable = "";

            // Clearing out the search result div first
            $(target).html('');

            for (x in data){
                appendable += '<a href="/company?cin="'+data.cin+'><div class="result">'+
                '<div class="company-name">'+data.name+'</div>'+
                '<div class="company-cin">'+data.cin+'</div>'+
                '<div class="company-state">'+data.state+'</div>'+
                '</div></a>';
            }

            // Append the results on screen
            $(target).append(appendable);
        },
    };
});
(function(){
    var grid = $find("ctl00_ContentPlaceHolder1_radSpecies");
    if (!grid) {
        console.log("Grid nathi malti bhai ... ");
        return;
    }

    var tableView = grid.get_masterTableView();
    var rows = document.querySelectorAll("tr.rgRow, tr.rgAltRow");

    console.log("total rows found ... :", rows.length);

    rows.forEach(function(row){
        try {
            tableView.selectItem(row);
        } catch(e) {
            console.log("Bhai Gadbad ho gyaa error selecting row:", e);
        }
    });

    console.log("Jetrock Selection done!");
})();

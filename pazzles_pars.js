/* parser for console - https://privatekeys.pw/puzzles/bitcoin-puzzle-tx */

var pazlss = {}

$.each($(".table.table-striped.table-hover > tbody > tr"), function (index, value) {
    var adr = $(value).find("a")[1].href.split("/")[5];
    if ($(value).find(".badge.badge-success")?.text()) {

        var rage = $(value).find(".no-break:eq(1)").text().trim().split("...")

        pazlss[adr] = {
            balance: $(value).find(".badge.badge-success").text().trim(),
            received: $(value).find(".badge.badge-primary").text().trim(),
            txcount: $(value).find(".badge.badge-warning").text().trim(),
            bit: $(value).find(".no-break:eq(0)").text().trim(),
            rage: "2^"+rage[0].substr(1)+"—2^"+rage[1].substr(1),
            startKey: new URL($(value).find("a")[0].href).searchParams.get("startKey"),
            stopKey: new URL($(value).find("a")[0].href).searchParams.get("stopKey"),
        };
    }
});


console.log(JSON.stringify(pazlss));
---
title: "Create Model and Sheet Views Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Model_and_Sheet_Views_Example_JS.htm"
---

# Create Model and Sheet Views Example (JS)

## Create Model and Sheet Views Example (JavaScript)

| This example shows how to create a model view or a sheet view. Start DraftSight. Using the following form: Select Create a model view . Type double values for the coordinates of a corner of a model view. Type double values for the coordinates of the opposite corner of the model view. Type the model view name. Type the category of the new model view. Type a save name for the current model view. Type a save category for the current model view. Activate the model space in DraftSight. Click Create View . - or - Select Create a sheet view . Type double values for the coordinates of a corner of a sheet view. Type double values for the coordinates of the opposite corner of the sheet view. Type the sheet view name. Type the category of the new sheet view. Type a save name of the current sheet view. Type a save category for the current sheet view. Activate the sheet space in DraftSight. Click Create View . Click View > Named Views in the model or sheet space and inspect View names. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the web page and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,view manager">
<meta name=MS-HKWD content="JavaScript examples,model views">
<meta name=MS-HKWD content="JavaScript examples,sheet views">
    <head>

    <!-- Without this line, this does not work in Internet Explorer 8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=8" />

    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

    <!-- Add your dsInterface .js Files here -->
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModel.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModelNamedView.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsNamedView.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSheetNamedView.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsViewManager.js"></script>

    <!-- This is the main block where you place the JavaScript API code -->
    <script type="text/javascript">
        function printOut(str) {
            document.getElementById("OB").value += str + "\n";
            document.getElementById("OB").scrollTop += document.getElementById("OB").scrollHeight;
        }

        function runMacro() {
            //This is to catch any errors and exit out of the code
            //It displays an error in the output box
            try {
                document.getElementById("OB").value = "";
                apiCode();
            }
            catch (err) {
                printOut(djErrorString(err));
            }
        }
        function apiCode() {
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mVMgr = mDoc.GetViewManager();
            if (document.inputform.Choose[0].checked){
            	mModel.Activate();
            	var X = parseFloat(document.getElementById("X").value);
                var Y = parseFloat(document.getElementById("Y").value);
                var Z = parseFloat(document.getElementById("Z").value);
                var bArray = new Array();
			    bArray[0] = X;
			    bArray[1] = Y;
			    bArray[2] = Z;
			    var X2 = parseFloat(document.getElementById("X2").value);
                var Y2 = parseFloat(document.getElementById("Y2").value);
                var Z2 = parseFloat(document.getElementById("Z2").value);
                var cArray = new Array();
			    cArray[0] = X2;
			    cArray[1] = Y2;
			    cArray[2] = Z2;
			    var name1 = document.getElementById("name1").value;
                var cat1 = document.getElementById("cat1").value;
				var savename1 = document.getElementById("savename1").value;
				var savecat1 = document.getElementById("savecat1").value;
                var resultStatus = mVMgr.CreateModelNamedView(name1, cat1, bArray, cArray);
                var nView = resultStatus.NamedView;
                var namedView1 = nView.GetNamedView();
                printOut("Result status of new model view creation: " + namedView1.GetName());
                mVMgr.ActivateModelView(namedView1.GetName());
                var modelNamedView = mVMgr.GetModelNamedView(name1);
                var namedView = modelNamedView.GetNamedView();
                var name = namedView.GetName();
                printOut("New model view: " + JSON.stringify(name));
                mVMgr.SaveCurrentViewAsModelView(savename1, savecat1);
                mVMgr.ActivateModelView(savename1);
            }
            else if (document.inputform.Choose[1].checked){
                var X1 = parseFloat(document.getElementById("X1").value);
                var Y1 = parseFloat(document.getElementById("Y1").value);
                var Z1 = parseFloat(document.getElementById("Z1").value);
                var dArray = new Array();
			    dArray[0] = X1;
			    dArray[1] = Y1;
			    dArray[2] = Z1;
			    var X3 = parseFloat(document.getElementById("X3").value);
                var Y3 = parseFloat(document.getElementById("Y3").value);
                var Z3 = parseFloat(document.getElementById("Z3").value);
                var eArray = new Array();
			    eArray[0] = X3;
			    eArray[1] = Y3;
			    eArray[2] = Z3;
			    var name2 = document.getElementById("name2").value;
                var cat2 = document.getElementById("cat2").value;
				var savename2 = document.getElementById("savename2").value;
				var savecat2 = document.getElementById("savecat2").value;
            	var resultStatus2 = mVMgr.CreateSheetNamedView(name2, cat2, dArray, eArray);
            	var snamedview = resultStatus2.NamedView;
            	var snview = snamedview.GetNamedView();
                printOut("Result status of new sheet view creation: " + snview.GetName());
                mVMgr.ActivateSheetView(snview.GetName());
                var sheetNamedView = mVMgr.GetSheetNamedView(name2);
                var namedView2 = sheetNamedView.GetNamedView();
                name = namedView2.GetName();
                printOut("New sheet view: " + JSON.stringify(name));
                mVMgr.SaveCurrentViewAsSheetView(savename2, savecat2);
                mVMgr.ActivateSheetView(savename2);
            }
           mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title> Create Model and Sheet Views Example (JS)</title>

    <!-- This style formats the heading -->
    <style type="text/css">
     H1 {
	font-weight: bold;
	font-size: 10pt;
	font-family: Verdana, sans-serif;
	/*border-left-style: Inset;*/
	/*border-right-style: Inset;*/
	border-top-style: none;
	/*border-bottom-style: none;*/
	border-bottom-style: solid;
	padding-top: 4pt;
	padding-bottom: 4pt;
	border-left-color: ##ccccff;
	border-right-color: ##ccccff;
	border-top-color: ##ccccff;
	/*border-bottom-color: ##ccccff;*/
	border-bottom-color: #808080;
	margin-top: -15pt;
	text-indent: .15in;
	border-top-width: 1px;
	border-bottom-width: 1px;
	color: #0000b9;
	border-left-width: 1px;
	border-right-width: 1px;
	margin-bottom: 10pt;
	vertical-align: Baseline;
	line-height: 28pt;
	margin-left: -10pt;
	margin-right: -10pt;
        background-image: url(dotnetimages/DraftSightTitleBackground.gif);
        }
         <!-- These styles format the table -->
        .style1
        {
        }
        .style2
        {
            height: 400px;
            text-align: center;
        }
        .style3
        {
            width: 460px;
            height: 60px;
        }
        .style4
        {
            height: 20px;
            text-align: left;
            font-family: Verdana, sans-serif;
            color: #006600;
            font-weight: bold;
        }
        .style5
        {
            width: 85px;
            height: 20px;
        }
        .style6
        {
            height: 30px;
            text-align: left;
            font-family: Verdana, sans-serif;
        }
        .style7
        {
            text-align: left;
	    font-size: 11px;
        }
        .style8
        {
            color: rgb(139, 141, 145);
            font-family: "Verdana, sans-serif";
        }
        .style14
        {
            font-family: "Verdana, sans-serif";
            text-align: center;
            color: rgb(153, 203, 82);
        }
        .style15
        {
            color: #99CB52;
            font-weight: bold;
        }
        .style16
        {
            color: #B3CFD3;
            font-weight: bold;
        }
        .style17
        {
            font-size: 36pt;
            color: #A2A1A6;
        }
        .style18
        {
            font-weight: bold;
        }
        .style19
        {
            text-align: left;
        }
        .style20
        {
            text-align: left;
            color: #006600;
        }
        .style21
        {
            width: 233px;
            height: 20px;
            text-align: left;
            font-family: Verdana, sans-serif;
            color: #B3CFD3;
            font-weight: bold;
        }
        .style22
        {
            width: 50px;
        }
    </style>

    </head>

    <H1> Create Model and Sheet Views Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to create a model view or a sheet view.<ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form:<ol type="a">
                            <li>Select <b>Create a model view</b>.<ol>
                            <li>Type double values for the coordinates of a corner of a model view.</li>
							<li>Type double values for the coordinates of the opposite corner
							of the model view.</li>
							<li>Type the model view name.</li>
							<li>Type the category of the new model view.</li>
							<li>Type a save name for the current model view.</li>
							<li>Type a save category for the current model view.</li>
                            </ol>
                            </li>
							<li>
							Activate the model space in DraftSight.</li><li>
							Click <b>Create View</b>.<ul>- or -</ul>
                            </ol>
                            <ol type="a">
                            <li></b>Select <b>Create a sheet view</b>.<ol>
                            <li>Type double values for the coordinates of a corner of a sheet view.</li>
							<li>Type double values for the coordinates of the opposite corner
							of the sheet view.</li>
							<li>Type the sheet view name.</li>
							<li>Type the category of the new sheet view.</li>
							<li>Type a save name of the current sheet view.</li>
							<li>Type a save category for the current sheet
							view.</li>
                            </ol>
                            </li>
							<li>Activate the sheet space in DraftSight.</li>
							<li>Click <b>Create View</b>.</li>
                            </ol>
                            <li>Click <b>View &gt; Named Views</b> in
							the model or sheet space and inspect View names.</li>
                            </ol>
								<p><b>NOTES:</b></p>
								<ul>
									<li>Errors are printed to
									Output.</li>
									<li>To recreate this example:</li>
								</ul>
								<blockquote>
									<ol>
										<li>Right-click the topic
										and select to view the source.
										</li>
										<li>Save the file as an HTML file. </li>
										<li>Open the HTML file in
										your web browser.</li>
										<li>If using Windows
										Internet Explorer and running scripts is
										blocked, click the Information bar
										near the top of the web page and select <b>
										Allow Blocked Content</b>.</li>
									</ol>
								</blockquote></div>
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3" width="535" style="width: 600px">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Create
										a model view</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        Coordinates of view corner:&nbsp; X:
                                        <input id="X" type="text" value="0.0" class="style22" /> Y:
                                        <input id="Y" type="text" value="0.0" class="style22" /> Z:
                                        <input id="Z" type="text" value="0.0" class="style22" /></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Coordinates of opposite
										view corner: X:
										<input id="X2" type="text" value="0.0" class="style22" name="T15" size="20" /> Y:
										<input id="Y2" type="text" value="0.0" class="style22" name="T16" size="20" /> Z:
										<input id="Z2" type="text" value="0.0" class="style22" name="T17" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Name:
										<input type="text" id="name1"name="T8" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Category:
										<input type="text" id="cat1" name="T9" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Save as name:
										<input type="text" id="savename1" name="T10" size="20">&nbsp;
										</td>
                                </tr>
                                <tr>
                                    <td class="style4">
										<p>&nbsp;&nbsp;&nbsp; Save as category:
										<input type="text" id="savecat1" name="T13" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="Radio2" name="Choose"
                                            type="radio" value="2" />Create a
										sheet view</td>
                                </tr>
                                <tr>
                                    <td class="style6" height="27" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <font color="#006600">
										<b>Coordinates of view</b></font><b><font color="#006600"> corner: X:</font></b>
										<input id="X1" type="text" value="0.0" class="style22" name="T4" size="20" />
										<b><font color="#006600">Y:</font></b>
										<input id="Y1" type="text" value="0.0" class="style22" name="T5" size="20" />
										<b><font color="#006600">Z:</font></b>
										<input id="Z1" type="text" value="0.0" class="style22" name="T6" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style6" height="25" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <font color="#006600">
										<b>Coordinates of opposite</b></font><b><font color="#006600">
										view
										corner:</font></b> <b>
										<font color="#006600">X:</font></b>
										<input id="X3" type="text" value="0.0" class="style22" name="T18" size="20" />
										<b><font color="#006600">Y:</font></b>
										<input id="Y3" type="text" value="0.0" class="style22" name="T19" size="20" />
										<b><font color="#006600">Z:</font></b>
										<input id="Z3" type="text" value="0.0" class="style22" name="T20" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style6" height="25" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">Name:
										<input type="text" id="name2" name="T7" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" height="23" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">Category</font><font color="#008000">:
										<input type="text" id="cat2" name="T11" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" height="25" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">Save as name:
										<input type="text" id="savename2" name="T12" size="20"> </font></b>
										</td>
                                </tr>
                                <tr>
                                    <td class="style6" height="23" style="height: 20px">
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;&nbsp;
										</b></font><b>
										<font color="#006600">Save as category:
										<input type="text" id="savecat2" name="T14" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" height="37" style="height: 20px">
                                        <input id="Button1" type="button" value="Create View" onclick="runMacro()" />

                                    </td>
                                </tr>
                            </table>
                            <div class="style19">
                                <h3 class="style20">
                                    Output</h3>
                            <textarea id="OB" cols="50" name="Output" rows="10" readonly="readonly"></textarea>
								<hr />
								<p>&nbsp;</div>
                        </form>
                    </td>
                </tr>

            </tbody>
        </table>
    <br />
    </body>
</html>
```

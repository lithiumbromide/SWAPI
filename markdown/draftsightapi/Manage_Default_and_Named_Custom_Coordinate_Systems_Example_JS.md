---
title: "Manage Custom Coordinate Systems Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm"
---

# Manage Custom Coordinate Systems Example (JS)

| This example shows how to manage World, default, and named custom coordinate systems in a DraftSight drawing. Start DraftSight. Using the following form, select an option and fill in any associated fields. Use double values for points. Click Run Macro . Inspect the Output. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,custom coordinate systems">

    <head>

    <!-- Without this line, this does not work in Internet Explorer 8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=8" />

    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

    <!-- Add your dsInterface .js Files here -->
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModel.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSketchManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsViewManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCustomCoordinateSystemManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCustomCoordinateSystem.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>

    <!-- This is the main block where you place the JavaScript API code -->
    <script type="text/javascript">
        function printOut(str) {
            document.getElementById("OB").value += str + "\n";
            document.getElementById("OB").scrollTop += document.getElementById("OB").scrollHeight;
        }

        function runMacro() {
            try {
            	document.getElementById("OB").value = "";
                apiCode();
            }
            catch (err) {
                printOut(djErrorString(err));
            }
        }
        function printCoordinateSystemParameters(dsCCS) {
        	printOut("Custom Coordinate System Parameters:");
        	printOut("Name: " + dsCCS.GetName());
        	var dsColl = dsCCS.GetDefaultCustomCoordinateSystemFlag();
        	printOut("IsDefault? " +  dsColl.IsDefault);
        	printOut("Default Custom Coordinate system flag: " + dsColl.DefaultCustomCoordinateSystemFlag);
        	var dsOrigin = dsCCS.GetOrigin();
        	printOut("Origin x coordinate: " + dsOrigin.OriginX);
        	printOut("Origin y coordinate: " + dsOrigin.OriginY);
        	printOut("Origin xz coordinate: " + dsOrigin.OriginXZ);
        	var dsXAxisDirection = dsCCS.GetXAxisDirection();
        	printOut("X axis direction x coordinate: " + dsXAxisDirection.X);
        	printOut("X axis direction y coordinate: " + dsXAxisDirection.Y);
        	printOut("X axis direction z coordinate: " + dsXAxisDirection.Z);
        	var dsYAxisDirection = dsCCS.GetYAxisDirection();
        	printOut("Y axis direction x coordinate: " + dsYAxisDirection.X);
        	printOut("Y axis direction y coordinate: " + dsYAxisDirection.Y);
        	printOut("Y axis direction z coordinate: " + dsYAxisDirection.Z);
        	var dsZAxisDirection = dsCCS.GetZAxisDirection();
        	printOut("Z axis direction x coordinate: " + dsZAxisDirection.X);
        	printOut("Z axis direction y coordinate: " + dsZAxisDirection.Y);
        	printOut("Z axis direction z coordinate: " + dsZAxisDirection.Z);
        }
        function apiCode() {
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var dsCCSManager = mDoc.GetCustomCoordinateSystemManager();
            var mViewMgr = mDoc.GetViewManager();
            if (document.inputform.Choose[0].checked){
            	// Get World CCS
            	printOut("Getting the World CCS...");
                var dsWorldCCS = dsCCSManager.GetWorldCustomCoordinateSystem();
                printCoordinateSystemParameters(dsWorldCCS);
            }
            else if (document.inputform.Choose[1].checked){
            	//Activate default Bottom CCS
            	printOut("Activating the default Bottom CCS...");
                var dsBottomCCS = dsCCSManager.GetDefaultCustomCoordinateSystem("dsDefaultCustomCoordinateSystem_Bottom");
                printCoordinateSystemParameters(dsBottomCCS);
                dsBottomCCS.Activate();
            }
            else if (document.inputform.Choose[2].checked){
            	//Change origin of active CCS
            	printOut("Changing the origin of active CCS...");
            	var originX = parseFloat(document.getElementById("X1").value);
            	var originY = parseFloat(document.getElementById("Y1").value);
            	var originZ = parseFloat(document.getElementById("Z1").value);
            	dsCCSManager.SetActiveCustomCoordinateSystemOrigin(originX, originY, originZ);
            	var dsActiveCCS = dsCCSManager.GetActiveCustomCoordinateSystem();
            	printCoordinateSystemParameters(dsActiveCCS);
            }
            else if (document.inputform.Choose[3].checked){
            	//Align active CCS with a Line
            	printOut("Aligning the active CCS with a Line...");
            	var startPoint = new Array();
            	startPoint[0] = parseFloat(document.getElementById("X2").value);
            	startPoint[1] = parseFloat(document.getElementById("Y2").value);
            	startPoint[2] = parseFloat(document.getElementById("Z2").value);
            	var endPoint = new Array();
            	endPoint[0] = parseFloat(document.getElementById("X3").value);
            	endPoint[1] = parseFloat(document.getElementById("Y3").value);
            	endPoint[2] = parseFloat(document.getElementById("Z3").value);
            	var dsLine = mSkMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2], endPoint[0], endPoint[1], endPoint[2]);
            	dsCCSManager.AlignActiveCustomCoordinateSystemByEntity(dsLine, startPoint);
            	var dsActiveCCS = dsCCSManager.GetActiveCustomCoordinateSystem();
            	printCoordinateSystemParameters(dsActiveCCS);
            }
			else if (document.inputform.Choose[4].checked){
				//Create a named CCS
				printOut("Creating a named CCS...");
            	mViewMgr.SetPredefinedView("dsPredefinedView_SWIsometric");
            	//mApp.Zoom("dsZoomRange_Fit", null, null);
            	var name = document.getElementById("newname").value;
            	var dsColl = dsCCSManager.SaveActiveViewAs(name);
            	var namedCCS = dsColl.CustomCoordinateSystem;
            	printCoordinateSystemParameters(namedCCS);
            	//Rename a CCS
            	printOut("Renaming a CCS...");
            	namedCCS.Rename(document.getElementById("nametorename").value);
            	printCoordinateSystemParameters(namedCCS);
            	// Print the list of named CCS's
            	printOut("List of named CCS's...");
            	var namedCCSList = new Array();
            	namedCCSList = dsCCSManager.GetNamedCustomCoordinateSystemList();
            	var count = namedCCSList.length;
            	var i;
            	for (i = 0; i<count; i++) {
            		namedCCS = namedCCSList[i];
            		printOut(namedCCS);
            	}
            }
            else if (document.inputform.Choose[5].checked) {
            	//Remove a CCS
            	printOut("Removing a named CCS...");
            	var removename = document.getElementById("removename").value;
            	dsCCSManager.RemoveCustomCoordinateSystem(removename);
            	// Print the list of named CCS's (should be one less now)
            	printOut("Current list of named CCS's...");
            	var namedCCSList = new Array();
            	namedCCSList = dsCCSManager.GetNamedCustomCoordinateSystemList();
            	if (namedCCSList != null) {
            		var count = namedCCSList.length;
            		var i;
            		for (i = 0; i<count; i++) {
            			namedCCS = namedCCSList[i];
            			printOut(namedCCS);
            		}
            	}
            }

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Manage Custom Coordinate Systems Example (JS)</title>

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

    <H1>Manage Custom Coordinate Systems Example (JS)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to manage World, default, and named
							custom coordinate systems in a DraftSight drawing.<ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form, select an option and fill in any associated
							fields. Use double values for points.<li>Click <b>Run Macro</b>.<li>Inspect the
							Output.</ol>
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
										near the top of the webpage and select <b>
										Allow Blocked Content</b>.</li>
									</ol>
								</blockquote></div>
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3" style="width: 650px">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Get
										World Coordinate System</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R2" type="radio" name="Choose" value="2">Activate
										default bottom custom coordinate system</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R3" type="radio" name="Choose" value="3">Change
										origin of active custom coordinate
										system:</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; X:
										<input id="X1" type="text" name="T5" size="10">
										Y:
										<input id="Y1" type="text" name="T6" size="9">
										Z:
										<input id="Z1" type="text" name="T7" size="10"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R4" type="radio" name="Choose" value="4">Align
										active custom coordinate system with the
										following
										line:</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Start point: X:
										<input id="X2" type="text" name="T8" size="10">
										Y:
										<input id="Y2" type="text" name="T9" size="11">
										Z:
										<input id="Z2" type="text" name="T10" size="11"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; End point: X:
										<input id="X3" type="text" name="T11" size="11">
										Y:
										<input id="Y3" type="text" name="T12" size="11">
										Z:
										<input id="Z3" type="text" name="T13" size="11"></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="R5" name="Choose"
                                            type="radio" value="5" />Create
										custom coordinate system named:
										<input id="newname" type="text" name="T1" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Rename:</font></b>
										<input id="nametorename" type="text" name="T2" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">
										<input id="R6" type="radio" name="Choose" value="6"/>Remove
										custom coordinate system named:</font></b>
										<input id="removename" type="text" name="T3" size="20"></td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Run Macro" onclick="runMacro()" />

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

---
title: "Insert Block, Notes, and Sketch Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm"
---

# Insert Block, Notes, and Sketch Entities Example (JS)

## Insert Block, Notes, and Sketch Entities Example (JavaScript)

| This example creates and inserts a Block, Notes with parameters, and sketch entities that display a compass with an arrow pointing in the selected direction in a DraftSight drawing. Start DraftSight. Using the following form, select the direction of the arrow and create the compass: Select the direction in which to point the arrow (e.g., N, NE, E , etc.) in Direction of arrow . Specify where to create the compass: Select Coordinates . Type x, y, and z coordinates. Click Insert . - or - Select Point in drawing. Click Insert . Click anywhere in the drawing to insert the compass at that point. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Block definitions">
<meta name=MS-HKWD content="JavaScript examples,2D PolyLines">
<meta name=MS-HKWD content="JavaScript examples,rotate entities">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,Notes">
<meta name=MS-HKWD content="JavaScript examples,Circles">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,models">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCommandMessage.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsNote.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockDefinition.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockInstance.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>

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
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            if (document.inputform.Choose[0].checked){
                //This is for the "Type coordinates" option
                //You must add text boxes in the HTML file to implement this option
                var X = parseFloat(document.getElementById("X").value);
                var Y = parseFloat(document.getElementById("Y").value);
                var Z = parseFloat(document.getElementById("Z").value);
            }
            else if (document.inputform.Choose[1].checked){
                var dsPoint = mCom.PromptForPoint("Insert at point in drawing");
                //This is for the "Insert at point in drawing" option
                //You must assign dsPoint.X, dsPoint.Y, and dsPoint.Z to the same variables
                //that are assigned in the "Type coordinates" option
                var X = dsPoint.X;
                var Y = dsPoint.Y;
                var Z = dsPoint.Z;
            }
            var checkBlock = mDoc.GetBlockDefinitions();
            var useExist = 0;
            for (var i in checkBlock) {
                if (checkBlock[i].GetName() == "Compass"){
                    useExist = 1;
                }
            }
            if (useExist == 1) {
                var block = mSkMgr.InsertBlock2("Compass", X, Y, Z, 1, 1, 1, 0);
            } else {
                var narray = new Array();
                var sarray = new Array();
                var earray = new Array();
                var warray = new Array();
                narray[0] = "N";
                sarray[0] = "S";
                earray[0] = "E";
                warray[0] = "W";
                var north = mSkMgr.InsertNoteWithParameters(X, Y + 4, 0, X + 5, Y + 4, 0, narray, 0, 1, "dsNoteJustification_MiddleCenter", "dsNoteLineSpacingStyle_AtLeast", 1, "Standard", 10);
                var south = mSkMgr.InsertNoteWithParameters(X, Y - 4, 0, X + 5, Y - 4, 0, sarray, 0, 1, "dsNoteJustification_MiddleCenter", "dsNoteLineSpacingStyle_AtLeast", 1, "Standard", 10);
                var west = mSkMgr.InsertNoteWithParameters(X - 4, Y, 0, X, Y, 0, warray, 0, 1, "dsNoteJustification_MiddleCenter", "dsNoteLineSpacingStyle_AtLeast", 1, "Standard", 10);
                var east = mSkMgr.InsertNoteWithParameters(X + 4, Y, 0, X + 6, Y, 0, earray, 0, 1, "dsNoteJustification_MiddleCenter", "dsNoteLineSpacingStyle_AtLeast", 1, "Standard", 10);
                var circle = mSkMgr.InsertCircle(X, Y, Z, 5);
                var longarray = new Array();
                var entityarray = new Array();
                longarray[0] = 30;
                longarray[1] = 30;
                longarray[2] = 30;
                longarray[3] = 30;
                longarray[4] = 22;
                entityarray[0] = north;
                entityarray[1] = south;
                entityarray[2] = west;
                entityarray[3] = east;
                entityarray[4] = circle;
                var block = mDoc.CreateBlockDefinition("Compass", "This contains the shape of the compass", X, Y, Z, longarray, entityarray, "dsBlockDefinitionEntities_ConvertToBlock");
            }
            //Find a way to get the arrow to revolve around
            var direction = parseFloat(document.getElementById("D").value);
            var arrowarray = new Array();
            arrowarray[0] = X - 0.5;
            arrowarray[1] = Y - 1;
            arrowarray[2] = X + 0.5;
            arrowarray[3] = Y - 1;
            arrowarray[4] = X + 0.5;
            arrowarray[5] = Y + 1;
            arrowarray[6] = X + 1;
            arrowarray[7] = Y + 1;
            arrowarray[8] = X;
            arrowarray[9] = Y + 2;
            arrowarray[10] = X - 1;
            arrowarray[11] = Y + 1;
            arrowarray[12] = X - 0.5;
            arrowarray[13] = Y + 1;
            var arrow = mSkMgr.InsertPolyline2D(arrowarray, true);
            var long2 = new Array();
            var entity2 = new Array();
            long2[0] = 27;
            entity2[0] = arrow;
            //mSkMgr.Mirror(X, Y + 2, 0, X, Y - 1, 0, false, long2, entity2);
            mSkMgr.RotateEntities(X, Y, direction, long2, entity2);
            //Type your JavaScript API code here
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Insert Block, Notes, and Sketch Entities Example (JS)</title>

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
            color: #006600;
            font-weight: bold;
        }
        .style22
        {
            width: 50px;
        }
    </style>

    </head>

    <H1>Insert Block, Notes, and Sketch Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example creates and inserts a Block,
							Notes with parameters, and sketch entities that
							display a compass with an arrow pointing in the
							selected direction in a DraftSight drawing.&nbsp;<ol>
                            <li>Start DraftSight.<li>Using
							the following form, select the direction of the
							arrow and create the compass:</ol>
							<blockquote>
								<ol>
									<li>Select the direction in which to point the arrow
							(e.g., <b>N, NE, E</b>, etc.) in <b>Direction of
									arrow</b>.</li>
                            </li>
									<li>Specify where to create the compass:</li>
								</ol>
								<blockquote>
									<ol>
										<li>Select <b>Coordinates</b>.</li>
										<li>Type x, y, and z coordinates.</li>
										<li>Click <b>Insert</b>.</li>
                            			<ul>- or -</ul>
									</ol>
									<ol>
										<li>Select <b>Point in drawing.</b></li>
										<li>Click <b>Insert</b>.</li>
										<li>Click anywhere in the drawing to insert the
										compass at that point.</li>
									</ol>
								</blockquote>
								<ol start="2">
									<li>Examine the drawing.</li>
								</ol>
							</blockquote>
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
                            <table class="style3">
                                <!-- Reuse this row to add more rows-->
                                <tr>
                                    <!-- Use these two cells to implement inputs, add more rows if necessary-->
                                    <td class="style21" width="285">
                                        Direction of arrow:<!-- Use this cell to name the input-->
                                    </td>
                                    <td class="style5" width="48">
                                        <!-- Use this cell to place a form element-->
                                        <select id="D" name="Directon">
                                            <option value="0">N</option>
                                            <option value="5.498">NE</option>
                                            <option value="4.712">E</option>
                                            <option value="3.927">SE</option>
                                            <option value="3.142">S</option>
                                            <option value="2.356">SW</option>
                                            <option value="1.571">W</option>
                                            <option value="0.785">NW</option>
                                        </select></td>
                                    <td ></td>
                                </tr>
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Coordinates</td>
                                </tr>
                                <tr>
                                      <td class="style4" colspan="2">
                                        &nbsp;&nbsp;&nbsp;
                                        X:
										<input id="X" type="text" value="0.0" class="style22" name="T1" size="20" />&nbsp;&nbsp;&nbsp;
										Y:
										<input id="Y" type="text" value="0.0" class="style22" name="T2" size="20" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Z:
										<input id="Z" type="text" value="0.0" class="style22" name="T3" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="Radio2" name="Choose"
                                            type="radio" value="2" />Point in drawing</td>
                                </tr>
                                <tr>
                                    <td colspan="2" class="style6">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td colspan="2" class="style6">
                                        <input id="Button1" type="button" value="Insert" onclick="runMacro()" />

                                    </td>
                                </tr>
                            </table>
                            <div class="style19">
                                <h3 class="style20">
                                    Output</h3>
                            <textarea id="OB" cols="50" name="Output" rows="10" readonly="readonly"></textarea>
                            	</div>
                        </form>
                        									<hr />
                    </td>
                </tr>
            </tbody>
        </table>
    <br />
    </body>
</html>
```

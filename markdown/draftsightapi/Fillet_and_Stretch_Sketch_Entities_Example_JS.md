---
title: "Fillet and Stretch Sketch Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Fillet_and_Stretch_Sketch_Entities_Example_JS.htm"
---

# Fillet and Stretch Sketch Entities Example (JS)

## Fillet and Stretch Sketch Entities Example (JavaScript)

| This example shows how to fillet and stretch sketch entities. Start DraftSight and open a new drawing. Using the following form: Select Create and fillet one pair of sketch entities . Click Run Macro . - or - Select Create and stretch three sketch entities. Click Run Macro. Inspect the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples, fillet entities">
<meta name=MS-HKWD content="JavaScript examples, stretch entities">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircleArc.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>

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
            mApp.AbortRunningCommand()
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            var choice;

           if (document.inputform.Choose[0].checked){
                var firstPointOnEntityArray = new Array();
                var firstEntityArray = new Array();
                var secondPointOnEntityArray = new Array();
                var secondEntityArray = new Array();

                // Draw entities to fillet
            	var entityIndex = 0;
            	var coordinateIndex = 0;

            	// Draw a Line
            	var startPoint = new Array();
            	startPoint[0] = 0;
            	startPoint[1] = 0;
            	startPoint[2] = 0;
            	var endPoint = new Array();
            	endPoint[0] = 5;
            	endPoint[1] = 0;
            	endPoint[2] = 0;
            	var dsLine = mSkMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2], endPoint[0], endPoint[1], endPoint[2]);

            	// Add Line to output arrays
            	firstEntityArray[entityIndex] = dsLine;
            	firstPointOnEntityArray[coordinateIndex] = endPoint[0];
            	firstPointOnEntityArray[coordinateIndex + 1] = endPoint[1];
            	firstPointOnEntityArray[coordinateIndex + 2] = endPoint[2];

            	// Draw an Arc
            	var radius = 1;
            	var centerPoint = new Array();
            	centerPoint[0] = 2;
            	centerPoint[1] = -1;
            	centerPoint[2] = 0;
            	var startAngle = 3.14;
            	var endAngle = 1.5 * startAngle;
            	var dsArc = mSkMgr.InsertArc(centerPoint[0], centerPoint[1], centerPoint[2], radius, startAngle, endAngle);

            	// Add Arc to output arrays
            	secondEntityArray[entityIndex] = dsArc;
            	secondPointOnEntityArray[coordinateIndex] = centerPoint[0] - radius;
            	secondPointOnEntityArray[coordinateIndex + 1] = centerPoint[1];
            	secondPointOnEntityArray[coordinateIndex + 2] = centerPoint[2];

            	// Set fillet radius
            	var setResult = mDoc.SetCommandOptionDouble("dsCommandOptionDouble_SetFltRad", 1);
            	mSkMgr.FilletEntities(firstPointOnEntityArray, firstEntityArray, secondPointOnEntityArray, secondEntityArray);

            	var lowerLeftArray = [0,0,0];
            	var upperRightArray = [0,0,0];
            	mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);
            }
            else if (document.inputform.Choose[1].checked){
                var displacementX = 4.0;
                var displacementY = 6.0;
                var displacementZ = 0.0;
                var dsEntities = new Array();
                var crossingBoxStartCorner = new Array();
                var crossingBoxEndCorner = new Array();

                // Draw entities to stretch
                var entitiesIndex = 0;

                // Draw PolyLine
                var closed = true;
                var coordinates = new Array();
                coordinates[0] = 1;
                coordinates[1] = 1;
				coordinates[2] = 3;
				coordinates[3] = 1;
				coordinates[4] = 3;
				coordinates[5] = 3;
				coordinates[6] = 1;
				coordinates[7] = 3;
            	var dsPolyline = mSkMgr.InsertPolyline2D(coordinates, closed);
            	// Add PolyLine to output array of entities
            	dsEntities[entitiesIndex] = dsPolyline;
            	entitiesIndex = entitiesIndex + 1;

            	// Draw Line
            	var startPoint = new Array();
            	startPoint[0] = 4;
            	startPoint[1] = 1;
				startPoint[2] = 0;
				var endPoint = new Array();
				endPoint[0] = 4;
				endPoint[1] = 5;
				endPoint[2] = 0;
            	var dsLine = mSkMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2], endPoint[0], endPoint[1], endPoint[2]);
            	// Add Line to output array of entities
            	dsEntities[entitiesIndex] = dsLine;
            	entitiesIndex = entitiesIndex + 1;

            	// Draw Circle
            	var radius = 1;
            	var centerPoint = new Array();
            	centerPoint[0] = 6;
            	centerPoint[1] = 2;
				centerPoint[2] = 0;

            	var dsCircle = mSkMgr.InsertCircle(centerPoint[0], centerPoint[1], centerPoint[2], radius);
            	// Add Circle to output array of entities
            	dsEntities[entitiesIndex] = dsCircle;
            	entitiesIndex = entitiesIndex + 1;

            	crossingBoxStartCorner[0] = 0.6;
            	crossingBoxStartCorner[1] = 2;
            	crossingBoxStartCorner[2] = 0;
            	crossingBoxEndCorner[0] = 8;
            	crossingBoxEndCorner[1] = 6;
            	crossingBoxEndCorner[2] = 0;

            	mSkMgr.StretchEntities(displacementX, displacementY, displacementZ, dsEntities, crossingBoxStartCorner, crossingBoxEndCorner);

            	var lowerLeftArray = [0,0,0];
            	var upperRightArray = [0,0,0];
            	mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);
            }

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title> Fillet and Stretch Sketch Entities Example (JS)</title>

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

    <H1> Fillet and Stretch Sketch Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to fillet and stretch sketch entities.
                            <ol>
                            <li>Start DraftSight and open a new drawing.</li>
                            <li>Using the following form:<ol>
                            <li>Select <b>Create and fillet one pair of
							sketch entities</b>.</li>
							<li>Click <b>Run Macro</b>.</li>
                            </ol>
							<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - or -</ol>
							<p></p>
							<blockquote>
								<ol>
									<li>Select <b>Create and stretch three
									sketch entities.</b></li>
									<li>Click <b>Run Macro.</b></li>
								</ol>
								<p></p>
							</blockquote>
							<ol start="3">
								<li>Inspect the drawing.</li>
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
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="Radio1" type="radio" name="Choose" checked="true" value="1"/>Create
										and fillet one pair of sketch
										entities</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        <input id="Radio2" name="Choose"
                                            type="radio" value="2" />Create and
										stretch three sketch entities</td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        &nbsp;</td>
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

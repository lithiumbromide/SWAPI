---
title: "Add and Modify Custom Data Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_and_Modify_Custom_Data_Example_JS.htm"
---

# Add and Modify Custom Data Example (JS)

## Add and Modify Custom Data Example (JavaScript)

| This example constructs a Circle in a DraftSight drawing and adds custom data to the Circle. Start DraftSight. Using the following form, specify the center point and radius for the Circle and the custom data's application name: Type the x, y, and z coordinates for the center point of the Circle in Center point X , Center point Y , and Center point Z . Type a radius for the Circle in Radius . Type an application name (maximum of 50 characters) for the custom data in Application name . Click Insert . Examine the drawing to verify that the Circle was constructed. Examine the Output field in the form to verify that custom data was added and modified. NOTES: Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,models">
<meta name=MS-HKWD content="JavaScript examples,Circles">
<meta name=MS-HKWD content="JavaScript examples,custom data">
<meta name=MS-HKWD content="JavaScript examples,zoom">

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
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCustomData.js"></script>

    <!-- This is the main block where you place the JavaScript API -->
    <script type="text/javascript">

			function printOut(str) {
			    document.getElementById("OB").value += str + "\n";
			    document.getElementById("OB").scrollTop += document.getElementById("OB").scrollHeight;
			}

			function runMacro() {

			    //This catches any errors and exits out of the code if caught
			    //Errors are displayed in Output field of form
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
			    mApp.AbortRunningCommand();
			    var mDoc = mApp.GetActiveDocument();
			    var mModel = mDoc.GetModel();
			    var mSkMgr = mModel.GetSketchManager();
			    var X = parseFloat(document.getElementById("X").value);
			    var Y = parseFloat(document.getElementById("Y").value);
			    var Z = parseFloat(document.getElementById("Z").value);
			    var R = parseFloat(document.getElementById("R").value)
			    var mCircle = mSkMgr.InsertCircle(X, Y, Z, R);

			    //Play around with the custom data
			    var appName = document.getElementById("A").value;

			    //Begin the custom data coding
			    var custom1 = mCircle.GetCustomData(appName);

			    var index = 0;
			    var marker = 1000;

			    printOut("Custom data...");
			    printOut(" ");

			    //Testing string, marker, and type
			    custom1.InsertStringData(index, marker, "Circle entity");
			    var testString = custom1.GetStringData(index);
			    printOut("  Original string: " + JSON.stringify(testString));
			    custom1.SetStringData(index, "Circle entity changed");
			    testString = custom1.GetStringData(index);
			    printOut("  Modified string: " + JSON.stringify(testString));
			    var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    var testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
			    printOut(" ");

			    //Testing double
			    index = 1;
			    marker = 1021;
			    custom1.InsertDoubleData(index, marker, 7.0);
			    var testDouble = custom1.GetDoubleData(index);
			    printOut("  Original double: " + JSON.stringify(testDouble));
			    custom1.SetDoubleData(index, 12.0);
			    testDouble = custom1.GetDoubleData(index);
			    printOut("  Modified double: " + JSON.stringify(testDouble));
			    var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
   			    printOut(" ");

			    //Testing Int16 and Int32
			    index = 2;
			    marker = 1070;
			    custom1.InsertInteger16Data(index, marker, 10);
			    var testInt16 = custom1.GetInteger16Data(index);
			    printOut("  Original Int16: " + JSON.stringify(testInt16));
			    custom1.SetInteger16Data(index, 20);
			    testInt16 = custom1.GetInteger16Data(index);
			    printOut("  Modified Int16: " + JSON.stringify(testInt16));
			     var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
			    printOut(" ");

			    index = 3;
			    marker = 1071;
			    custom1.InsertInteger32Data(index, marker, 30);
			    var testInt32 = custom1.GetInteger32Data(index);
			    printOut("  Original Int32: " + JSON.stringify(testInt32));
			    custom1.SetInteger32Data(index, 40);
			    testInt32 = custom1.GetInteger32Data(index);
   			    printOut("  Modified Int32: " + JSON.stringify(testInt32));
			    var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
			    printOut(" ");

			    //Testing the Layer name
			    index = 4;
			    marker = 1003;
			    custom1.InsertLayerName(index, "Original Layer name");
			    var testLayer = custom1.GetLayerName(index);
			    printOut("  Original Layer name: " + JSON.stringify(testLayer));
			    custom1.SetLayerName(index, "Modified Layer name");
			    testLayer = custom1.GetLayerName(index);
			    printOut("  Modified Layer name: " + JSON.stringify(testLayer));
			    var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
			    printOut(" ");

			    //Testing the byte array
			    index = 5;
			    marker = 1004;
			    var bArray = new Array();
			    bArray[0] = 3;
			    bArray[1] = 4;
			    bArray[2] = 5;
			    bArray[3] = 6;
			    custom1.InsertByteData(index, bArray);
			    var testArray = custom1.GetByteData(index);
			    for(var i = 0; i<testArray.length; i++){
			    	var arrElement = testArray[i];
			    	printOut("  Original binary data element " + i + ": " + JSON.stringify(arrElement));
			    }
			    var cArray = new Array();
			    cArray[0] = 9;
			    cArray[1] = 10;
			    cArray[2] = 11;
			    cArray[3] = 12;
			    custom1.SetByteData(index, cArray);
			    testArray = custom1.GetByteData(index);
			    for(var i = 0; i<testArray.length; i++){
			    	var arrElement = testArray[i];
			    	printOut("  Modified binary data element " + i + ": " + JSON.stringify(arrElement));
			    }
			    var testMarker = custom1.GetDataMarker(index);
			    printOut("  Marker: " + JSON.stringify(testMarker));
			    testType = custom1.GetDataType(index);
			    printOut("  Data type: " + JSON.stringify(testType));
			    printOut(" ");

			    //Print number of custom data;
			    index =  custom1.GetDataCount();
			    printOut("  Number of custom data added to Circle: " + String(index));

            	var lowerLeftArray = [0,0,0]
            	var upperRightArray = [0,0,0]
            	mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

			    mApp.releaseAll();
			}

</script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Add and Modify Custom Data Example (JS)</title>

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
            color: #006600;
            font-weight: bold;
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

    <H1>Add and Modify Custom Data Example (JavaScript)</H1>

       <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example constructs a Circle in a DraftSight
							drawing and adds custom data to the Circle.
							<ol>
                            <li>Start DraftSight.<li>
							Using the following form, specify the center point
							and radius for the Circle and the custom data's
							application name:<ol>
								<li>Type the x, y, and z coordinates for the
								center point of the Circle in <b>Center point X</b>,
								<b>Center point Y</b>, and <b>Center point Z</b>.</li>
								<li>Type a radius for the Circle in <b>Radius</b>.</li>
								<li>Type an application name (maximum of 50
								characters) for the custom data in <b>
								Application name</b>.</li>
								<li>Click <b>Insert</b>.</li>
							</ol>
							</li>
							<li>Examine the drawing to verify that the
								Circle was constructed.</li>
							<li>Examine the Output field in the form to verify
							that custom data was added and modified.</li>
                            </ol>
							<p><b>NOTES:</b></p>
								<ul>
									<li>Errors are also printed to Output.</li>
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
                            <table class="style3" width="460">
                                <!-- Reuse this row to add more rows-->
                                <tr>
                                    <td class="style20" width="306">
                                    <b>Center point X:</b>
                                    <input type="text" name="CenterX" id="X" value="30.0" size="8" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
                                    <b>Center point Y:</b>
                                    <input type="text" name="CenterY" id="Y" value="30.0" size="8" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
                                    <b>Center point Z:</b>
									<input type="text" name="CenterZ" id="Z"  value="0.0" size="8" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
 									&nbsp;</td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
 									<b>Radius:</b>
 									<input type="text" name="Radius" id="R"  value="10.0" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
 									&nbsp;</td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
									<b>Application name: </b>
									<input type="text" name="App" id="A" value="Name" size="50" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
									&nbsp;</td>
                                </tr>

                                <tr>
									<td class="style6">
									<button id="Button1" type="button" onclick="runMacro()">Insert</button></td>
								</tr>

                            </table>

                            <div class="style19">
                                <h3 class="style20">
                                	Output</h3>
                            			<textarea id="OB" cols="75" name="Output" rows="10" readonly="readonly"></textarea>
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

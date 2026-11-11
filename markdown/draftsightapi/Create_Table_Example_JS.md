---
title: "Create Table Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Table_Example_JS.htm"
---

# Create Table Example (JS)

## Create Table Example (JavaScript)

| This example shows how to change the transparency of the active Layer, create a TableStyle and Table, and change the background colors of the top row and a cell in the Table. Start DraftSight. Using the following form, type: X coordinate for the upper-left corner of the Table. Y coordinate for the upper-left corner of the Table. number of rows for the Table. number of columns for the Table. Click Create Table . Examine the drawing document and Output. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click Allow Blocked Content on the information bar. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Tables">
<meta name=MS-HKWD content="JavaScript examples,TableStyles">
<meta name=MS-HKWD content="JavaScript examples,TableStyle Manager">
<meta name=MS-HKWD content="JavaScript examples,Layers">
<meta name=MS-HKWD content="JavaScript examples,transparency">
<meta name=MS-HKWD content="JavaScript examples,Colors">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsTable.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsTableStyle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsTableStyleManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLayer.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLayerManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsTransparency.js"></script>

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
            mApp.AbortRunningCommand();

            //User input values
            var X = parseFloat(document.getElementById("X").value);
            var Y = parseFloat(document.getElementById("Y").value);
            var X0 = parseFloat(document.getElementById("X0").value);
            var Y0 = parseFloat(document.getElementById("Y0").value);

            //Create the TableStyle
            var mDoc = mApp.GetActiveDocument();

            //Get how transparency is defined
            var mLayerManager = mDoc.GetLayerManager();
            var mLayer = mLayerManager.GetActiveLayer();
            var percentage = mLayer.get_Transparency();
            printOut("Transparency percentage for active Layer: " + JSON.stringify(percentage));

            //Set new transparency percentage for the active Layer
            var newPercentage = 50;
            mLayer.put_Transparency(newPercentage);
            var newPercentage = mLayer.get_Transparency();
            printOut("New transparency percentage for active Layer: " + JSON.stringify(newPercentage));

            var mTableStyleManager = mDoc.GetTableStyleManager();
            var sampleTableStyle = "Sample Table Style";
            var collTableStyle = mTableStyleManager.CreateTableStyle(sampleTableStyle);

            //Set the TableStyle styles
            //Create the Table in a downward direction
            collTableStyle.TableStyle.put_HeaderOrientation("dsTableHeaderOrientation_Down");

            //Set the Colors for the Table
            var mColorHeader = collTableStyle.TableStyle.GetBackgroundColor("dsTableCellType_Header");
        	mColorHeader.SetNamedColor("dsNamedColor_Cyan");
        	collTableStyle.TableStyle.SetBackgroundColor("dsTableCellType_Header", mColorHeader);

        	var mColorData = collTableStyle.TableStyle.GetBackgroundColor("dsTableCellType_Data");
			mColorData.SetNamedColor("dsNamedColor_Green");
		    collTableStyle.TableStyle.SetBackgroundColor("dsTableCellType_Data", mColorData);

			var mColorTitle = collTableStyle.TableStyle.GetBackgroundColor("dsTableCellType_Title");
			mColorTitle.SetNamedColor("dsNamedColor_White");
			collTableStyle.TableStyle.SetBackgroundColor("dsTableCellType_Title", mColorTitle);

            //Activate the TableStyle
			collTableStyle.TableStyle.Activate();

			//Get the model document
			var mModel = mDoc.GetModel();

			//Get the Sketch Manager
			var mSketchManager = mModel.GetSketchManager();

			//Insert the Table
			var rowHeight = 2;
			var colWidth = 4;
			var mTable = mSketchManager.InsertTable(X, Y, X0, Y0, rowHeight, colWidth, "dsTableCellType_Title", "dsTableCellType_Header", "dsTableCellType_Data");

			//Get transparency object for Table
			var mTransparency = mTable.get_Transparency();
			//Find out if Table's transparency ByLayer
			printOut("Transparency defined ByLayer: " + mTransparency.IsByLayer());
			//If not, then change Table's transparency to ByLayer and
			//update Table's transparency object
			if (mTransparency.IsByLayer() != true){
				mTransparency.SetByLayer();
				printOut("Transparency now ByLayer: " + dsTransparency.IsByLayer());
				//Update Table's transparency object
				dsTable.put_Transparency(dsTransparency);
			}

			//Change Table's top row's background color
			mColorTitle.SetNamedColor("dsNamedColor_Yellow");
			mTable.SetBackgroundColor("dsTableCellType_Title", mColorTitle);
			//Change background color of cell in second roww and second column
			//to match the top ro's background color
			mTable.SetCellBackgroundColor(1, 1, mColorTitle);

            printOut("Name of TableStyle: " + collTableStyle.TableStyle.get_Name());

            //Zoom to fit
            var lowerLeftArray = [2,0,0]
            var upperRightArray = [0,0,0]
            mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Create Table Example (JS)</title>

    <!-- This style formats the heading -->
    <style type="text/css">
     H1 {
	border-top:1px none ##ccccff; border-bottom:1px solid #808080; font-weight: bold;
	font-size: 10pt;
	font-family: Verdana, sans-serif;
	/*border-left-style: Inset;*/
	/*border-right-style: Inset;*/
	/*border-bottom-style: none;*/
	padding-top: 4pt;
	padding-bottom: 4pt;
	border-left-color: ##ccccff;
	border-right-color: ##ccccff;
	/*border-bottom-color: ##ccccff;*/
	margin-top: -15pt;
	text-indent: .15in;
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

    <H1> Create Table Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to change the transparency of
							the active Layer, create a TableStyle and Table, and
							change the background colors of the top row and a
							cell in the Table.<ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form, type:<ol type="a">
                            <li>X coordinate for the upper-left corner of the Table.</li>
							<li>Y coordinate for the upper-left corner of the Table.</li>
							<li>number of rows for the Table.</li>
							<li>number of columns for the Table.</li>
                            </ol></li>
							<li>Click <b>Create Table</b>.</li>
							<li>Examine the drawing document and Output.</li>
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
										<li>If using Windows Internet Explorer
										and running scripts is blocked, click <b>
										Allow Blocked Content</b> on the
										information bar.</li>
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
                                        Coordinates for upper-left corner:</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        X: <input id="X" type="text" value="0.0" class="style22" /> Y: <input id="Y" type="text" value="0.0" class="style22" /> </td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        Number of rows and columns:</td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;&nbsp; <font color="#006600"><b>
										Rows</b></font><b><font color="#006600">:</font></b>
										<input id="X0" type="text" value="0" class="style22" name="T1" size="20" />
										<font color="#006600"><b>Columns</b></font><b><font color="#006600">:</font></b>
										<input id="Y0" type="text" value="0" class="style22" name="T2" size="20" />
										</td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Create Table" onclick="runMacro()" />

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

---
title: "Mirror Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Mirror_Entities_Example_JS.htm"
---

# Mirror Entities Example (JS)

## Mirror Entities Example (JavaScript)

| This example creates a sketch that resembles a tee shirt by inserting and mirroring sketch entities. Start DraftSight. Using the following form: Select the size of the tee shirt in Size . Specify where to place the tee shirt: Select Coordinates . Type x, y, and z coordinates. Click Insert . - or - Select Point in drawing. Click Insert . Click anywhere in the drawing to insert the tee shirt at that point. The tee shirt is shown and zoomed to fit. Examine the drawing. NOTES: The width, height, and the point where the tee shirt was placed are printed to Output. Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,Splines">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,models">
<meta name=MS-HKWD content="JavaScript examples,2D PolyLines">
<meta name=MS-HKWD content="JavaScript examples,Arcs">
<meta name=MS-HKWD content="JavaScript examples,mirror entities">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCommandMessage.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircleArc.js"></script>

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
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            if (document.inputform.Choose[0].checked){
                //This is for the "Enter Coordinates" option
                //You must add textboxes in the html file in order to implement this option
                var X = parseFloat(document.getElementById("X").value);
                var Y = parseFloat(document.getElementById("Y").value);
                var Z = parseFloat(document.getElementById("Z").value);
            }
            else if (document.inputform.Choose[1].checked){
                var dsPoint = mCom.PromptForPoint("Select the center of the t-shirt");
                //This is for the "Select on Screen" option
                //You must assign dsPoint.X, dsPoint.Y, and dsPoint.Z to the same variables
                //that are assigned in the "Enter Coordinates" option
                var X = dsPoint.X;
                var Y = dsPoint.Y;
                var Z = dsPoint.Z;
            }
            var size = document.getElementById("S").value;
            var W = 0;
            var H = 0;
            //Units are in centimeters
            if (size == "Small") {
                W = 45;
                H = 65;
            }
            else if (size == "Medium") {
                W = 55;
                H = 75;
            }
            else if (size == "Large") {
                W = 65;
                H = 85;
            }
            else if (size == "X-Large") {
                W = 75;
                H = 95;
            }
            else if (size == "XX-Large") {
                W = 85;
                H = 105;
            }
            var halfShirt = new Array();
            halfShirt[0] = X;
            halfShirt[1] = Y - H/2;
            halfShirt[2] = X + W/2;
            halfShirt[3] = Y - H/2;
            halfShirt[4] = X + W/2;
            halfShirt[5] = Y + H/4;
            halfShirt[6] = X + 3*W/4;
            halfShirt[7] = Y;
            halfShirt[8] = X + W;
            halfShirt[9] = Y + H/8;
            halfShirt[10] = X + W/2;
            halfShirt[11] = Y + H/2;
            halfShirt[12] = X + W/4;
            halfShirt[13] = Y + H/2;
            var shirtLine = mSkMgr.InsertPolyline2D(halfShirt, false);
            var collar = mSkMgr.InsertArc(X, Y + H/2, 0, W/4, 3/2*Math.PI, 2*Math.PI);
            var entityarray = new Array();
            var longarray = new Array();
            entityarray[0] = shirtLine;
            entityarray[1] = collar;
            longarray[0] = 27;
            longarray[1] = 23;
            mSkMgr.MirrorEntities(X, Y + H/2, 0, X, Y - H/2, 0, false, longarray, entityarray);
            printOut("Width: " + W + " Height: " + H);
            printOut("X: " + X + " Y: " + Y + " Z: " + Z);

            var lowerLeftArray = [0,0,0]
            var upperRightArray = [0,0,0]
            mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Mirror Entities Example (JS)</title>

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

    <H1>Mirror Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example creates a sketch that resembles a tee
							shirt by inserting and mirroring sketch entities.<ol>
                            <li>Start DraftSight.<li>
							Using the following form:<ol>
                            <li>Select the size of the tee shirt in <b>Size</b>.</li>
							<li>Specify where to place the tee
							shirt:
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
								tee shirt at that
							point.<br>
								<br>
								The tee shirt is shown and zoomed to fit.<br>
&nbsp;</li>
							</ol></li>
                            </ol>
								<li>Examine the drawing.</li>
                            </ol>
								<p><b>NOTES:</b></p>
								<ul>
									<li>The width, height, and the point where
									the tee shirt was placed are printed to
									Output. Errors are also printed to Output.</li>
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
                                    <!-- Use these two cells to implement inputs, add more rows if necessarily-->
                                    <td class="style4" width="52">
                                        Size:</td>
                                    <td class="style5" width="398">
                                        <!-- Use this cell to place a form element-->
                                        <select id="S" name="Size">
                                            <option value="Small">Small</option>
                                            <option value="Medium">Medium</option>
                                            <option value="Large">Large</option>
                                            <option value="X-Large">X-Large</option>
                                            <option value="XX-Large">XX-Large</option>
                                        </select></td>
                                </tr>
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Coordinates&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;&nbsp;&nbsp;
                                        X: <input id="X" type="text" value="0.0" class="style22" /> Y: <input id="Y" type="text" value="0.0" class="style22" /> Z: <input id="Z" type="text" value="0.0" class="style22" /></td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R2" name="Choose"
                                            type="radio" value="2" />Point in
										drawing</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
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

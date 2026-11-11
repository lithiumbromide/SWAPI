---
title: "Insert and Dimension Sketch Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_and_Dimension_Sketch_Example_JS.htm"
---

# Insert and Dimension Sketch Example (JS)

## Insert and Dimension Sketch Example (JavaScript)

| This example inserts and dimensions a sketch similar to the following image. In the DraftSight drawing, Dimension values are shown instead of the text shown in the image. Start DraftSight. Using the following form, specify how to create the sketch and where to place it in the drawing: Type a diameter in Diameter of large Arc . Type a diameter in Diameter of small Arc . Type the distance between the center points of the Arcs in Distance between center points . Insert the center points: Select Center point coordinates . Type the x, y, and z coordinates for the center point of the large Arc. Click Insert . - or - Select Center point in drawing. Click Insert . Click anywhere in the drawing to insert the center point for the large Arc and to insert the sketch. Examine the drawing. NOTES: The coordinates of the center points are printed to Output. Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,Dimensions">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,models">
<meta name=MS-HKWD content="JavaScript examples,Arcs">
<meta name=MS-HKWD content="JavaScript examples,Lines">
<meta name=MS-HKWD content="JavaScript examples,DimensionStyles">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircleArc.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDiameterDimension.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsAlignedDimension.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsGeneralDimension.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleTextOptions.js"></script>

    <!-- This is the main block where you place the JavaScript API code -->
    <script type="text/javascript">
        function printOut(str) {
            document.getElementById("OB").value += str;
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
            var bR = parseFloat(document.getElementById("bR").value);
            var sR = parseFloat(document.getElementById("sR").value);
            var L = parseFloat(document.getElementById("L").value);

            if (document.inputform.Choose[0].checked){
                var X = parseFloat(document.getElementById("T1").value);
                var Y = parseFloat(document.getElementById("T2").value);
                var Z = parseFloat(document.getElementById("T3").value);
            }
            else if (document.inputform.Choose[1].checked){
                var wiiPoint = mCom.PromptForPoint("Please place the center point of the large Arc.");
                var X = wiiPoint.X;
                var Y = wiiPoint.Y;
                var Z = wiiPoint.Z;
            }
            else {
                return false;
            }

            var bRadius = bR/2;
            var sRadius = sR/2;
            //This will calculate the angles depending on the small radius
            var angle1 = Math.asin(sRadius/bRadius);
            var angle2 = 2*Math.PI - angle1;
            var bArc = mSkMgr.InsertArc(X, Y, Z, bRadius, angle1, angle2);

            printOut("Center of large Arc\n");
            printOut("X: " + X + " Y: " + Y + " Z: " + Z + "\n");

            var disLine = Math.cos(angle1)*bRadius;
            var stretch = L - disLine;
            //For the top line, line1, from left to right
            var x1 = X + disLine;
            var y1 = Y + sRadius;
            var z1 = Z;
            var x2 = X + disLine + stretch;
            var y2 = Y + sRadius;
            var z2 = Z;
            //For the bottom line, line2, from left to right
            var x3 = X + disLine;
            var y3 = Y - sRadius;
            var z3 = Z;
            var x4 = X + disLine + stretch;
            var y4 = Y - sRadius;
            var z4 = Z;
            var line1 = mSkMgr.InsertLine(x1, y1, z1, x2, y2, z2);
            var line2 = mSkMgr.InsertLine(x3, y3, z3, x4, y4, z4);
            var sArc = mSkMgr.InsertArc(X + L, Y, Z, sRadius, 4.71238898, 7.85398163);
            printOut("Center of small Arc\n");
            printOut("X: " + (X + L) + " Y: " + Y + " Z: " + Z + "\n");
            var dimArray1 = new Array();
            dimArray1[0] = X - 2*bRadius;
            dimArray1[1] = Y + 2*bRadius;
            dimArray1[2] = Z;

            //This is where the code tries to change the height of the dimension text
            var styleMgr = mDoc.GetDimensionStyleManager();
            var dimStyle = styleMgr.GetActiveDimensionStyle();
            var dimText1 = dimStyle.GetDimensionStyleTextOptions();
            dimText1.put_Height(1);
            var hh = dimText1.get_Height();

            var dim1 = mSkMgr.InsertDiameterDimensionArc(bArc, dimArray1, "");
            var dimArray2 = new Array();
            dimArray2[0] = X + L + 2*sRadius;
            dimArray2[1] = Y - 2*sRadius;
            dimArray2[2] = Z;
            var dim2 = mSkMgr.InsertDiameterDimensionArc(sArc, dimArray2, "");
            dimArray1[0] = X;
            dimArray1[1] = Y;
            dimArray1[2] = Z;
            dimArray2[0] = X + L;
            dimArray2[1] = Y;
            dimArray2[2] = Z;
            var dimArray3 = new Array();
            dimArray3[0] = X + L/2;
            dimArray3[1] = Y - 2*bRadius;
            dimArray3[2] = Z;
            var dim3 = mSkMgr.InsertAlignedDimension(dimArray1, dimArray2, dimArray3, "");
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Insert and Dimension Sketch Example (JS)</title>

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

    <H1>Insert and Dimension Sketch Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example inserts and dimensions a
							sketch similar to the following image. In the
							DraftSight drawing, Dimension values are
							shown instead of the text shown in the image.
							<p>
							<img border="0" src="Keyhole.gif" width="288" height="194"></p>
							<ol>
                            <li>Start DraftSight.<li>Using
							the following form, specify how to create the sketch
							and where to place it in the drawing:<ol>
                            <li>Type a diameter in <b>Diameter
							of large Arc</b>. </li>
							<li>Type a diameter in <b>Diameter of small Arc</b>.</li>
							<li>Type the distance between the center points of
							the Arcs in <b>Distance between center
							points</b>.
                            </li>
							<li>Insert the center points:</li>
                            </ol></li>
                            </ol>
							<blockquote>
								<blockquote>
									<ol>
										<li>Select <b>Center point coordinates</b>.</li>
										<li>Type the x, y, and z coordinates for the
										center point of the large Arc.</li>
										<li>Click <b>Insert</b>.</li>
                            			<br>
&nbsp;<ul>- or -</ul>
									</ol>
									<ol>
										<li>Select <b>Center point in drawing.</b></li>
										<li>Click
										<b>Insert</b>.</li>
										<li>Click anywhere in the drawing to insert
										the center point for the large Arc and
										to insert the sketch.</li>
										</ol>
								</blockquote>
							</blockquote>
							<ol start="3">
								<li>Examine the drawing.</li>
							</ol>
								<p><b>NOTES:</b></p>
								<ul>
									<li>The coordinates of the center points are printed to
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
                            <table class="style3" width="410">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style20" width="322">
                                        <b>Diameter of large Arc:</b></td>
                                    <td class="style5" width="128">
                                    	<input id="bR" type="text" value="1.0" size="11"/></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="322">
                                        <b>Diameter of small Arc:</b></td>
                                    <td class="style5" width="128">
                                        <input id="sR" type="text" value="0.5" size="11"/></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="322">
                                        <b>Distance between center points:</b></td>
                                    <td class="style5" width="128">
                                        <input id="L" type="text" value="1.0" size="11"/></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="322">
                                        &nbsp;</td>
                                    <td class="style5" width="128">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Center point coordinates&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        <br />
                                        &nbsp;&nbsp;&nbsp;
                                        X:
										<input id="T1" type="text" value="0.0" size="13" /> Y:
										<input id="T2"
                                            type="text" value="0.0" size="13" /> Z:
										<input id="T3" type="text" value="0.0" size="14" /></td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
										<input id="R2" name="Choose"
                                            type="radio" value="2" />Center
										point in drawing</td>
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

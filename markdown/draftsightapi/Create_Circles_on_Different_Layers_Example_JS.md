---
title: "Create Circles on Different Layers Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Circles_on_Different_Layers_Example_JS.htm"
---

# Create Circles on Different Layers Example (JS)

## Create Circles on Different Layers Example (JavaScript)

| This example creates concentric Circles on different Layers in a DraftSight drawing. Start DraftSight. Using the following form, specify the colors for the Circles and their center point: Select a color for: Innermost Circle Circle next to innermost Circle circle next to outermost Circle Outermost Circle Insert the center point: Select Center point coordinates . Type the x, y, and z coordinates for the center point of the Circles. Click Insert . - or - Select Center point in drawing. Click Insert . Click anywhere in the drawing to insert the center point for the Circles. Select Format > Layer . To hide the Circle on the Center Layer, click the button in its Show column once, possibly twice, and click OK . Examine the drawing to verify that the Circle on the Center Layer is hidden. To show the Circle on the Center Layer, select Format > Layer . Click the button in the Show column for the Center Layer once, possible twice, and click OK . Examine the drawing to verify that the Circle on the Center Layer is visible. NOTES: The coordinates of the center point and the colors of the Circles are printed to Output. Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,Layers">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,models">
<meta name=MS-HKWD content="JavaScript examples,Circles">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCommandMessage.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLayerManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLayer.js"></script>

    <!-- This is the main block where you place the JavaScript API -->
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
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            var mLM = mDoc.GetLayerManager();
            //Enter in your JavaScript API here

            if (document.inputform.Choose[0].checked){
                var X = parseFloat(document.getElementById("T1").value);
                var Y = parseFloat(document.getElementById("T2").value);
                var Z = parseFloat(document.getElementById("T3").value);
            }
            else if (document.inputform.Choose[1].checked){
                var wiiPoint = mCom.PromptForPoint("Select where you want to place the center point of the Circles.");
                var X = wiiPoint.X;
                var Y = wiiPoint.Y;
                var Z = wiiPoint.Z;
            }
            else {
                return false;
            }

            var circle1 = mSkMgr.InsertCircle(X,Y,Z,2);
            var circle2 = mSkMgr.InsertCircle(X,Y,Z,4);
            var circle3 = mSkMgr.InsertCircle(X,Y,Z,6);
            var circle4 = mSkMgr.InsertCircle(X,Y,Z,8);
            var ncolor1 = document.getElementById("C1").value;
            var ncolor2 = document.getElementById("C2").value;
            var ncolor3 = document.getElementById("C3").value;
            var ncolor4 = document.getElementById("C4").value;

            var color1 = circle1.get_Color();
            var color2 = circle2.get_Color();
            var color3 = circle3.get_Color();
            var color4 = circle4.get_Color();

            color1.SetNamedColor(ncolor1);
            color2.SetNamedColor(ncolor2);
            color3.SetNamedColor(ncolor3);
            color4.SetNamedColor(ncolor4);

            circle1.put_Color(color1);
            circle2.put_Color(color2);
            circle3.put_Color(color3);
            circle4.put_Color(color4);

            var layer1 = mLM.CreateLayer("Center");
            var layer2 = mLM.CreateLayer("SmallerMiddle");
            var layer3 = mLM.CreateLayer("BiggerMiddle");
            var layer4 = mLM.CreateLayer("Outer");

            var clayer1 = circle1.get_Layer();
            var clayer2 = circle2.get_Layer();
            var clayer3 = circle3.get_Layer();
            var clayer4 = circle4.get_Layer();

            circle1.put_Layer("Center");
            circle2.put_Layer("SmallerMiddle");
            circle3.put_Layer("BiggerMiddle");
            circle4.put_Layer("Outer");

            clayer1 = circle1.get_Layer();
            clayer2 = circle2.get_Layer();
            clayer3 = circle3.get_Layer();
            clayer4 = circle4.get_Layer();

            var lw1 = circle1.get_LineWeight();
            var lw2 = circle2.get_LineWeight();
            var lw3 = circle3.get_LineWeight();
            var lw4 = circle4.get_LineWeight();

            circle1.put_LineWeight("dsLnWt_025");
            circle2.put_LineWeight("dsLnWt_050");
            circle3.put_LineWeight("dsLnWt_100");
            circle4.put_LineWeight("dsLnWt_200");

            lw1 = circle1.get_LineWeight();
            lw2 = circle2.get_LineWeight();
            lw3 = circle3.get_LineWeight();
            lw4 = circle4.get_LineWeight();

            printOut("Center point of Circles:\n");
            printOut("X: " + X + " Y: " + Y + " Z: " + Z + "\n");
            printOut("Innermost Circle color: " + ncolor1 + "\n");
            printOut("Circle next to innermost Circle color: " + ncolor2 + "\n");
            printOut("Circle next to outermost Circle color: " + ncolor3 + "\n");
            printOut("Outmermost Circle color: " + ncolor4 + "\n\n");
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Create Circles on Different Layers Example (JS)</title>

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

    <H1>Create Circles on Different Layers Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example creates concentric Circles on different
							Layers in a DraftSight drawing.
							<ol>
                            <li>Start DraftSight.<li>
							Using the following form, specify the colors for the
							Circles and their center point:<ol>
								<li>Select a color for:<ul>
									<li><b>Innermost Circle</b></li>
									<li><b>Circle next to innermost Circle</b></li>
									<li><b>circle next to outermost Circle</b></li>
									<li><b>Outermost Circle</b></li>
								</ul>
								</li>
								<li>Insert the center point:</li>
							</ol>
							</li>
                            </ol>
							<blockquote>
								<blockquote>
									<ol>
										<li>Select <b>Center point coordinates</b>.</li>
										<li>Type the x, y, and z coordinates for
										the center point of the Circles.</li>
										<li>Click <b>Insert</b>.</li>
                            			<br>
                            			<br>
										- or -</ol>
									<ol>
										<li>Select <b>Center point in drawing.</b></li>
										<li>Click
										<b>Insert</b>.</li>
										<li>Click anywhere in the drawing to
										insert the center point for the Circles.</li>
										</ol>
								</blockquote>
							</blockquote>
							<ol start="3">
								<li>Select <b>Format &gt; Layer</b>. </li>
								<li>To hide the Circle on the Center Layer,
								click the button in its <b>Show</b> column once,
								possibly twice,
								and click <b>OK</b>.</li>
								<li>Examine the drawing to verify that the
								Circle on the Center Layer is hidden.</li>
								<li>To show the Circle on the Center Layer,
								select <b>Format &gt; Layer</b>.</li>
								<li>Click the button in the <b>Show</b> column
								for the Center Layer once, possible twice, and click <b>OK</b>.</li>
								<li>Examine the drawing to verify that the
								Circle on the Center Layer is visible.</li>
							</ol>
							<p><b>NOTES:</b></p>
								<ul>
									<li>The coordinates of the center point and
									the colors of the Circles are printed to
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
                                    <td class="style20" width="306">
                                        <b>Innermost Circle:</b></td>
                                    <td class="style5" width="144">
                                        <select id="C1" name="Color1">
                                            <option value="dsNamedColor_Red">Red</option>
                                            <option value="dsNamedColor_Yellow">Yellow</option>
                                            <option value="dsNamedColor_Green">Green</option>
                                            <option value="dsNamedColor_Cyan">Cyan</option>
                                            <option value="dsNamedColor_Blue">Blue</option>
                                            <option value="dsNamedColor_Magenta">Magenta</option>
                                            <option value="dsNamedColor_White">White</option>
                                        </select></td>
                                </tr>
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style20" width="306">
                                        <b>Circle next to innermost Circle:</b></td>
                                    <td class="style5" width="144">
                                        <select id="C2" name="Color2">
                                            <option value="dsNamedColor_Red">Red</option>
                                            <option value="dsNamedColor_Yellow">Yellow</option>
                                            <option value="dsNamedColor_Green">Green</option>
                                            <option value="dsNamedColor_Cyan">Cyan</option>
                                            <option value="dsNamedColor_Blue">Blue</option>
                                            <option value="dsNamedColor_Magenta">Magenta</option>
                                            <option value="dsNamedColor_White">White</option>
                                        </select></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="306">
                                        <b>Circle next to outermost Circle:</b></td>
                                    <td class="style5" width="144">
                                        <select id="C3" name="Color3">
                                            <option value="dsNamedColor_Red">Red</option>
                                            <option value="dsNamedColor_Yellow">Yellow</option>
                                            <option value="dsNamedColor_Green">Green</option>
                                            <option value="dsNamedColor_Cyan">Cyan</option>
                                            <option value="dsNamedColor_Blue">Blue</option>
                                            <option value="dsNamedColor_Magenta">Magenta</option>
                                            <option value="dsNamedColor_White">White</option>
                                        </select></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="306">
                                        <b>Outermost Circle:</b></td>
                                    <td class="style5" width="144">
                                        <select id="C4" name="Color4">
                                            <option value="dsNamedColor_Red">Red</option>
                                            <option value="dsNamedColor_Yellow">Yellow</option>
                                            <option value="dsNamedColor_Green">Green</option>
                                            <option value="dsNamedColor_Cyan">Cyan</option>
                                            <option value="dsNamedColor_Blue">Blue</option>
                                            <option value="dsNamedColor_Magenta">Magenta</option>
                                            <option value="dsNamedColor_White">White</option>
                                        </select></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="306">
                                        &nbsp;</td>
                                    <td class="style5" width="144">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Center
										point coordinates&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        <br />
                                        &nbsp;&nbsp;&nbsp;
                                        X:
										<input id="T1" type="text" value="0.0" size="10" /> Y:
										<input id="T2"
                                            type="text" value="0.0" size="12" /> Z:
										<input id="T3" type="text" value="0.0" size="12" /></td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
										<input id="R2" name="Choose"
                                            type="radio" value="2" />Center point
										in drawing</td>
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

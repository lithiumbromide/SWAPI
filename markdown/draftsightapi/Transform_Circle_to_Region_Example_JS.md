---
title: "Transform Circle to Region Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Transform_Circle_to_Region_Example_JS.htm"
---

# Transform Circle to Region Example (JS)

## Transform Circle to Region Example (JavaScript)

| This example shows how to transform a Circle to a Region. Start DraftSight. Using the following form, insert the center point for the Circle: Select Center point coordinates . Type the x, y, and z coordinates for the center point of the Circle. Click Insert . - or - Select Center point in drawing. Click Insert . Click anywhere in the drawing to insert the center point for the Circle. The Circle is selected and transformed to a Region. To verify, interactively select the perimeter of the Circle in the drawing and examine the Properties palette. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Circles">
<meta name=MS-HKWD content="JavaScript examples,Regions">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSelectionManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsRegion.js"></script>

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
            var mSelMgr = mDoc.GetSelectionManager();
            var mCom = mApp.GetCommandMessage();
            //Enter in your JavaScript API here

            if (document.inputform.Choose[0].checked){
                var X = parseFloat(document.getElementById("T1").value);
                var Y = parseFloat(document.getElementById("T2").value);
                var Z = parseFloat(document.getElementById("T3").value);
            }
            else if (document.inputform.Choose[1].checked){
                var wiiPoint = mCom.PromptForPoint("Select where you want to place the center point of the Circle.");
                var X = wiiPoint.X;
                var Y = wiiPoint.Y;
                var Z = wiiPoint.Z;
            }
            else {
                return false;
            }

            //Insert the Circle
            var circle1 = mSkMgr.InsertCircle(X,Y,Z,2);

            //Select the Circle
            var status = circle1.Select(true);

            //Get the selected Circle
            var dsEntityType;
            var entities = new Array();
            entities[0] = mSelMgr.GetSelectedObject("dsSelectionSetType_Current", 0, dsEntityType).SelObj;

            var regions = new Array();
            mSkMgr.InsertRegion(entities, regions);

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Transform Circle to Region Example (JS)</title>

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

    <H1>Transform Circle to Region Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to transform a Circle to a
							Region.
							<ol>
                            <li>Start DraftSight.<li>
							Using the following form, insert the center point
							for the
							Circle:</li>
                            </ol>
							<blockquote>
								<blockquote>
									<ol>
										<li>Select <b>Center point coordinates</b>.</li>
										<li>Type the x, y, and z coordinates for
										the center point of the Circle.</li>
										<li>Click <b>Insert</b>.</li>
                            			<br>
                            			<br>
										- or -</ol>
									<ol>
										<li>Select <b>Center point in drawing.</b></li>
										<li>Click
										<b>Insert</b>.</li>
										<li>Click anywhere in the drawing to
										insert the center point for the Circle.</li>
										</ol>
								</blockquote>
							</blockquote>
							<ol start="3">
								<li>The Circle is selected and transformed to a Region. </li>
								<li>To verify, interactively select the
								perimeter of the Circle in the drawing and examine the
								Properties palette.</li>
							</ol>
							<p><b>NOTES:</b></p>
								<ul>
									<li>Errors are printed to Output.</li>
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
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
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
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
										<input id="R2" name="Choose"
                                            type="radio" value="2" />Center point
										in drawing</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style6">
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

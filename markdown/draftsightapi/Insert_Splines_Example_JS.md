---
title: "Insert Splines Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Splines_Example_JS.htm"
---

# Insert Splines Example (JS)

## Insert Splines Example (JavaScript)

| This example constructs several Splines, which are displayed as the Dassault Syst è mes logo in a DraftSight drawing. Start DraftSight. Using the following form, specify where to place the logo: Select Center point coordinates . Type x, y, and z coordinates. Click Insert . - or - Select Center point in drawing. Click Insert . Click anywhere in the drawing to insert the logo at that point. Examine the drawing. Click View > Zoom > Fit to better see the logo. NOTES: The coordinates are printed to Output. Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSpline.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>

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

            //Type your JavaScript API code here

            if (document.inputform.Choose[0].checked){
                var x = parseFloat(document.getElementById("T1").value);
                var y = parseFloat(document.getElementById("T2").value);
                var z = parseFloat(document.getElementById("T3").value);
            }
            else if (document.inputform.Choose[1].checked){
                var wiiPoint = mCom.PromptForPoint("Please select where the bottom left corner of the 3DS logo should go");
                var x = wiiPoint.X;
                var y = wiiPoint.Y;
                var z = wiiPoint.Z;
            }
            else {
                return false;
            }

            //This is for the debugging purposes
            //var x = 0;
            //var y = 0;
            //var z = 0;

            var spArray1 = new Array();
            var spArray2 = new Array();
            var spArray3 = new Array();

            //This is for the D
            spArray1[0] = x + 0.4513;
            spArray1[1] = y + 0.3825;
            spArray1[2] = z + 0.0;
            spArray1[3] = x + 0.3240;
            spArray1[4] = y + 0.1912;
            spArray1[5] = z + 0.0;
            spArray1[6] = x + 0.1261;
            spArray1[7] = y + 0.0932;
            spArray1[8] = z + 0.0;
            spArray1[9] = x + 0.2571;
            spArray1[10] = y + 0.3839;
            spArray1[11] = z + 0.0;
            spArray1[12] = x + 0.0023;
            spArray1[13] = y + 0.0086;
            spArray1[14] = z + 0.0;
            spArray1[15] = x + 0.2132;
            spArray1[16] = y + 0.0711;
            spArray1[17] = z + 0.0;
            spArray1[18] = x + 0.5275;
            spArray1[19] = y + 0.4664;
            spArray1[20] = z + 0.0;
            spArray1[21] = x + 0.4280;
            spArray1[22] = y + 0.5052;
            spArray1[23] = z + 0.0;
            spArray1[24] = x + 0.1237;
            spArray1[25] = y + 0.4568;
            spArray1[26] = z + 0.0;

            var spline1 = mSkMgr.InsertSpline(spArray1, true, 0, 0, 0, 0, 0, 0);

            //This is for the S
            spArray2[0] = x + 0.4659;
            spArray2[1] = y + 0.1472;
            spArray2[2] = z + 0.0;
            spArray2[3] = x + 0.8218;
            spArray2[4] = y + 0.2052;
            spArray2[5] = z + 0.0;
            spArray2[6] = x + 0.6099;
            spArray2[7] = y + 0.5472;
            spArray2[8] = z + 0.0;
            spArray2[9] = x + 0.7898;
            spArray2[10] = y + 0.6372;
            spArray2[11] = z + 0.0;
            spArray2[12] = x + 0.9877;
            spArray2[13] = y + 0.5952;
            spArray2[14] = z + 0.0;
            spArray2[15] = x + 0.7158;
            spArray2[16] = y + 0.5472;
            spArray2[17] = z + 0.0;
            spArray2[18] = x + 0.9318;
            spArray2[19] = y + 0.2232;
            spArray2[20] = z + 0.0;
            spArray2[21] = x + 0.7818;
            spArray2[22] = y + 0.1112;
            spArray2[23] = z + 0.0;

            var spline2 = mSkMgr.InsertSpline(spArray2, true, 0, 0, 0, 0, 0, 0);

            //This is for the 3
            spArray3[0] = x + 0.6319;
            spArray3[1] = y + 0.8672;
            spArray3[2] = z + 0.0;
            spArray3[3] = x + 0.3300;
            spArray3[4] = y + 0.9233;
            spArray3[5] = z + 0.0;
            spArray3[6] = x + 0.5000;
            spArray3[7] = y + 0.9642;
            spArray3[8] = z + 0.0;
            spArray3[9] = x + 0.7318;
            spArray3[10] = y + 0.8952;
            spArray3[11] = z + 0.0;
            spArray3[12] = x + 0.6279;
            spArray3[13] = y + 0.6892;
            spArray3[14] = z + 0.0;
            spArray3[15] = x + 0.3690;
            spArray3[16] = y + 0.5563;
            spArray3[17] = z + 0.0;

            var spline3 = mSkMgr.InsertSpline(spArray3, true, 0, 0, 0, 0, 0, 0);

            var color1 = spline1.get_Color();
            var color2 = spline2.get_Color();
            var color3 = spline3.get_Color();

            color1.SetNamedColor("dsNamedColor_Blue");
            color2.SetNamedColor("dsNamedColor_Yellow");
            color3.SetNamedColor("dsNamedColor_Red");

            spline1.put_Color(color1);
            spline2.put_Color(color2);
            spline3.put_Color(color3);

            var realcount = 1;
            printOut("D Part\n");
            for (n = 0; n < 27; n = n + 3) {
                printOut("Point " + realcount + "\n");
                printOut("X: " + spArray1[n]);
                printOut(" Y: " + spArray1[n + 1]);
                printOut(" Z: " + spArray1[n + 2] + "\n");
                realcount++;
            }

            realcount = 1;
            printOut("\nS Part\n");
            for (n = 0; n < 24; n = n + 3) {
                printOut("Point " + realcount + "\n");
                printOut("X: " + spArray1[n]);
                printOut(" Y: " + spArray1[n + 1]);
                printOut(" Z: " + spArray1[n + 2] + "\n");
                realcount++;
            }

            realcount = 1;
            printOut("\n3 Part\n");
            for (n = 0; n < 18; n = n + 3) {
                printOut("Point " + realcount + "\n");
                printOut("X: " + spArray1[n]);
                printOut(" Y: " + spArray1[n + 1]);
                printOut(" Z: " + spArray1[n + 2] + "\n");
                realcount++;
            }
            printOut("\n");
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Insert Splines Example (JS)</title>

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

    <H1>Insert Splines Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example constructs several Splines, which
							are displayed as
							the Dassault Syst<font face="Verdana">è</font>mes
							logo in a DraftSight drawing. <ol>
                            <li>Start DraftSight.<li>Using
							the following form, specify where to place the logo:
                            <ol>
                            <li>Select <b>Center point coordinates</b>.</li>
                            <li>Type x, y, and z coordinates.</li>
                            <li>Click <b>Insert</b>.</li>
                            <ul>- or -</ul>
                            </ol>
                            <ol>
                            <li>Select <b>Center point in drawing.</b></li>
                            <li>Click <b>Insert</b>.</li>
                            <li>Click anywhere in the drawing to insert the logo at that
							point.</li>
                            </ol>
                            <li>Examine the drawing.</li>
							<li>Click <b>View &gt; Zoom &gt; Fit</b> to better see the
							logo.</li>
                            </ol>
								<p><b>NOTES:</b></p>
								<ul>
									<li>The coordinates are printed to
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
                            <table class="style3">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style6">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Center point coordinates&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        <br />
                                        &nbsp;&nbsp;&nbsp;
                                        X:
										<input id="T1" type="text" value="0.0" size="11" /> Y:
										<input id="T2"
                                            type="text" value="0.0" size="13" /> Z:
										<input id="T3" type="text" value="0.0" size="13" /><p>&nbsp;</p>
										<p> <input id="R2" name="Choose"
                                            type="radio" value="2" />Center point in drawing</p>
										<p> &nbsp;</p></td>
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

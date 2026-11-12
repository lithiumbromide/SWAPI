---
title: "Get Distance Between Two Math Points Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Distance_Between_Two_Math_Points_Example_JS.htm"
---

# Get Distance Between Two Math Points Example (JS)

## Get Distance Between Two Math Points Example (JavaScript)

| This example shows how to get the distance between two math points. Start DraftSight. Using the following form: Type the double values of the coordinates of the first point. Type the double values of the coordinates of the second point. Click Get Distance . Inspect the Output. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,math points">
<meta name=MS-HKWD content="JavaScript examples,math utility">

    <head>

    <!-- Without this line, this does not work in Internet Explorer 8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=8" />

    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

    <!-- Add your dsInterface .js Files here -->
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>

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
            var mMathUtil = mApp.GetMathUtility();
            var X = parseFloat(document.getElementById("X").value);
            var Y = parseFloat(document.getElementById("Y").value);
            var Z = parseFloat(document.getElementById("Z").value);
            var X0 = parseFloat(document.getElementById("X0").value);
            var Y0 = parseFloat(document.getElementById("Y0").value);
            var Z0 = parseFloat(document.getElementById("Z0").value);
            var mMathPt1 = mMathUtil.CreatePoint(X, Y, Z);
            var mMathPt2 = mMathUtil.CreatePoint(X0, Y0, Z0);
            var distance = mMathUtil.Distance(mMathPt1, mMathPt2).Result;
            printOut("Distance between points: " + distance);
            var resultPt1 = mMathUtil.Distance(mMathPt1, mMathPt2).Point1;
            var resultPt2 = mMathUtil.Distance(mMathPt1, mMathPt2).Point2;
			printOut("First point position: " + resultPt1.GetPosition().X + ", " + resultPt1.GetPosition().Y + ", " + resultPt1.GetPosition().Z);
			printOut("Second point position: " + resultPt2.GetPosition().X + ", " + resultPt2.GetPosition().Y + ", " + resultPt2.GetPosition().Z);
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Get Distance Between Two Math Points Example (JS)</title>

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

    <H1> Get Distance Between Two Math Points Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to get the distance between two math points.
                            <ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form:<ol>
                            <li>Type the double values of the coordinates of the first point.</li>
							<li>Type the double values of the coordinates of the second point.</li>
							<li>Click <b>Get Distance</b>.</li>
                            </ol></li>
							<li>Inspect the Output.</li>
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
                                        Coordinates of first point:</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        X: <input id="X" type="text" value="0.0" class="style22" /> Y: <input id="Y" type="text" value="0.0" class="style22" /> Z: <input id="Z" type="text" value="0.0" class="style22" /></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        Coordinates of second point:</td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;&nbsp; <b><font color="#006600">X:</font></b>
										<input id="X0" type="text" value="0.0" class="style22" name="T1" size="20" />
										<b><font color="#006600">Y:</font></b>
										<input id="Y0" type="text" value="0.0" class="style22" name="T2" size="20" />
										<b><font color="#006600">Z:</font></b>
										<input id="Z0" type="text" value="0.0" class="style22" name="T3" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Get Distance" onclick="runMacro()" />

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

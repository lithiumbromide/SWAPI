---
title: "Insert Lines and Angular Dimension Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Lines_and_Angular_Dimension_Example_JS.htm"
---

# Insert Lines and Angular Dimension Example (JS)

## Insert Lines and Angular Dimension Example (JavaScript)

| This example constructs two lines and inserts an angular dimension between the lines in a DraftSight drawing. Start DraftSight. Using the following form, specify the text for the angular dimension in Dimension text : Specify where to place the lines: Select Coordinates . Type the x, y, and z coordinates for the start and end lines in First line start , First line end , Second line start , and Second line end . When prompted, type the x, y, and z coordinates for the angular dimension and click OK after each prompt. Click Insert . - or - Select Points in drawing. Click Insert . When prompted, type the x, y, and z coordinates for the angular dimension and click OK after each prompt. Click anywhere in the drawing to insert the start and end points for the first and second lines. Examine the drawing. NOTES: If Dimension text is left blank, null is displayed. The coordinates for the angular dimension are printed to Output. Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
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
<meta name=MS-HKWD content="JavaScript examples,Lines">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsAngularDimension.js"></script>

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
            var doublearray = new Array();
            var xstring = prompt("Type the x coordinate for the dimension", "13");
            doublearray[0] = xstring;
            var ystring = prompt("Type the y coordinate for the dimension", "4");
            doublearray[1] = ystring;
            var zstring = prompt("Type the z coordinate for the dimension", "0");
            doublearray[2] = zstring;
            printOut(" X: " + xstring + " Y: " + ystring + " Z: " + zstring + "\n");

            /*For debugging purposes to see if it is placed into the array*/
            /*document.write(doublearray);*/

            /*Uncomment when it is ready to be sent to the server*/
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            if (document.inputform.Choose[0].checked){
                var SX1 = parseFloat(document.getElementById("SX1").value);
                var SY1 = parseFloat(document.getElementById("SY1").value);
                var SZ1 = parseFloat(document.getElementById("SZ1").value);
                var EX1 = parseFloat(document.getElementById("EX1").value);
                var EY1 = parseFloat(document.getElementById("EY1").value);
                var EZ1 = parseFloat(document.getElementById("EZ1").value);
                var SX2 = parseFloat(document.getElementById("SX2").value);
                var SY2 = parseFloat(document.getElementById("SY2").value);
                var SZ2 = parseFloat(document.getElementById("SZ2").value);
                var EX2 = parseFloat(document.getElementById("EX2").value);
                var EY2 = parseFloat(document.getElementById("EY2").value);
                var EZ2 = parseFloat(document.getElementById("EZ2").value);
            }
            else if (document.inputform.Choose[1].checked){
                var wiiPoint1 = mCom.PromptForPoint("Select where you want to start the first line");
                var SX1 = wiiPoint1.X;
                var SY1 = wiiPoint1.Y;
                var SZ1 = wiiPoint1.Z;
                var wiiPoint2 = mCom.PromptForPoint("Select where you want to end the first line");
                var EX1 = wiiPoint2.X;
                var EY1 = wiiPoint2.Y;
                var EZ1 = wiiPoint2.Z;
                var wiiPoint3 = mCom.PromptForPoint("Select where you want to start the second line");
                var SX2 = wiiPoint3.X;
                var SY2 = wiiPoint3.Y;
                var SZ2 = wiiPoint3.Z;
                var wiiPoint4 = mCom.PromptForPoint("Select where you want to end the second line");
                var EX2 = wiiPoint4.X;
                var EY2 = wiiPoint4.Y;
                var EZ2 = wiiPoint4.Z;
            }
            else {
                return false;
            }

            var OR = document.getElementById("OR").value;

            var mLine1 = mSkMgr.InsertLine(SX1, SY1, SZ1, EX1, EY1, EZ1);
            var mLine2 = mSkMgr.InsertLine(SX2, SY2, SZ2, EX2, EY2, EZ2);
            var mDim = mSkMgr.InsertAngularDimension2Line(mLine1, mLine2, doublearray, OR);
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Insert Lines and Angular Dimension Example (JS)</title>

    <!-- These styles are used to format the table cells -->
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
            color: #006600;
            font-weight: bold
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
        #OR
        {
            width: 300px;
        }
        #SX1
        {
            width: 30px;
        }
        #SY1
        {
            width: 30px;
        }
        #SZ1
        {
            width: 30px;
        }
        #EX1
        {
            width: 30px;
        }
        #EY1
        {
            width: 30px;
        }
        #EZ1
        {
            width: 30px;
        }
        #SX2
        {
            width: 30px;
        }
        #SY2
        {
            width: 30px;
        }
        #SZ2
        {
            width: 30px;
            height: 22px;
        }
        #EX2
        {
            width: 30px;
        }
        #EY2
        {
            width: 30px;
        }
        #EZ2
        {
            width: 30px;
        }
    </style>

    </head>

    <H1>Insert Lines and Angular Dimension Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 75px;">
                        <div class="style7">
							This example constructs two lines and inserts an
							angular dimension between the lines in a DraftSight drawing.<ol>
                            <li>Start DraftSight.<li>Using the following form, specify the text for the angular dimension in <b>
							Dimension text</b>:<li>Specify where to place the lines:
                            <ol>
                            <li>Select <b>Coordinates</b>.</li>
                            <li>Type the x, y, and z coordinates for the start
							and end lines in <b>First line start</b>, <b>First
							line end</b>, <b>Second line start</b>, and <b>
							Second line end</b>.</li>
							<li>When prompted, type the x, y, and z coordinates
							for the angular dimension and click <b>OK</b> after each prompt.</li>
                            <li>Click <b>Insert</b>.</li>
                            <ul>- or -</ul>
                            </ol>
                            <ol>
                            <li>Select <b>Points in drawing.</b></li>
							<li>Click <b>Insert</b>.</li>
							<li>When prompted, type the x, y, and z coordinates
							for the angular dimension and click <b>OK</b> after each prompt.</li>
							<li>Click anywhere in the drawing to insert the
							start and end points for the first and second lines.</li>
                            </ol>
                            <li>Examine the drawing.</li>
                            </ol>
								<p><b>NOTES:</b></p>
								<ul>
									<li>If <b>Dimension text </b>is left blank, <b>null</b>
									is displayed.</li>
									<li>The coordinates for the angular dimension are printed to
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
                            <table class="style3" width="700">
                                <!-- Reuse this row to add more rows-->
                                <tr>
                                    <!-- Use these two cells to implement inputs, add more rows if necessarily-->
                                    <td class="style20" width="150">
                                        Dimension text:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="Override" id="OR" value = "Random" size="41" /></td>
                                </tr>
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Coordinates&nbsp;&nbsp;&nbsp;&nbsp; </td>
                                </tr>
                                <tr>
                                    <td class="style20" width="450" colspan="2">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; First line
										start</td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; x:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartX1" id="SX1" value="7" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartY1" id="SY1"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartZ1" id="SZ1"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="450" colspan="2">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; First line end</td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndX1" id="EX1" value="10" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndY1" id="EY1"  value="3" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndZ1" id="EZ1"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="450" colspan="2">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Second line
										start </td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartX2" id="SX2" value="12" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartY2" id="SY2"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="StartY3" id="SZ2"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="450" colspan="2">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Second line end </td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndX2" id="EX2" value="15" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndY2" id="EY2"  value="2" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z:</td>
                                    <td class="style5" width="300">
                                        <input type="text" name="EndY3" id="EZ2"  value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="150">
                                        &nbsp;</td>
                                    <td class="style5" width="300">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td colspan="2" class="style6">
										<input id="R2" name="Choose"
                                            type="radio" value="2" />Points in drawing</td>
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

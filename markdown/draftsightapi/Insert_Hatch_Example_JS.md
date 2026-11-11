---
title: "Insert Hatch Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_Example_JS.htm"
---

# Insert Hatch Example (JS)

## Insert Hatch Example (JavaScript)

| This example shows how to create a Hatch and Hatch boundary loop data. Start DraftSight and open a drawing document with sketch entities. Using the following form, create a Hatch by selecting: Boundary loop - or - Line segments that form the Hatch boundary - or - Internal points of an enclosed area Type the Hatch pattern: Name. (See the Pattern dropdown list box on the Draw > Hatch/Fill dialog for options.) Scale. Angle. Click Create Hatch . Inspect the Hatch in the DraftSight drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the web page and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Hatches">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsHatch.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSelectionManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>

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
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSMgr = mModel.GetSketchManager();
            var mSelMgr = mDoc.GetSelectionManager();
            var mCom = mApp.GetCommandMessage();
            if (document.inputform.Choose[0].checked){
            	var X2 = parseFloat(document.getElementById("X2").value);
                var Y2 = parseFloat(document.getElementById("Y2").value);
                var X4 = parseFloat(document.getElementById("X4").value);
                var Y4 = parseFloat(document.getElementById("Y4").value);
                var X5 = parseFloat(document.getElementById("X5").value);
                var Y5 = parseFloat(document.getElementById("Y5").value);
                var X6 = parseFloat(document.getElementById("X6").value);
                var Y6 = parseFloat(document.getElementById("Y6").value);
                var bArray = new Array();
			    bArray[0] = X2;
			    bArray[1] = Y2;
			    bArray[2] = X4;
			    bArray[3] = Y4;
			    bArray[4] = X5;
			    bArray[5] = Y5;
			    bArray[6] = X6;
			    bArray[7] = Y6;
			    var longArray = new Array();
			    longArray[0] = 4;
			    var patName = document.getElementById("H1").value;
                var patScale = parseFloat(document.getElementById("H2").value);
				var patAngle = parseFloat(document.getElementById("H3").value);
                var hatch = mSMgr.InsertHatchByBoundary(longArray, bArray, patName, patScale, patAngle);
                var color = hatch.get_Color();
                printOut("Color of new Hatch: " + color.GetNamedColor());
            }
            else if (document.inputform.Choose[1].checked){
            	var prompt = "Select a Hatch boundary entity"
            	var errorMessage = "Unknown entity."
            	var statusSelect = mCom.PromptForSelection(false, prompt, errorMessage);
            	if (statusSelect) {
            		var count = mSelMgr.GetSelectedObjectCount("dsSelectionSetType_Previous");
            		var i;
            		var dsEntityType;
            		var dsEntities = new Array();
            		printOut("Number of entities selected: " + count);
            		for (i = 0; i < count; i++) {
            			dsEntities[i] = mSelMgr.GetSelectedObject("dsSelectionSetType_Previous", i, dsEntityType).SelObj;
            		}
            		var patName = document.getElementById("H1").value;
                	var patScale = parseFloat(document.getElementById("H2").value);
					var patAngle = parseFloat(document.getElementById("H3").value);
                	var hatch = mSMgr.InsertHatchByEntities(dsEntities, patName, patScale, patAngle);
                	var color = hatch.get_Color();
                	printOut("Color of new Hatch: " + color.GetNamedColor());
                }
            }
            else if (document.inputform.Choose[2].checked){
                var X7 = parseFloat(document.getElementById("X7").value);
                var Y7 = parseFloat(document.getElementById("Y7").value);
                var X8 = parseFloat(document.getElementById("X8").value);
                var Y8 = parseFloat(document.getElementById("Y8").value);
                var X9 = parseFloat(document.getElementById("X9").value);
                var Y9 = parseFloat(document.getElementById("Y9").value);
                var X10 = parseFloat(document.getElementById("X10").value);
                var Y10 = parseFloat(document.getElementById("Y10").value);
                var bArray = new Array();
			    bArray[0] = X7;
			    bArray[1] = Y7;
			    bArray[2] = X8;
			    bArray[3] = Y8;
			    bArray[4] = X9;
			    bArray[5] = Y9;
			    bArray[6] = X10;
			    bArray[7] = Y10;
                var patName = document.getElementById("H1").value;
                var patScale = parseFloat(document.getElementById("H2").value);
				var patAngle = parseFloat(document.getElementById("H3").value);
                var hatch = mSMgr.InsertHatchByInternalPoints(bArray, patName, patScale, patAngle);
                var color = hatch.get_Color();
                printOut("Color of new Hatch: " + color.GetNamedColor());

            }

           mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title> Insert Hatch Example (JS)</title>

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

    <H1> Insert Hatch Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to create a Hatch and Hatch
							boundary loop data.<ol>
                            <li>Start DraftSight and open a drawing document
							with sketch entities.</li>
                            <li>Using the following form, create a Hatch by
							selecting:<ol type="a">
                            <li><b>Boundary loop</b></li>
                            </ol>
                            <ul>
								<p>- or -</p>
							</ul>
							<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </b>
							<b>Line segments
							that form
							the Hatch boundary</b><ul>
								<p>- or -</p>
							</ul>
							<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							<b>Internal points of an enclosed area<br>
&nbsp;</b><ol type="a">
                            <li value="2">Type the Hatch pattern:<ol type="a">
                            <li>Name. (See the
							Pattern dropdown list box on the <b>Draw &gt; Hatch/Fill
							</b>dialog<b> </b>for options.)</li>
							<li>Scale.</li>
							<li>Angle.</li>
                            </ol>
								</li>
							<li>Click <b>Create Hatch</b>.</li>
                            </ol>
								<li>Inspect the Hatch in the DraftSight drawing.</li>
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
										near the top of the web page and select <b>
										Allow Blocked Content</b>.</li>
									</ol>
								</blockquote></div>
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3" width="535" style="width: 750px">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Boundary
										loop</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										First
										point:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X:
										<input id="X2" type="text" value="0.0" class="style22" name="T15" size="20" /> Y:
										<input id="Y2" type="text" value="0.0" class="style22" name="T16" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Second
										point:&nbsp;&nbsp;&nbsp; X:
										<input id="X4" type="text" value="0.0" class="style22" name="T24" size="20" /> Y:
										<input id="Y4" type="text" value="0.0" class="style22" name="T25" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Third
										point:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X:
										<input id="X5" type="text" value="0.0" class="style22" name="T26" size="20" /> Y:
										<input id="Y5" type="text" value="0.0" class="style22" name="T27" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Fourth
										point:&nbsp;&nbsp;&nbsp;&nbsp; X:
										<input id="X6" type="text" value="0.0" class="style22" name="T28" size="20" /> Y:
										<input id="Y6" type="text" value="0.0" class="style22" name="T29" size="20" />
										<br>
&nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        <input id="Radio2" name="Choose"
                                            type="radio" value="2" />Line
										segments that
										form the
										Hatch boundary</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;
										<font color="#006600"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Select multiple
										Lines that form the Hatch boundary. <br>
										</b></font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										<font color="#006600"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Press Enter.<br>
&nbsp;</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;
                                        <input id="Radio3" name="Choose"
                                            type="radio" value="3" />Internal
										points of an enclosed area</td>
                                </tr>
                                <tr>
                                    <td class="style6" height="27" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <font color="#006600">
										<b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										First </b></font><b>
										<font color="#006600">point</font></b><font color="#006600"><b>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X:</b></font>
										<input id="X7" type="text" value="0.0" class="style22" name="T30" size="20" />
										<b>
										<font color="#006600">Y:</font></b>
										<input id="Y7" type="text" value="0.0" class="style22" name="T31" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style6" height="25" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Second point:&nbsp;&nbsp;&nbsp; X:</font></b>
										<input id="X8" type="text" value="0.0" class="style22" name="T32" size="20" />
										<b>
										<font color="#006600">Y:</font></b>
										<input id="Y8" type="text" value="0.0" class="style22" name="T33" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style6" height="25" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Third points:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X:</font></b>
										<input id="X9" type="text" value="0.0" class="style22" name="T34" size="20" />
										<b>
										<font color="#006600">Y:</font></b>
										<input id="Y9" type="text" value="0.0" class="style22" name="T35" size="20" /> </td>
                                </tr>
                                <tr>
                                    <td class="style6" height="23" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; <b>
										<font color="#006600">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										Fourth points:&nbsp;&nbsp;&nbsp;X:</font></b>
										<input id="X10" type="text" value="0.0" class="style22" name="T36" size="20" />
										<b>
										<font color="#006600">Y:</font></b>
										<input id="Y10" type="text" value="0.0" class="style22" name="T37" size="20" />
										<br>
&nbsp;</td>
                                </tr>

                                <tr>
                                    <td class="style6" height="37" style="height: 20px">
                                        &nbsp;<b><font color="#006600">Hatch<br>
&nbsp;&nbsp;&nbsp;&nbsp; Name:</font></b>&nbsp;&nbsp;
										<input id="H1" type="text" name="T21" size="20"></td>
                                </tr>

                                <tr>
                                    <td class="style6" height="37" style="height: 20px">
                                        &nbsp;<b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Scale:</font></b>&nbsp;&nbsp;&nbsp;
										<input id="H2" type="text" name="T22" size="20"></td>
                                </tr>

                                <tr>
                                    <td class="style6" height="37" style="height: 20px">
                                        &nbsp;<b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Angle:</font></b>&nbsp;&nbsp;
										<input id="H3" type="text" name="T23" size="20"><br>
&nbsp;</td>
                                </tr>

                                <tr>
                                    <td class="style6" height="37" style="height: 20px">
                                        <input id="Button1" type="button" value="Create Hatch" onclick="runMacro()" />

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

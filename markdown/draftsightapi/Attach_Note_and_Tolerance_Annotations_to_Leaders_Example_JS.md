---
title: "Attach Note and Tolerance Annotations to Leaders Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_JS.htm"
---

# Attach Note and Tolerance Annotations to Leaders Example (JS)

## Attach Note and Tolerance Annotations to Leaders Example (JavaScript)

| This example attaches Note and Tolerance annotations to Leaders. Start DraftSight. Click Insert to insert two Leaders to which to attach Note and Tolerance annotations. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Leaders">
<meta name=MS-HKWD content="JavaScript examples,Tolerances">
<meta name=MS-HKWD content="JavaScript examples,geometric Tolerances">
<meta name=MS-HKWD content="JavaScript examples,Notes">
<meta name=MS-HKWD content="JavaScript examples,annotations">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLeader.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPlane.js"></script>
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
                apiCode();
            }
            catch (err) {
                printOut(djErrorString(err));
            }
        }
        function apiCode() {
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();

            //Abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();

            //Get document, model, and Sketch Manager
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();

            //Add first Leader
            var leaderCoordinates = new Array();
            leaderCoordinates[0] = 42.5;
            leaderCoordinates[1] = 20;
            leaderCoordinates[2] = 0;
            leaderCoordinates[3] = 75;
            leaderCoordinates[4] = 65;
            leaderCoordinates[5] = 0;
            var noteWidth = 1.0;
            var noteText = "L1 ";
            var mLeader = mSkMgr.InsertLeader(leaderCoordinates, noteWidth, noteText);

            //Create point where to insert Tolerance annotation
            var firstX = 20;
            var firstY = 20;
            var firstZ = 20;
            var mMathUtility = mApp.GetMathUtility();
            var mMathPoint = mMathUtility.CreatePoint(firstX, firstY, firstZ);

            //Attach Tolerance annotation
            mLeader.SetToleranceAnnotation("{\\Fgdt;j}%%v{\\Fgdt;n}0.7{\\Fgdt;m}", mMathPoint);

            //Add second Leader
            var leaderCoordinates2 = new Array();
            leaderCoordinates2[0] = 27.5;
            leaderCoordinates2[1] = 10;
            leaderCoordinates2[2] = 0;
            leaderCoordinates2[3] = 9;
            leaderCoordinates2[4] = 10;
            leaderCoordinates2[5] = 0;
            var noteWidth2 = 1.0;
            var noteText2 = "L2 ";
            var mLeader2 = mSkMgr.InsertLeader(leaderCoordinates2, noteWidth2, noteText2);

            //Create point where to insert Tolerance annotation
            var secondX = 30;
            var secondY = 10;
            var secondZ = 30;
            var mMathUtility2 = mApp.GetMathUtility();
            var mMathPoint2 = mMathUtility2.CreatePoint(secondX, secondY, secondZ);

            //Attach Tolerance annotation
            mLeader2.SetNoteAnnotation("New Note", mMathPoint2);

            //Zoom to fit
            var lowerLeftArray = [0,0,0]
            var upperRightArray = [0,0,0]
            mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

            //Type your JavaScript API code here
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Attach Note and Tolerance Annotations to Leaders Example (JS)</title>

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
            height: 10px;
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
            height: 10px;
            text-align: left;
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
            color: #006600;
            font-weight: bold;
        }
        .style22
        {
            width: 50px;
        }
    </style>

    </head>

    <H1>Attach Note and Tolerance Annotations to Leaders Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example attaches Note and Tolerance annotations
							to Leaders.&nbsp;<ol>
                            <li>Start DraftSight.<li>Click <b>Insert </b>to
							insert two Leaders to which to attach Note
							and Tolerance annotations.<li>Examine the drawing.</ol>
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
										and running scripts is blocked, allow blocked
										content.</li>
								</ol>
							</blockquote></div>
						<hr />
                    </td>
                </tr>
                <tr>
                    <td>
                        <form name="inputform">
                            <table class="style3">
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
                            	</div>
                        </form>
                       <hr />
                    </td>
                </tr>
            </tbody>
        </table>
    <br />
    </body>
</html>
```

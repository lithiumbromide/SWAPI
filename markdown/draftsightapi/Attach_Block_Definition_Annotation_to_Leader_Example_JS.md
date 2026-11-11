---
title: "Attach Block Definition Annotation to Leader Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Attach_Block_Definition_Annotation_to_Leader_Example_JS.htm"
---

# Attach Block Definition Annotation to Leader Example (JS)

## Attach Block Definition Annotation to Leader Example (JavaScript)

| This example attaches a Block definition annotation to a Leader. Start DraftSight. Click Insert to insert a Leader to which to attach a Block definition annotation. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,Leaders">
<meta name=MS-HKWD content="JavaScript examples,Block definitions">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockDefinition.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLeader.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>

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

            //Construct a line
            var mLine = mSkMgr.InsertLine(1, 1, 0, 6, 1, 0);

            //Constuct another line
            var mLine2 = mSkMgr.InsertLine(2, 2, 0, 2, 20, 0);

            var longArray = new Array();
            longArray[0] = 21;
            longArray[1] = 21;

            var entityArray = new Array();
            entityArray[0] = mLine;
            entityArray[1] = mLine2;

            var mBlockDefinition = mDoc.CreateBlockDefinition("MyBlockAnnotation", "Block annotation to attach to Leader", 0, 0, 0, longArray, entityArray, "dsBlockDefinitionEntities_ConvertToBlock");
            printOut(mBlockDefinition.GetName());

            //Add Leader
            var leaderCoordinates = new Array();
            leaderCoordinates[0] = 6.5;
            leaderCoordinates[1] = 7.2;
            leaderCoordinates[2] = 0;
            leaderCoordinates[3] = 7.7;
            leaderCoordinates[4] = 8.6;
            leaderCoordinates[5] = 0;
            var noteWidth = 1.0;
            var noteText = "L1 ";
            var mLeader = mSkMgr.InsertLeader(leaderCoordinates, noteWidth, noteText);

            //Create point where to insert Block definition annotation
            var firstX = 10;
            var firstY = 20;
            var firstZ = 0;
            var mMathUtility = mApp.GetMathUtility();
            var mMathPoint = mMathUtility.CreatePoint(firstX, firstY, firstZ);

           //Attach Tolerance annotation
           mLeader.SetBlockAnnotation("MyBlockAnnotation", mMathPoint);

           //Zoom to fit
           var lowerLeftArray = [0,0,0]
           var upperRightArray = [0,0,0]
           mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

           //Type your JavaScript API code here
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Attach Block Definition Annotation to Leader Example (JS)</title>

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

    <H1>Attach Block Definition Annotation to Leader Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example attaches a Block definition annotation
							to a Leader.&nbsp;<ol>
                            <li>Start DraftSight.<li>Click <b>Insert </b>to
							insert a Leader to which to attach a Block
							definition annotation.<li>Examine the drawing.</ol>
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

---
title: "Prompt for Mouse or Keyword Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Prompt_for_Mouse_or_Keyword_Example_JS.htm"
---

# Prompt for Mouse or Keyword Example (JS)

## Prompt for Mouse or Keyword Example (JavaScript)

| This example inserts a HyperLink, which you can use to send an email message from a DraftSight drawing. Start DraftSight. Using the following form, specify where to place the HyperLink: Select Prompt for mouse or keyword. Click Insert . Follow the command window prompts to insert the HyperLink in the graphics area. Inspect the Output window. Examine the drawing and locate the HyperLink (i.e., place your cursor over a red line). Ctrl-click the HyperLink to open the email message. Change the email address of the recipient. Type the subject and body for the email message. Send the email message. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,command window">
<meta name=MS-HKWD content="JavaScript examples,HyperLinks">
<meta name=MS-HKWD content="JavaScript examples,3D PolyLines">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,prompts">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsHyperLink.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine3D.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsTracker.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPlane.js"></script>

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
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var mCom = mApp.GetCommandMessage();
            var mathUtil = mApp.GetMathUtility();
            if (document.inputform.Choose.checked){
                //This is for the "Point in drawing" option
                //You must assign dsPoint.X, dsPoint.Y, and dsPoint.Z to the same variables
                //that are assigned in the "Type coordinates" option
                var globalArr = [];
                var localArr = [];
                var resultPoint;
                var keyword;
                var modificators;
                var mouseResult;

                //var tracker = mApp.CreateTracker();
				//mCom.AddTracker(tracker);

				var xy_plane = mathUtil.CreateXYPlane();

                var basePoint = mathUtil.CreatePoint(1.77,4.86,0.0);

                var ret = mCom.PromptForMouseOrKeyword2("Select where to place the upper-left corner:", "Invalid first input", globalArr, localArr, 0, false, basePoint, basePoint, xy_plane);

                printOut("Prompt result type: " + ret.Result);
                printOut("Mouse result: " + ret.MouseResult);
                printOut("Modificators: " + ret.Modificators);
                printOut("Keyword: " + ret.Keyword);
                printOut("Upper-left x coordinate: " + ret.ResultPoint.GetPosition().X);
                printOut("Upper-left y coordinate: " + ret.ResultPoint.GetPosition().Y);
                printOut("Upper-left z coordinate: " + ret.ResultPoint.GetPosition().Z);

                var X1 = ret.ResultPoint.GetPosition().X
                var Y1 = ret.ResultPoint.GetPosition().Y;
                var Z1 = ret.ResultPoint.GetPosition().Z;

                var basePoint2 = mathUtil.CreatePoint(7.019, 1.6722, 0.0);
                var ret = mCom.PromptForMouseOrKeyword2("Select where to place the lower-right corner:", "Invalid second input", globalArr, localArr, 0, false, basePoint2, basePoint2, xy_plane);

                //mCom.RemoveTracker(tracker);

                printOut("");
                printOut("Prompt result type: " + ret.Result);
                printOut("Mouse result: " + ret.MouseResult);
                printOut("Modificators: " + ret.Modificators);
                printOut("Keyword: " + ret.Keyword);
                printOut("Lower-right x coordinate: " + ret.ResultPoint.GetPosition().X);
                printOut("Lower-right y coordinate: " + ret.ResultPoint.GetPosition().Y);
                printOut("Lower-right z coordinate: " + ret.ResultPoint.GetPosition().Z);

                var X2 = ret.ResultPoint.GetPosition().X;
                var Y2 = ret.ResultPoint.GetPosition().Y;
                var Z2 = ret.ResultPoint.GetPosition().Z;
            }

            var link = mSkMgr.AttachLinkToArea(X1, Y1, Z1, X2, Y2, Z2, "mailto:nobody@draftsight.com", "Send an email to nobody.");
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Prompt for Mouse or Keyword Example (JS)</title>

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

    <H1>Prompt for Mouse or Keyword Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
               <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example inserts a HyperLink, which you can use to
							send an email message from a DraftSight
							drawing. <ol>
                            <li>Start DraftSight.<li>Using the following form, specify where to place the HyperLink:</li>
                            	<ol>
									<li>Select <b>Prompt for mouse or keyword.</b></li>
									<li>Click <b>Insert</b>.</li>
									<li>Follow the command window prompts to
									insert the HyperLink in the graphics area.</li>
									<li>Inspect the Output window.</li>
								</ol>
								<li>Examine the drawing and locate the HyperLink (i.e., place your cursor over a red line).</li>
								<li>Ctrl-click the HyperLink to open the email message.</li>
								<li>Change the email address of the recipient.</li>
								<li>Type the subject and body for the email message.</li>
								<li>Send the email message.</li>
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
										<li>Save the
										file as an HTML file. </li>
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
                    <td class="style2" height="574">
                        <form name="inputform">
                            <table class="style3" width="460">
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;<input id="R2" name="Choose"
                                            type="radio" value="2" />Prompt for
										mouse or keyword</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        &nbsp;</td>
                                    <td class="style6" width="432">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style6" colspan="2">
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

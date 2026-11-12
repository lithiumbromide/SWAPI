---
title: "Insert HyperLink Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_HyperLink_Example_JS.htm"
---

# Insert HyperLink Example (JS)

## Insert HyperLink Example (JavaScript)

| This example inserts a HyperLink, which you can use to send an email message from a DraftSight drawing. Start DraftSight. Using the following form, specify where to place the HyperLink: Select Coordinates . Type x1, y1, z1, x2, y2, and z2 coordinates. Click Insert . - or - Select Point in drawing. Click Insert . Click anywhere in the drawing to insert the HyperLink at that point. Examine the drawing and locate the HyperLink (i.e., place your cursor over a red line). Ctrl-click the HyperLink to open the email message. Change the email address of the recipient. Type the subject and body for the email message. Send the email message. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
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
<meta name=MS-HKWD content="JavaScript examples,3D PolyLines">
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
            if (document.inputform.Choose[0].checked){
                //This is for the "Type coordinates" option
                //You must add text boxes in the HTML file to implement the "Type coordinates" option
                var X1 = parseFloat(document.getElementById("X1").value);
                var Y1 = parseFloat(document.getElementById("Y1").value);
                var Z1 = parseFloat(document.getElementById("Z1").value);
                var X2 = parseFloat(document.getElementById("X2").value);
                var Y2 = parseFloat(document.getElementById("Y2").value);
                var Z2 = parseFloat(document.getElementById("Z2").value);
            }
            else if (document.inputform.Choose[1].checked){
                var dsPoint1 = mCom.PromptForPoint("Select where to place the upper-left corner:");
                //This is for the select a point in DraftSight
                //You must assign dsPoint.X, dsPoint.Y, and dsPoint.Z to the same variables
                //that are assigned in the "Type coordinates" option
                var X1 = dsPoint1.X;
                var Y1 = dsPoint1.Y;
                var Z1 = dsPoint1.Z;
                var dsPoint2 = mCom.PromptForPoint("Select where to place the lower-right corner:");
                var X2 = dsPoint2.X;
                var Y2 = dsPoint2.Y;
                var Z2 = dsPoint2.Z;
            }
            //Type your JavaScript API here
            var link = mSkMgr.AttachLinkToArea(X1, Y1, Z1, X2, Y2, Z2, "mailto:nobody@draftsight.com", "Send an email to nobody.");
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Insert HyperLink Example (JS)</title>

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

    <H1>Insert HyperLink Example (JavaScript)</H1>

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
                            <li>Select <b>Coordinates</b>.</li>
                            <li>Type x1, y1, z1, x2, y2, and z2 coordinates.</li>
                            <li>Click <b>Insert</b>.</li>
                            <ul>- or -</ul>
                            </ol>
                            <ol>
                            <li>Select <b>Point in drawing.</b></li>
                            <li>Click <b>Insert</b>.</li>
                            <li>Click anywhere in the drawing to insert the HyperLink at that point.</li>
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
										the file as an HTML file. </li>
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
                                        <input id="R1" type="radio" name="Choose" checked="true" value="1"/>Coordinates&nbsp;&nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" width="18">
                                        &nbsp;</td>
                                    <td class="style4" width="432">
                                        X1:
										<input id="X1" type="text" value="0.0" size="9"/> Y1:
										<input id="Y1" type="text" value="0.0" size="11" /> Z1:
										<input id="Z1" type="text" value="0.0" size="9" /><br />
                                        X2:
										<input id="X2" type="text" value="10.0" size="9"/> Y2:
										<input id="Y2" type="text"
                                            value="-10.0" size="11" /> Z2:
										<input id="Z2" type="text" value="0.0" size="9" /></td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        &nbsp;</td>
                                    <td class="style6" width="432">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style4" colspan="2">
                                        &nbsp;<input id="R2" name="Choose"
                                            type="radio" value="2" />Point in drawing</td>
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

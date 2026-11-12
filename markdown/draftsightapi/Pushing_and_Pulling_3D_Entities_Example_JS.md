---
title: "Pushing and Pulling 3D Entities Example (JavaScript)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Pushing_and_Pulling_3D_Entities_Example_JS.htm"
---

# Pushing and Pulling 3D Entities Example (JavaScript)

| This example shows how to pull a polyline into a 3D entity. Start DraftSight. Using the following form: Click Go . Inspect the Output text area. Follow the command window prompts in DraftSight, if any. Examine the drawing. You should see a polyline pulled into a 3D entity. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

    <head>
    <meta name=MS-HKWD content="JavaScript examples">
    <meta name=MS-HKWD content="JavaScript examples,flat shots">

    <!-- Without this line, this does not work in Internet Explorer 8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=8" >
    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" >

    <!-- Add your dsInterface .js Files here -->
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModel.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSketchManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsExtrusion.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsViewManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSolid3D.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLoft.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLoftedSurface.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSweep.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSweptSurface.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockInstance.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockDefinition.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>

    <!-- This is the main block where you place the JavaScript API code -->
    <script type="text/javascript">
        function printOut(str) {
            document.getElementById("OB").value += str + "\n";
            document.getElementById("OB").scrollTop += document.getElementById("OB").scrollHeight;
        }

        function runMacro() {
            try {

                apiCode();
            }
            catch (err) {
            //This is to catch any errors and exit out of the code
            //It displays an error in the output box
                printOut(djErrorString(err));
            }
        }
        function apiCode() {

            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mViewMgr = mDoc.GetViewManager();
            var dsMathUtility = mApp.GetMathUtility();

            mViewMgr.SetPredefinedView("dsPredefinedView_SWIsometric");

            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var lowerLeftArray = [0,0,0];
            var upperRightArray = [0,0,0];
            var coordinates = [308.611,244.543,308.611,133.606,440.093,133.606,440.093,244.543];
            var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
            var dsCircle = mSkMgr.InsertCircle(60.029, 196.265, 0.0, 100.0);
            var InternalPoint = dsMathUtility.CreatePoint(308.611, 244.543, 0.0);
            mSkMgr.PushPullEntities(InternalPoint, 300);

            mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Pushing and Pulling 3D Entities Example (JavaScript)</title>

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
	border-left-color: #ccccff;
	border-right-color: #ccccff;
	border-top-color: #ccccff;
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

    <H1>Pushing and Pulling 3D Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
               <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to
							pull a polyline into a 3D entity. <ol>
                            <li>Start DraftSight.<li>Using the following form:</li>
                            	<ol>
									<li>Click <strong>Go</strong><b>.</b></li>
									<li>Inspect the Output
									text area.</li>
								</ol>
								<li>Follow the command window prompts in
								DraftSight, if any.</li>
								<li>Examine the drawing. You should see a
								polyline pulled into a 3D entity.</li>
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
                         	<hr >
                    </td>
                </tr>
                <tr>
                    <td class="style2" height="574">
                        <form name="inputform">
                            <table class="style3" style="width: 539px">
                                <tr>
                                    <td class="style6">
                                        &nbsp;<input id="Button1" type="button" value="Go" onclick="runMacro()" ></td>
                                </tr>
                            </table>
                            <div class="style19">
                                <h3 class="style20">
                                    Output</h3>
                            <textarea id="OB" cols="50" name="Output" rows="10" readonly="readonly"></textarea>
								<hr >
								<p>&nbsp;</div>
                        </form>
                    </td>
                </tr>

            </tbody>
        </table>

    </body>
</html>
```

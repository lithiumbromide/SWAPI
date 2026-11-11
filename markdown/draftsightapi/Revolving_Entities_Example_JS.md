---
title: "Revolving Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Revolving_Entities_Example_JS.htm"
---

# Revolving Entities Example (JS)

## Revolving Entities Example (JavaScript)

| This example shows how to revolve 3D solids and surfaces. Start DraftSight. Using the following form: Specify which 3D revolve to perform. Click Go . Inspect the Output text area. Follow the command window prompts in DraftSight, if any. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

    <head>
    <meta name=MS-HKWD content="JavaScript examples">
    <meta name=MS-HKWD content="JavaScript examples,revolves">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsExtrudedSurface.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsViewManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSolid3D.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLoft.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLoftedSurface.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsRevolve.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsRevolvedSurface.js"></script>

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

            mViewMgr.SetPredefinedView("dsPredefinedView_SWIsometric");

            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var lowerLeftArray = [0,0,0];
            var upperRightArray = [0,0,0];
            if (document.inputform.R2.checked){
                //Revolve entities to solid by object

                var coordinates = [-231.229,148,-231.229,76.963,-157.191,76.963,-157.191,148];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(-199.212, 233.044, 0.0, 48.357);
                var mLine = mSkMgr.InsertLine(-111.167, 282.069, 0, -111.167, 83.966, 0);
                var mEntities = [mPolyline, mCircle];
                var revolveArray = [mLine];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSolidByObject(mEntities, revolveArray, 360.0);
                //printOut(revolves.length);
                var revolve = revolves[0];
                var dsColor = mApp.GetColorByIndex(2);
                revolve.put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);
            }
            else if (document.inputform.R3.checked) {
                //Extrude entities to surface by object

                var coordinates = [-231.229,148,-231.229,76.963,-157.191,76.963,-157.191,148];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(-199.212, 233.044, 0.0, 48.357);
                var mLine = mSkMgr.InsertLine(-111.167, 282.069, 0, -111.167, 83.966, 0);
                var mEntities = [mPolyline, mCircle];
                var revolveArray = [mLine];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSurfaceByObject(mEntities, revolveArray, 360.0);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R4.checked) {
                //Revolve entities to solid by X-axis

                var coordinates = [107.848,158.077,107.848,74.014,212.128,74.014,212.128,158.077];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline1.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(153.603, 252.781, 0.0, 52.831);
                var mEntities2 = [mPolyline1, mCircle];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSolidByXAxis(mEntities2, 360.0, true);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R5.checked) {
                //Revolve entities to surface by X-axis

                var coordinates = [107.848,158.077,107.848,74.014,212.128,74.014,212.128,158.077];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline1.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(153.603, 252.781, 0.0, 52.831);
                var mEntities2 = [mPolyline1, mCircle];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSurfaceByXAxis(mEntities2, 360.0, true);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R6.checked) {
                //Revolve entities to solid by axis

                var coordinates = [435.587,167.654,435.587,98.488,483.471,98.488,483.471,167.654];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline1.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(447.292, 270.87, 0.0, 41.116);
                var mEntities1 = [mPolyline1, mCircle];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSolidByAxis(mEntities1, 447.292, 270.87, 0.0, 483.471, 167.654, 0.0, 360.0);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R7.checked) {
                //Revolve entities to surface by axis

                var coordinates = [435.587,167.654,435.587,98.488,483.471,98.488,483.471,167.654];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                mPolyline1.put_Elevation(100);
                var mCircle = mSkMgr.InsertCircle(447.292, 270.87, 0.0, 41.116);
                var mEntities1 = [mPolyline1, mCircle];
                var revolves = [];

                revolves = mSkMgr.RevolveEntitiesToSurfaceByAxis(mEntities1, 447.292, 270.87, 0.0, 483.471, 167.654, 0.0, 360.0);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }

            else {
                //No selection
            	printOut("Please select an option.");
            }

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Revolving Entities Example (JS)</title>

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
    .auto-style3 {
		border-width: 0;
		height: 30px;
		text-align: left;
		font-family: Verdana, sans-serif;
		color: #006600;
		font-weight: bold;
	}
    </style>

    </head>

    <H1>Revolving Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
               <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to
							revolve 3D solids
							and surfaces. <ol>
                            <li>Start DraftSight.<li>Using the following form:</li>
                            	<ol>
									<li>Specify which 3D revolve to perform.</li>
									<li>Click <strong>Go</strong><b>.</b></li>
									<li>Inspect the Output
									text area.</li>
								</ol>
								<li>Follow the command window prompts in
								DraftSight, if any.</li>
								<li>Examine the drawing.</li>
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
                         	<hr >
                    </td>
                </tr>
                <tr>
                    <td class="style2" height="574">
                        <form name="inputform">
                            <table class="style3" style="width: 539px">
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R2" name="Choose" type="radio" value="2"></td>
                                    <td class="auto-style3" width="432">
                                        Revolve entities to solid by object<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R3" name="Choose" type="radio" value="3"></td>
                                    <td class="style6" width="432">
                                        Revolve entities to surface by object<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R4" name="Choose" type="radio" value="4"></td>
                                    <td class="style6" width="432">
                                        Revolve entities to solid by X-axis<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R5" name="Choose" type="radio" value="5"></td>
                                    <td class="style6" width="432">
                                        Revolve entities to surface by X-axis</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R6" name="Choose" type="radio" value="6"></td>
                                    <td class="style6" width="432">
                                        Revolve entities to solid by axis</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R7" name="Choose" type="radio" value="7"></td>
                                    <td class="style6" width="432">
                                        Revolve entities to surface by axis</td>
                                </tr>
                                <tr>
                                    <td class="style6" colspan="2">
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

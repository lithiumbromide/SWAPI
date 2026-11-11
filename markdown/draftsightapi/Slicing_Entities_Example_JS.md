---
title: "Slicing Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Slicing_Entities_Example_JS.htm"
---

# Slicing Entities Example (JS)

## Slicing Entities Example (JavaScript)

| This example shows how to slice 3D solids and surfaces. Start DraftSight. Using the following form: Specify which 3D slice to perform. Click Go . Inspect the Output text area. Follow the command window prompts in DraftSight, if any. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

    <head>
    <meta name=MS-HKWD content="JavaScript examples">
    <meta name=MS-HKWD content="JavaScript examples,slicing">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSweep.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSweptSurface.js"></script>
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>

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
            var dsMathUtility = mApp.GetMathUtility();
            var lowerLeftArray = [0,0,0];
            var upperRightArray = [0,0,0];
            if (document.inputform.R2.checked){
                //Slice entities by 3 points

                var coordinates = [30.7029,12.4677,30.7029,10.2257,28.4117,10.2257,28.4117,12.4677];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                var dsEntities = [mPolyline];
                var extrudes = [];
                extrudes = mSkMgr.ExtrudeEntitiesToSolidByHeight(dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes.ExtrusionArray;
                var FirstPoint = dsMathUtility.CreatePoint(28.4117, 10.2257, 4.0);
                var SecondPoint = dsMathUtility.CreatePoint(30.7029, 12.4677, 4.0);
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj = [];

                obj = mSkMgr.SliceEntitiesBy3Points(extrusions, FirstPoint, SecondPoint, ThirdPoint, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(1);
                obj.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);
            }
            else if (document.inputform.R3.checked) {
                //Slice entities by planar entity

                var coordinates = [31.3452,6.8946,31.3452,9.2404,33.888,9.2404,33.888,6.8946];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                var mCircle = mSkMgr.InsertCircle(32.6166, 8.0675, 2.0, 0.98);
                var dsEntities = [mPolyline];
                var extrudes1 = [];
                extrudes1 = mSkMgr.ExtrudeEntitiesToSolidByHeight( dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes1.ExtrusionArray;
                var dsEntityPlanar = [mCircle];
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj1 = [];

                obj1 = mSkMgr.SliceEntitiesByPlanarEntity(extrusions, dsEntityPlanar, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(2);
                obj1.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R4.checked) {
                //Slices entities by surface

                var coordinates = [34.5488,3.2662,34.5488,5.8077,37.1209,5.8077,37.1209,3.2662];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var dsEntities = [mPolyline1];
                var extrudes2 = [];
                extrudes2 = mSkMgr.ExtrudeEntitiesToSolidByHeight( dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes2.ExtrusionArray;
                var mLine = mSkMgr.InsertLine(35.8348, 3.2662, 0.0, 35.8348, 5.8077, 0.0);
                var dsEntities = [mLine];
                var extrudesSur = [];
                extrudesSur = mSkMgr.ExtrudeEntitiesToSurfaceByHeight( dsEntities, 4.0, 0);
                var extrudedSurfaces = [];
                extrudedSurfaces = extrudesSur.ExtrudedSurfaceArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj2 = [];

                obj2 = mSkMgr.SliceEntitiesBySurface (extrusions, extrudedSurfaces, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(3);
                obj2.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R5.checked) {
                //Slice entities by view

                var coordinates = [51.3856,-14.871,51.3856,-12.0151,54.0805,-12.0151,54.0805,-14.871];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var dsEntities = [mPolyline1];
                var extrudes7 = [];
                extrudes7 = mSkMgr.ExtrudeEntitiesToSolidByHeight (dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes7.ExtrusionArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj7 = [];
                var aPoint = dsMathUtility.CreatePoint(52.733, -14.871, 0.0);

                obj7 = mSkMgr.SliceEntitiesByView(extrusions, aPoint, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(4);
                obj7.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R6.checked) {
                //Slice entities by XY-plane

                var coordinates = [37.9451,-0.4819,37.9451,2.3739,40.64,2.3739,40.64,-0.4819];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var extrudes3 = [];
                var dsEntities = [mPolyline1];
                extrudes3 = mSkMgr.ExtrudeEntitiesToSolidByHeight( dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes3.ExtrusionArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj3 = [];
                var aPoint = dsMathUtility.CreatePoint(37.9451, -0.4819, 2.0);

                obj3 = mSkMgr.SliceEntitiesByXY(extrusions, aPoint, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(5);
                obj3.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R7.checked) {
                //Slice entities by YZ-plane

                var coordinates = [41.2617,-4.0399,41.2617,-1.1841,43.9566,-1.1841,43.9566,-4.0399];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var extrudes4 = [];
                var dsEntities = [mPolyline1];
                extrudes4 = mSkMgr.ExtrudeEntitiesToSolidByHeight( dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes4.ExtrusionArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj4 = [];
                var aPoint = dsMathUtility.CreatePoint(42.60915, -4.0399, 4.0);

                obj4 = mSkMgr.SliceEntitiesByYZ(extrusions, aPoint, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(6);
                obj4.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R8.checked) {
                //Slice entities by ZX-plane

                var coordinates = [44.7029,-7.6823,44.7029,-4.8264,47.3978,-4.8264,47.3978,-7.6823];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var extrudes5 = [];
                var dsEntities = [mPolyline1];
                extrudes5 = mSkMgr.ExtrudeEntitiesToSolidByHeight (dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes5.ExtrusionArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj5 = [];
                var aPoint = dsMathUtility.CreatePoint(44.7029, -6.25435, 4.0);

                obj5 = mSkMgr.SliceEntitiesByZX (extrusions, aPoint, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(1);
                obj5.ObjectsArray[0].put_Color(dsColor);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray);

            }
            else if (document.inputform.R9.checked) {
                //Slice entities by Z-axis

                var coordinates = [48.056,-11.3057,48.056,-8.4498,50.7509,-8.4498,50.7509,-11.3057];
                var mPolyline1 = mSkMgr.InsertPolyline2D(coordinates, true);
                var extrudes6 = [];
                var dsEntities = [mPolyline1];
                extrudes6 = mSkMgr.ExtrudeEntitiesToSolidByHeight (dsEntities, 4.0, 0);
                var extrusions = [];
                extrusions = extrudes6.ExtrusionArray;
                var ThirdPoint = dsMathUtility.CreatePoint(0.0, 0.0, 0.0);
                var obj6 = [];
                var aPoint = dsMathUtility.CreatePoint(49.4034, -11.3057, 0.0);
                var aPoint2 = dsMathUtility.CreatePoint(50.7509, -11.3057, 2.0);

                obj6 = mSkMgr.SliceEntitiesByZAxis (extrusions, aPoint, aPoint2, true, ThirdPoint);
                var dsColor = mApp.GetColorByIndex(2);
                obj6.ObjectsArray[0].put_Color(dsColor);

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
    <title>Slicing Entities Example (JS)</title>

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

    <H1>Slicing Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
               <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to
							slice 3D solids
							and surfaces. <ol>
                            <li>Start DraftSight.<li>Using the following form:</li>
                            	<ol>
									<li>Specify which 3D slice to perform.</li>
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
                                        Slice entities by 3 points<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R3" name="Choose" type="radio" value="3"></td>
                                    <td class="style6" width="432">
                                        Slice entities by planar entity<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R4" name="Choose" type="radio" value="4"></td>
                                    <td class="style6" width="432">
                                        Slice entities by surface<br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R5" name="Choose" type="radio" value="5"></td>
                                    <td class="style6" width="432">
                                        Slice entities by view</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R6" name="Choose" type="radio" value="6"></td>
                                    <td class="style6" width="432">
                                        Slice entities by XY plane</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R7" name="Choose" type="radio" value="7"></td>
                                    <td class="style6" width="432">
                                        Slice entities by YZ plane</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R8" name="Choose" type="radio" value="8"></td>
                                    <td class="style6" width="432">
                                        Slice entities by ZX plane</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R9" name="Choose" type="radio" value="9"></td>
                                    <td class="style6" width="432">
                                        Slice entities by Z-axis</td>
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

---
title: "Unifying, Subtracting, and Intersecting Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Unifying_Subtracting_Intersecting_Entities_Example_JS.htm"
---

# Unifying, Subtracting, and Intersecting Entities Example (JS)

## Unifying, Subtracting, and Intersecting Entities Example (JavaScript)

| This example shows how to perform union, subtract, and intersect operations on 3D solids. Start DraftSight. Using the following form: Specify which 3D solid operation to perform: Unite, Subtract, or Intersect. Click Go . Inspect the Output text area. Follow the command window prompts in DraftSight, if any. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,unions">
<meta name=MS-HKWD content="JavaScript examples,subtracts">
<meta name=MS-HKWD content="JavaScript examples,intersects">
<meta name=MS-HKWD content="JavaScript examples,prompts">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsExtrusion.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsViewManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsPolyLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSolid3D.js"></script>

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
            var lowerLeftArray = [0,0,0]
            var upperRightArray = [0,0,0]
            if (document.inputform.R2.checked){
                //Unite
                var coordinates = [0.8839,7.3348,0.8839,6.0943,9.3647,6.0943,9.3647,7.3348];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                var coordinates = [5.8839,12.3348,5.8839,11.0943,14.3647,11.0943,14.3647,12.3348];
                var mPolyline2 = mSkMgr.InsertPolyline2D(coordinates, true);

                var polyLineArr = [mPolyline];
                var solid3D_1 = mSkMgr.PolysolidByEntities(polyLineArr, 4.0, 0.25, "dsPolySolidJustification_Left");

                var polyLineArr2 = [mPolyline2];
                var solid3D_2 = mSkMgr.PolysolidByEntities(polyLineArr2, 4.0, 0.25, "dsPolySolidJustification_Left");

                var solidArr = [solid3D_1, solid3D_2];
                var obj = [];

                mSkMgr.UnionEntities(solidArr, obj);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)
                           }
            else if (document.inputform.R3.checked) {
                //Subtract
                var coordinates = [22.507,8.2407,22.507,13.8125,36.4164,13.8125,36.4164,8.2407];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                var coordinates = [30.7029,12.4677,30.7029,10.2257,28.4117,10.2257,28.4117,12.4677];
                var mPolyline2 = mSkMgr.InsertPolyline2D(coordinates, true);

                var extrudes1 = [];
                var extrudes2 = [];

                var polyLineArr = [mPolyline];
                var solid3D_1 = mSkMgr.ExtrudeEntitiesToSolidByHeight(polyLineArr, 4.0, 0, extrudes1);

                var polyLineArr2 = [mPolyline2];
                var solid3D_2 = mSkMgr.ExtrudeEntitiesToSolidByHeight(polyLineArr2, 4.0, 0, extrudes2);

                var solidArr = [solid3D_1, solid3D_2];
                var obj = [];

                mSkMgr.SubtractEntities(extrudes2, extrudes1, obj);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

            }
            else if (document.inputform.R4.checked) {
                //Intersect
                var coordinates = [22.178,3.6354,22.178,-2.0369,36.1998,-2.0369,36.1998,3.6354];
                var mPolyline = mSkMgr.InsertPolyline2D(coordinates, true);
                var coordinates = [36.1998,-2.0369,36.1998,2.124,30.3079,2.124,30.3079,-2.0369];
                var mPolyline2 = mSkMgr.InsertPolyline2D(coordinates, true);

                var polyLineArr = [mPolyline];
                var solid3D_1 = mSkMgr.PolysolidByEntities(polyLineArr, 4.0, 0.25, "dsPolySolidJustification_Left");

                var polyLineArr2 = [mPolyline2];
                var solid3D_2 = mSkMgr.PolysolidByEntities(polyLineArr2, 4.0, 0.25, "dsPolySolidJustification_Left");

                var solidArr = [solid3D_1, solid3D_2];
                var obj = [];

                mSkMgr.IntersectEntities(solidArr, obj);

                mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)

            }
            else {
                //No selection
            	printOut("Please select an option.");
            }

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Unifying, Subtracting, and Intersecting Entities Example (JS)</title>

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
    .auto-style3 {
		border-width: 0;
		height: 30px;
		text-align: left;
		font-family: Verdana, sans-serif;
		color: #006600;
		font-weight: bold;
	}
    .auto-style4 {
		font-weight: normal;
	}
    </style>

    </head>

    <H1>Unifying, Subtracting, and Intersecting Entities Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
               <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to perform union, subtract, and intersect operations
on 3D solids. <ol>
                            <li>Start DraftSight.<li>Using the following form:</li>
                            	<ol>
									<li>Specify which 3D solid operation to
									perform: Unite, Subtract, or Intersect.</li>
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
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2" height="574">
                        <form name="inputform">
                            <table class="style3" style="width: 539px">
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R2" name="Choose" type="radio" value="2"></td>
                                    <td class="auto-style3" width="432" style="height: 30">
                                        Unite
										<span class="auto-style4">(creates two PolySolids and unites them)</span><br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R3" name="Choose" type="radio" value="3"></td>
                                    <td class="style6" width="432">
                                        Subtract
										<span class="auto-style4">(creates two Extrusions and subtracts them)</span><br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" width="18">
                                        <input id="R4" name="Choose" type="radio" value="4"></td>
                                    <td class="style6" width="432">
                                        Intersect
										<span class="auto-style4">(creates two PolySolids and intersects
										them)</span><br>
									</td>
                                </tr>
                                <tr>
                                    <td class="style6" colspan="2">
                                        &nbsp;<input id="Button1" type="button" value="Go" onclick="runMacro()" /></td>
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

    </body>
</html>
```

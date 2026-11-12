---
title: "Rotate, Scale, Project, and Mirror a Line Entity Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm"
---

# Rotate, Scale, Project, and Mirror a Line Entity Example (JS)

## Rotate, Scale, Project, and Mirror a Line Entity Example (JavaScript)

| This example shows how to use a math transform to rotate, scale, project, and mirror a Line entity. Start DraftSight. Using the following form: Type the coordinates of the start point of a Line. Type the coordinates of the end point of a Line. Select the transformation you want to perform. Fill in all fields for the selected transformation. Use double values unless instructed otherwise. Click Transform Line . Inspect the Output. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,math transformations">
<meta name=MS-HKWD content="JavaScript examples,math utility">
<meta name=MS-HKWD content="JavaScript examples,math lines">
<meta name=MS-HKWD content="JavaScript examples,math vectors">
<meta name=MS-HKWD content="JavaScript examples,math points">
<meta name=MS-HKWD content="JavaScript examples,math planes">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPoint.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathUtility.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathLine.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathVector.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathTransform.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsMathPlane.js"></script>
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
                document.getElementById("OB").value = "";
                apiCode();
            }
            catch (err) {
                printOut(djErrorString(err));
            }
        }
        function printMathLineParameters(dsMathLine) {
        	printOut("Math line data");
        	var type = dsMathLine.GetType();
        	printOut("   Type: " + type);
        	var dsStartPoint = dsMathLine.get_StartPoint();
        	var dsEndPoint = dsMathLine.get_EndPoint();
        	printOut("   Start point: " + dsStartPoint.GetPosition().X + ", " + dsStartPoint.GetPosition().Y + ", " + dsStartPoint.GetPosition().Z);
        	printOut("   End point: " + dsEndPoint.GetPosition().X + ", " + dsEndPoint.GetPosition().Y + ", " + dsEndPoint.GetPosition().Z);
        	var dsVector = dsMathLine.GetDirection().Vector;
        	printOut("   Direction: " + dsVector.GetCoordinates().X + ", " + dsVector.GetCoordinates().Y + ", " + dsVector.GetCoordinates().Z);
        	printOut("   Length: " + dsMathLine.GetLength());

        }
        function printMathTransformation(dsMathTransform) {
        	printOut("Math transformation data");
        	var countOfRows = 4;
        	var countOfColumns = 4;
        	for (var i = 0; i < countOfRows; i++) {
        		var rowInformation = "(";
        		for (var j = 0; j < countOfColumns; j++){
        			rowInformation = rowInformation + dsMathTransform.GetElementAt(i,j);
        			if (j != (countOfColumns - 1)) {
        				rowInformation = rowInformation + "  ,  ";
        			}
        		}
        		rowInformation += ");";
        		printOut(rowInformation);
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
            var point1x = parseFloat(document.getElementById("X0").value);
            var point1y = parseFloat(document.getElementById("Y0").value);
			var point1z = parseFloat(document.getElementById("Z0").value);
			var point2x = parseFloat(document.getElementById("X1").value);
			var point2y = parseFloat(document.getElementById("Y1").value);
			var point2z = parseFloat(document.getElementById("Z1").value);
			var dsLine = mSkMgr.InsertLine(point1x, point1y, point1z, point2x, point2y, point2z);
			var dsMathUtility = mApp.GetMathUtility();
			var dsMathLine = dsLine.get_MathLine();
			if (dsMathLine != null) {
            	if (document.inputform.R1[0].checked){
            		//transform by translation
            		printMathLineParameters(dsMathLine);
            		var v1 = parseFloat(document.getElementById("X2").value);
            		var v2 = parseFloat(document.getElementById("Y2").value);
					var v3 = parseFloat(document.getElementById("Z2").value);
            		var dsTranslationVector = dsMathUtility.CreateVector(v1, v2, v3);
            		var dsMathTransform = dsMathUtility.CreateTransformTranslation(dsTranslationVector);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
            	else if (document.inputform.R1[1].checked){
            	    //transform by scaling
            		printMathLineParameters(dsMathLine);
            		var scalefactor = parseFloat(document.getElementById("scalefactor").value);
            		var x3 = parseFloat(document.getElementById("X3").value);
            		var y3 = parseFloat(document.getElementById("Y3").value);
					var z3 = parseFloat(document.getElementById("Z3").value);
            		var dsCenterPoint = dsMathUtility.CreatePoint(x3, y3, z3);
            		var dsMathTransform = dsMathUtility.CreateTransformScaling(dsCenterPoint, scalefactor);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
            	else if (document.inputform.R1[2].checked){
            	    //transform by rotation
            		printMathLineParameters(dsMathLine);
            		var rotationAngle = parseFloat(document.getElementById("rotationangle").value);
            		var x4 = parseFloat(document.getElementById("X4").value);
            		var y4 = parseFloat(document.getElementById("Y4").value);
					var z4 = parseFloat(document.getElementById("Z4").value);
            		var dsCenterPoint = dsMathUtility.CreatePoint(x4, y4, z4);
            		var x5 = parseFloat(document.getElementById("X5").value);
            		var y5 = parseFloat(document.getElementById("Y5").value);
					var z5 = parseFloat(document.getElementById("Z5").value);
            		var dsRotationAxis = dsMathUtility.CreateVector(x5, y5, z5);
            		var dsMathTransform = dsMathUtility.CreateTransformRotation(dsCenterPoint, dsRotationAxis, rotationAngle);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
				else if (document.inputform.R1[3].checked){
					//transform by mirroring about a point
            		printMathLineParameters(dsMathLine);
            		var x6 = parseFloat(document.getElementById("X6").value);
            		var y6 = parseFloat(document.getElementById("Y6").value);
					var z6 = parseFloat(document.getElementById("Z6").value);
            		var dsMirrorPoint = dsMathUtility.CreatePoint(x6, y6, z6);
            		var dsMathTransform = dsMathUtility.CreateTransformMirroringAboutPoint(dsMirrorPoint);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
				else if (document.inputform.R1[4].checked){
					//transform by mirroring about a line
            		printMathLineParameters(dsMathLine);
            		var x7 = parseFloat(document.getElementById("X7").value);
            		var y7 = parseFloat(document.getElementById("Y7").value);
					var z7 = parseFloat(document.getElementById("Z7").value);
					var x8 = parseFloat(document.getElementById("X8").value);
            		var y8 = parseFloat(document.getElementById("Y8").value);
					var z8 = parseFloat(document.getElementById("Z8").value);
            		var dsMirrorLine = dsMathUtility.CreateLine(x7, y7, z7, x8, y8, z8, "dsMathLineType_Bounded");
            		var dsMathTransform = dsMathUtility.CreateTransformMirroringAboutLine(dsMirrorLine);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
				else if (document.inputform.R1[5].checked){
					//transform by mirroring about a plane
            		printMathLineParameters(dsMathLine);
            		var mirrorplane = document.getElementById("mirrorplane").value;
            		if (mirrorplane == "XY") {
            			var dsMirrorPlane = dsMathUtility.CreateXYPlane();
            		}
            		else if (mirrorplane == "ZX") {
            			var dsMirrorPlane = dsMathUtility.CreateZXPlane();
            		}
            		else if (mirrorplane == "YZ") {
            			var dsMirrorPlane = dsMathUtility.CreateYZPlane();
            		}
            		var dsMathTransform = dsMathUtility.CreateTransformMirroringAboutPlane(dsMirrorPlane);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);;
                	printMathLineParameters(dsMathLine);
            	}
				else if (document.inputform.R1[6].checked){
					//transform by projecting onto a plane
            		printMathLineParameters(dsMathLine);
            		var projectionplane = document.getElementById("projectionplane").value;
            		if (projectionplane == "XY") {
            			var dsProjectionPlane = dsMathUtility.CreateXYPlane();
            		}
            		else if (projectionplane == "ZX") {
            			var dsProjectionPlane = dsMathUtility.CreateZXPlane();
            		}
            		else if (projectionplane == "YZ") {
            			var dsProjectionPlane = dsMathUtility.CreateYZPlane();
            		}
            		var x9 = parseFloat(document.getElementById("X9").value);
            		var y9 = parseFloat(document.getElementById("Y9").value);
					var z9 = parseFloat(document.getElementById("Z9").value);
            		var dsProjectionDirection = dsMathUtility.CreateVector(x9, y9, z9);
            		var dsMathTransform = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection);
                	printMathTransformation(dsMathTransform);
                	dsMathLine.TransformBy(dsMathTransform);
                	dsLine.put_MathLine(dsMathLine);
                	printMathLineParameters(dsMathLine);
            	}
			}
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title> Rotate, Scale, Project, and Mirror a Line Entity Example (JS)</title>

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

    <H1> Rotate, Scale, Project, and Mirror a Line Entity Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to use a math transform to rotate, scale, project, and
mirror a Line entity.<ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form:<ol>
                            <li>Type the coordinates of the start point of a
							Line.</li>
							<li>Type the coordinates of the end point of a
							Line.</li>
							<li>Select the transformation you want to perform.</li>
							<li>Fill in all fields for the selected
							transformation. Use double values unless
							instructed otherwise.</li>
							<li>Click <b>Transform Line</b>.</li>
                            </ol>
							<li>Inspect the Output.</li>
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
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3" style="width: 600px">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        Line:</td>
                                </tr>
                                <tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; Start point:</td>
                                </tr>
								<tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X:
										<input id="X0" type="text" value="0.0" class="style22" name="T1" size="20" /> Y:
										<input id="Y0" type="text" value="0.0" class="style22" name="T2" size="20" /> Z:
										<input id="Z0" type="text" value="0.0" class="style22" name="T3" size="20" /></td>
                                </tr>
								<tr>
                                    <td class="style4">
                                        &nbsp;&nbsp;&nbsp; End point:</td>
                                </tr>
								<tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;&nbsp; <b><font color="#006600">&nbsp;&nbsp;&nbsp;&nbsp; X:</font></b>
										<input id="X1" type="text" value="0.0" class="style22" name="T4" size="20" />
										<b><font color="#006600">Y:</font></b>
										<input id="Y1" type="text" value="0.0" class="style22" name="T5" size="20" />
										<b><font color="#006600">Z:</font></b>
										<input id="Z1" type="text" value="0.0" class="style22" name="T6" size="20" /></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">Transform Line
										by:</font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" value="V1" checked name="R1" style="font-weight: 700"><b>Translation</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Translation vector:
										</font></b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X2" type="text" name="T7" size="8">
										Y: <input id="Y2" type="text" name="T9" size="8">
										Z:
										<input id="Z2" type="text" name="T10" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V2" style="font-weight: 700"><b>Scaling</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Scaling factor:
										<input id="scalefactor" type="text" name="T8" size="8"></font></b><p>
										<font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										Center point: </b></font></p>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X3" type="text" name="T31" size="8">
										Y:
										<input id="Y3" type="text" name="T32" size="8">
										Z:
										<input id="Z3" type="text" name="T33" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V3" style="font-weight: 700"><b>Rotation&nbsp;&nbsp;&nbsp;
										</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Rotation vector:
										</font></b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X5" type="text" name="T13" size="8">
										Y:
										<input id="Y5" type="text" name="T14" size="8">
										Z:
										<input id="Z5" type="text" name="T15" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Rotation angle:
										<input id="rotationangle" type="text" name="T34" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Center point: </font>
										</b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X4" type="text" name="T16" size="8">
										Y:
										<input id="Y4" type="text" name="T17" size="8">
										Z:
										<input id="Z4" type="text" name="T18" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V4" style="font-weight: 700"><b>Mirroring
										about a point</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Point: </font>
										</b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X6" type="text" name="T19" size="8">
										Y:
										<input id="Y6" type="text" name="T20" size="8">
										Z:
										<input id="Z6" type="text" name="T21" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V5" style="font-weight: 700"><b>Mirroring
										about a Line</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Start point: </font></b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X7" type="text" name="T22" size="8">
										Y:
										<input id="Y7" type="text" name="T23" size="8">
										Z:
										<input id="Z7" type="text" name="T24" size="8"></font></b></p>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										End point :</b></font></p>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X8" type="text" name="T25" size="8">
										Y:
										<input id="Y8" type="text" name="T26" size="8">
										Z:
										<input id="Z8" type="text" name="T27" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V6" style="font-weight: 700"><b>Mirroring
										about a plane</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Mirror plane (type XY, ZX, or YZ):
										<input id="mirrorplane" type="text" name="T11" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <font color="#006600">
										<input type="radio" name="R1" value="V7" style="font-weight: 700"><b>Projection
										onto a plane</b></font></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Projection plane (type XY, ZX, or YZ):
										<input id="projectionplane" type="text" name="T12" size="20"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        <b><font color="#006600">&nbsp;&nbsp;&nbsp;
										Direction vector: </font></b>
										<p><font color="#006600"><b>&nbsp;&nbsp;&nbsp;
										</b></font><b><font color="#006600">X:
										<input id="X9" type="text" name="T28" size="8">
										Y:
										<input id="Y9" type="text" name="T29" size="8">
										Z:
										<input id="Z9" type="text" name="T30" size="8"></font></b></td>
                                </tr>
                                <tr>
                                    <td class="style6" style="height: 20px">
                                        &nbsp;&nbsp;&nbsp; </td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Transform Line" onclick="runMacro()" />

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

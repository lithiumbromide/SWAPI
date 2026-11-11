---
title: "Insert Shapes Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Shapes_Example_JS.htm"
---

# Insert Shapes Example (JS)

## Insert Shapes Example (JavaScript)

| This example loads a shape file and inserts shapes in the drawing. Start DraftSight. Click Load and Insert to load a shape file and insert shapes in the drawing. LTypeShp.shx is loaded, and the shapes within this file are inserted at the origin of the drawing at a 30 obliquing angle. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,shapes">
<meta name=MS-HKWD content="JavaScript examples,Shape Manager">

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
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsShape.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsShapeManager.js"></script>

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

			//Get Shape Manager
			var mShapeManager = mDoc.GetShapeManager();

			//Load shape file and get shapes
			var shapeFile = "c:\\Program Files\\Dassault Systemes\\DraftSight\\Fonts\\LTypeShp.shx";
			mShapeManager.Load(shapeFile);
			var shapesStrList = mShapeManager.GetAvailableShapes();

			var shapesCount = 0;
			shapesCount = shapesStrList.length;

			//Insert shapes
			var PositionX = 0;
			var PositionY = 0;
			var PositionZ = 0;
			for (var i = 0; i < shapesCount; ++i) {
			    var mShape = mSkMgr.InsertShape(shapesStrList[i], PositionX, PositionY, PositionZ, 1, 0);
			    var angle = 30 * Math.PI / 180;
			    mShape.put_Obliquing(angle);
			    var X1 = 0;
			    var Y1 = 0;
			    var Z1 = 0;
			    var X2 = 0;
			    var Y2 = 0;
			    var Z2 = 0;

			    mShape.GetBoundingBox(X1, Y1, Z1, X2, Y2, Z2);

			    PositionX += (X2 - X1) + 5;

			}

			mApp.releaseAll();
		}
	</script>

	<!-- Change the title so that it describes what the example demonstrates -->
	<title>Insert Shapes Example (JS)</title>

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
		.style3
		{
			width: 460px;
			height: 10px;
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
		.style19
		{
			text-align: left;
		}
		.style20
		{
			text-align: left;
			color: #006600;
		}
		</style>

	</head>

	<h1>Insert Shapes Example (JavaScript)</h1>

	<body>
		<table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
			cellpadding="0" cellspacing="0">

			<tbody>
				<tr>
					<td style="height: 55px">
						<div class="style7">
							This example loads a shape file and inserts shapes in the drawing.&nbsp;<ol>
							<li>Start DraftSight.</li><li>Click <b>Load and Insert </b>to
							load a shape file and insert shapes in the drawing.</li>
								<strong>LTypeShp.shx</strong> is loaded, and the shapes within this file are inserted at the origin of the
								drawing at a 30 obliquing angle.<li>Examine the drawing.</li></ol>
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
										<input id="Button1" type="button" value="Load and Insert" onclick="runMacro()" />

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

---
title: "Load and Activate LineStyles Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Load_and_Activate_LineStyles_Example_JS.htm"
---

# Load and Activate LineStyles Example (JS)

## Load and Activate LineStyles Example (JavaScript)

| This example loads and activates LineStyles. Start DraftSight. Click Load and Activate to load and activate Linestyles. Two Lines are drawn using the loaded and activated LineStyles. Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,LineStyles">
<meta name=MS-HKWD content="JavaScript examples,LineStyle Manager">
<meta name=MS-HKWD content="JavaScript examples,Lines">

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
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLineStyle.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLineStyleManager.js"></script>

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

			//Get LineStyle Manager
			var mLineStyleManager = mDoc.GetLineStyleManager();

			//Load LineStyles
			var LineStyleFile = "c:\\Program Files\\Dassault Systemes\\DraftSight\\Default Files\\Linestyles\\MM.LIN";
			var mColl = mLineStyleManager.LoadLineStyle("BATTING", LineStyleFile);
			var mColl = mLineStyleManager.LoadLineStyle("ZIGZAG", LineStyleFile);

			var mLineStyle = mColl.LineStyle;

			//Construct Line using BATTING LineStyle
			mLineStyle = mLineStyleManager.GetLineStyle("BATTING");
			mLineStyle.Activate();
			var mLine = mSkMgr.InsertLine(0, 0, 0, 100, 100, 0);

			//Constuct Line using ZIGZAG LineStle
			mLineStyle = mLineStyleManager.GetLineStyle("ZIGZAG");
			mLineStyle.Activate();
			var mLine = mSkMgr.InsertLine(100, 0, 0, 200, 100, 0);

		   	mApp.releaseAll();
		}
	</script>

	<!-- Change the title so that it describes what the example demonstrates -->
	<title>Load and Activate LineStyles Example (JS)</title>

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

	<h1>Load and Activate LineStyles Example (JavaScript)</h1>

	<body>
		<table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
			cellpadding="0" cellspacing="0">

			<tbody>
				<tr>
					<td style="height: 55px">
						<div class="style7">
							This example loads and activates LineStyles.&nbsp;<ol>
							<li>Start DraftSight.</li><li>Click <b>Load and
							Activate </b>to
							load and activate Linestyles.</li>
							Two Lines are drawn using the loaded and activated LineStyles.<li>Examine the drawing.</li></ol>
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
										<input id="Button1" type="button" value="Load and Activate" onclick="runMacro()" />

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

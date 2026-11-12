---
title: "Create and Change EntityGroups Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_EntityGroups_Example_JS.htm"
---

# Create and Change EntityGroups Example (JS)

## Create and Change EntityGroups Example (JavaScript)

| This example creates and changes EntityGroups. Start DraftSight. Click Create EntityGroups . Examine Output. Type GROUP at the command-window prompt to verify that only one EntityGroup remains. NOTES: Information and errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,EntityGroups">
<meta name=MS-HKWD content="JavaScript examples,groups">

	<head>

	<!-- Without this line, this does not work in Internet Explorer 8 -->
	<meta http-equiv="X-UA-Compatible" content="IE=8" />

	<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

	<!-- Add your dsInterface .js Files here -->
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplicationOptions.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsGroup.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLine.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsEntityHelper.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSketchManager.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModel.js"></script>

	<!-- This is the main block where you place the JavaScript API -->
	<script type="text/javascript">
		function printOut(str) {
			document.getElementById("OB").value += str;
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
			var dsApp = mScript.getApplication();
			dsApp.AbortRunningCommand();

			//Type your JavaScript API here

			//Insert entities

			var dsDoc = dsApp.GetActiveDocument();
			var dsModel = dsDoc.GetModel();
			var dsSketchMgr = dsModel.GetSketchManager();
			var line1 = dsSketchMgr.InsertLine(0, 0, 0, 10, 10, 0);
			var line2 = dsSketchMgr.InsertLine(5, 0, 0, 15, 10, 0);
			var circle1 = dsSketchMgr.InsertCircle(5, 5, 0, 10);
			var circle2 = dsSketchMgr.InsertCircle(10, 5, 0, 10);

			var EntitiesArray1 = Array(line1, line2);
			var EntitiesArray2 = Array(circle1, circle2);

			var dsGroup1 = dsDoc.CreateGroup("SampleGroup1", false, "This is my first sample group.", EntitiesArray1);

			printOut("SampleGroup1 created.\n");

			var mEntities = dsGroup1.GetEntities();

			//Change color of lines from white to red
			var dsEntityHelper = dsApp.GetEntityHelper();
			var dsColor = dsApp.GetNamedColor("dsNamedColor_Red");

			for (n=0; n < mEntities.EntitiesArray.length; n++){
				dsEntityHelper.SetColor (mEntities.EntitiesArray[n], dsColor);
            }

            printOut("Line entities colors changed from white to red.\n");

			var dsGroup2 = dsDoc.CreateGroup("SampleGroup2", false, "This is my second sample group.", EntitiesArray2);

            printOut("SampleGroup2 created.\n");

			//Get SampleGroup2 and remove circle2
			var dsGroup2 = dsDoc.GetGroup("SampleGroup2");
			if(dsGroup2.HasEntity(circle2)){
				var index = dsGroup2.GetIndex(circle2);
				dsGroup2.RemoveEntityAt (index);
			}

            printOut("circle2 removed from SampleGroup2.\n");

			//Get SampleGroup1 and add circle1 at last position
			var dsGroup1 = dsDoc.GetGroup("SampleGroup1");
			var EntitiesArray = new Array();
			EntitiesArray[0] = circle1;
			var count = dsGroup1.GetEntitiesCount();
			dsGroup1.InsertEntitiesAt(count, EntitiesArray);

			var newCount = dsGroup1.GetEntitiesCount();

			//Move circle1 to second position (index 1)
			circleIndex = dsGroup1.GetIndex(circle1);

			dsGroup1.Reorder(circleIndex, 1, 1);
			circleIndex = dsGroup1.GetIndex(circle1);

            printOut("circle1 added to SampleGroup1, and entities within SampleGroup1 reordered.\n");

			//Explode SampleGroup2
			dsGroup2.Explode();

            printOut("SampleGroup2 exploded.\n");

			//Rename SampleGroup1 and change description
			dsGroup1.Rename ("SampleGroup");
			dsGroup1.put_Description("My sample group.");

            printOut("SampleGroup1 renamed SampleGroup and its description also changed.\n");

			dsApp.releaseAll();
		}
	</script>

	<!-- Change the title so that it shows what the API is going to be used for -->
	<title>Create and Change EntityGroups Example (JS)</title>

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

	<H1>Create and Change EntityGroups Example (JavaScript)</H1>

	<body>
		<table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
			cellpadding="0" cellspacing="0">

			<tbody>
				<tr>
					<td style="height: 55px">
						<div class="style7">
							This example creates and changes EntityGroups.
							<ol>
							<li>Start DraftSight.<li>Click <b>Create EntityGroups</b>.</li>
							<li>Examine Output.</li>
								<li>Type <b>GROUP</b> at the command-window prompt to verify that only one EntityGroup remains.</li>
									 </ol>
							<p><b>NOTES:</b> </p>
							<ul>
								<li>Information and errors are printed to Output.</li>
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
							<table class="style3" width="460">
								<!-- Reuse this row to add more rows-->
								<tr>
									<td colspan="2" class="style6">
										<input id="Button1" type="button" value="Create EntityGroups" onclick="runMacro()" />

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

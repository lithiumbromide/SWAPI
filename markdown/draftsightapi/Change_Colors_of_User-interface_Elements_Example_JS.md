---
title: "Change Colors of User-interface Elements Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Change_Colors_of_User-interface_Elements_Example_JS.htm"
---

# Change Colors of User-interface Elements Example (JS)

## Change Colors of User-interface Elements Example (JavaScript)

| This example changes the colors of user-interface elements. Start DraftSight. Using the following form: Select a color for: Text in command window Crosshair Background of model Click Show . Examine and experiment with the user-interface elements whose colors changed. To reset the colors of the user-interface elements to their defaults: Click Tools > Options > System Options . Expand Display . Expand Element Colors . Click Reset All . Click OK . NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,application options">
<meta name=MS-HKWD content="JavaScript examples,system options">
<meta name=MS-HKWD content="JavaScript examples,Colors">

	<head>

	<!-- Without this line, this does not work in Internet Explorer 8 -->
	<meta http-equiv="X-UA-Compatible" content="IE=8" />

	<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

	<!-- Add your dsInterface .js Files here -->
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplicationOptions.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>

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
			var mApp = mScript.getApplication();
			mApp.AbortRunningCommand();

			//Enter in your JavaScript API here
			var mAppOptions = mApp.GetApplicationOptions();

			var ncolor1 = document.getElementById("C1").value;
			var ncolor2 = document.getElementById("C2").value;
			var ncolor3 = document.getElementById("C3").value;

			var color1 = mAppOptions.GetElementColor("dsElementColor_CommandWindowText");
			var color2 = mAppOptions.GetElementColor("dsElementColor_ModelCrosshair");
			var color3 = mAppOptions.GetElementColor("dsElementColor_ModelBackground");

			printOut("New color of: \n");
            printOut("   Text of command window: " + JSON.stringify(ncolor1) + "\n");
			printOut("   Crosshair: " + JSON.stringify(ncolor2) + "\n");
			printOut("   Background of model: " + JSON.stringify(ncolor3) + "\n");

			color1.SetNamedColor(ncolor1);
			color2.SetNamedColor(ncolor2);
			color3.SetNamedColor(ncolor3);

			mAppOptions.SetElementColor("dsElementColor_CommandWindowText", color1);
			mAppOptions.SetElementColor("dsElementColor_ModelCrosshair", color2);
			mAppOptions.SetElementColor("dsElementColor_ModelBackground", color3);

			mApp.releaseAll();
		}
	</script>

	<!-- Change the title so that it shows what the API is going to be used for -->
	<title>Change Colors of User-interface Elements Example (JS)</title>

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

	<H1>Change Colors of User-interface Elements Example (JavaScript)</H1>

	<body>
		<table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
			cellpadding="0" cellspacing="0">

			<tbody>
				<tr>
					<td style="height: 55px">
						<div class="style7">
							This example changes the colors of user-interface elements.
							<ol>
							<li>Start DraftSight.<li>
							Using the following form:<ol>
								<li>Select a color for:<ul>
									<li><b>Text in command window</b></li>
									<li><b>Crosshair</b></li>
									<li><b>Background of model</b></li>
								</ul>
								</li>
								<li>Click <b>Show</b>.</li>
								<li>Examine and experiment with the
								user-interface elements whose colors changed.</li>
								<li>To reset the colors of the user-interface
								elements to their defaults:<ol>
                                     <li>Click <b>Tools > Options > System Options</b>.</li>
                                     <li>Expand <b>Display</b>.</li>
                                     <li>Expand <b>Element Colors</b>.</li>
                                     <li> Click <b>Reset All</b>.</li>
                                     <li>Click <b>OK</b>.</li>
                                     </ol>
                                     </li>
							</ol>
							<p><b>NOTES:</b> </p>
							<ul>
								<li>Errors are printed to Output.</li>
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
									<!-- Use these two cells to implement inputs, add more rows if necessarily-->
									<td class="style20" width="306">
										<b>Text in command window:</b></td>
									<td class="style5" width="144">
										<select id="C1" name="Color1">
											<option value="dsNamedColor_Red">Red</option>
											<option value="dsNamedColor_Yellow">Yellow</option>
											<option value="dsNamedColor_Green">Green</option>
											<option value="dsNamedColor_Cyan">Cyan</option>
											<option value="dsNamedColor_Blue">Blue</option>
											<option value="dsNamedColor_Magenta">Magenta</option>
											<option value="dsNamedColor_White">White</option>
										</select></td>
								</tr>
								<!-- End of the input row -->
								<tr>
									<td class="style20" width="306">
										<b>Crosshair:</b></td>
									<td class="style5" width="144">
										<select id="C2" name="Color2">
											<option value="dsNamedColor_Red">Red</option>
											<option value="dsNamedColor_Yellow">Yellow</option>
											<option value="dsNamedColor_Green">Green</option>
											<option value="dsNamedColor_Cyan">Cyan</option>
											<option value="dsNamedColor_Blue">Blue</option>
											<option value="dsNamedColor_Magenta">Magenta</option>
											<option value="dsNamedColor_White">White</option>
										</select></td>
								</tr>
								<tr>
									<td class="style20" width="306">
										<b>Background of model:</b></td>
									<td class="style5" width="144">
										<select id="C3" name="Color3">
											<option value="dsNamedColor_Red">Red</option>
											<option value="dsNamedColor_Yellow">Yellow</option>
											<option value="dsNamedColor_Green">Green</option>
											<option value="dsNamedColor_Cyan">Cyan</option>
											<option value="dsNamedColor_Blue">Blue</option>
											<option value="dsNamedColor_Magenta">Magenta</option>
											<option value="dsNamedColor_White">White</option>
										</select></td>
								</tr>
								<tr>
									<td colspan="2" class="style6">
										<input id="Button1" type="button" value="Show" onclick="runMacro()" />

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

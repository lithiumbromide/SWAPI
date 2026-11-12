---
title: "Create and Remove Dictionary Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Remove_Dictionary_Example_JS.htm"
---

# Create and Remove Dictionary Example (JS)

## Create and Remove Dictionary Example (JavaScript)

| This example constructs a Circle in a DraftSight drawing and adds and removes a dictionary to and from the Circle. Start DraftSight. Using the following form: Specify the center point and radius for the Circle: Type the x, y, and z coordinates for the center point of the Circle in Center point X , Center point Y , and Center point Z . Type a radius for the Circle in Radius . Type a name for the Circle's dictionary in Name . Type a name for a record to add to the Circle's dictionary in Record Name . Type the data for the record added to the Circle's dictionary in Record Data . Click Create . Examine the drawing to verify that the Circle was constructed. Examine the Output field in the form to verify: Dictionary was created for the Circle. Record was added to the dictionary. Data was added to the record. Record was removed from the dictionary. Dictionary was released and erased. NOTES: Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,dictionaries">
<meta name=MS-HKWD content="JavaScript examples,XRecords">
<meta name=MS-HKWD content="JavaScript examples,extension dictionaries">

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
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDictionary.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsXRecord.js"></script>

	<!-- This is the main block where you place the JavaScript API -->
	<script type="text/javascript">

			function printOut(str) {
				document.getElementById("OB").value += str + "\n";
				document.getElementById("OB").scrollTop += document.getElementById("OB").scrollHeight;
			}

			function runMacro() {

				//This catches any errors and exits out of the code if caught
				//Errors are displayed in Output field of form
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
					var mDoc = mApp.GetActiveDocument();
					var mModel = mDoc.GetModel();
					var mSkMgr = mModel.GetSketchManager();
					var X = parseFloat(document.getElementById("X").value);
					var Y = parseFloat(document.getElementById("Y").value);
					var Z = parseFloat(document.getElementById("Z").value);
					var R = parseFloat(document.getElementById("R").value)

					//Construct Circle
					var mCircle = mSkMgr.InsertCircle(X, Y, Z, R);

					var dict = document.getElementById("dict").value;
					var rec = document.getElementById("rec").value;
					var recdata = document.getElementById("recdata").value;

					//Create extension dictionary for Circle
					var mCircleDict = mCircle.CreateExtensionDictionary();

					printOut("Name of Circle's dictionary: " + JSON.stringify(dict) + "\n");

					//Add XRecord to Circle extension dictionary
					var mRec = mCircleDict.CreateXRecord(rec);

					printOut("Name of record added to " + JSON.stringify(dict) + ": " + JSON.stringify(rec) + "\n");

					//Add data to XRecord
					mRec.InsertStringData(0, 1, recdata);
					var count = mRec.GetDataCount();
					var strData = mRec.GetStringData(count-1);
					printOut("Data added to " + JSON.stringify(rec) + " in " + JSON.stringify(dict) + ": " + JSON.stringify(strData) + "\n");

					//Remove XRecord from extension dictionary
					mCircleDict.RemoveEntry(rec);
					printOut(JSON.stringify(rec) + " removed from " + JSON.stringify(dict) + "\n");

					//Release and erase the extension dictionary
					var removed = mCircle.ReleaseExtensionDictionary();
					if (removed){
						printOut(JSON.stringify(dict) + " released and removed.");
					}
					mApp.releaseAll();
				}

</script>

	<!-- Change the title so that it shows what the API is going to be used for -->
	<title>Create and Remove Dictionary Example (JS)</title>

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
		.style21
		{
			text-align: left;
			color: #006600;
			width: 265px;
		}
		.style22
		{
			height: 30px;
			text-align: left;
			font-family: Verdana, sans-serif;
			color: #006600;
			font-weight: bold;
			width: 265px;
		}
		</style>

</head>

	<H1>Create and Remove Dictionary Example (JavaScript)</H1>

	   <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
			cellpadding="0" cellspacing="0">

			<tbody>
				<tr>
					<td style="height: 55px">
						<div class="style7">
							This example constructs a Circle in a DraftSight
							drawing and adds and removes a dictionary to and
							from the Circle.
							<ol>
							<li>Start DraftSight.<li>
							Using the following form:</li>
								<li>
									Specify the center point
							and radius for the Circle:<ol>
								<li>Type the x, y, and z coordinates for the
								center point of the Circle in <b>Center point X</b>,
								<b>Center point Y</b>, and <b>Center point Z</b>.</li>
								<li>Type a radius for the Circle in <b>Radius</b>.</li>
							</ol>
							</li>
							<li>Type a name for the Circle&#39;s dictionary in
							<strong>Name</strong>.</li>
							<li>Type a name for a record to add to the Circle&#39;s dictionary
							in <b>Record Name</b>.</li>
							<li>Type the data for the record added to the Circle&#39;s dictionary
							in <b>Record Data</b>.</li>
							<li>Click <b>Create</b>.</li>
							<li>Examine the drawing to verify that the
								Circle was constructed.</li>
							<li>Examine the Output field in the form to verify:<ol>
								<li>Dictionary was created for the Circle.</li>
								<li>Record was added to the dictionary.</li>
								<li>Data was added to the record.</li>
								<li>Record was removed from the dictionary.</li>
								<li>Dictionary was released and
								erased.</li>
							</ol>
							</li>
							</ol>
							<p><b>NOTES:</b></p>
								<ul>
									<li>Errors are also printed to Output.</li>
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
										and running scripts is blocked, allow
										blocked content.</li>
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
									<td class="style21">
										<strong>Circle</strong></td>
									<td class="style20" width="306">
										&nbsp;</td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										<b>Center point X:</b>
									<input type="text" name="CenterX" id="X" value="40.0" size="8" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
									<b>Center point Y:</b>
									<input type="text" name="CenterY" id="Y" value="40.0" size="8" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
									<b>Center point Z:</b>
									<input type="text" name="CenterZ" id="Z"  value="0.0" size="8" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
									<b>Radius:</b>
									<input type="text" name="Radius" id="R"  value="50.0" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										&nbsp;</td>
								</tr>

								<tr>
									<td class="style21">
										<strong>Dictionary</strong></td>
									<td class="style20" width="306">
										&nbsp;</td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										<strong>Name</strong><b>: </b>
									<input type="text" id="dict" value="CircleDictionary1" size="50" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										<strong>Record Name</strong><b>: </b>
									<input type="text" id="rec" value="CircleRecord1" size="50" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										<strong>Record data</strong><b>: </b>
									<input type="text" id="recdata" value="CircleRecord1Data" size="50" /></td>
								</tr>

								<tr>
									<td class="style21">
										&nbsp;</td>
									<td class="style20" width="306">
										&nbsp;</td>
								</tr>

								<tr>
									<td class="style22">
										<button id="Button1" type="button" onclick="runMacro()">Create</button></td></td>
									<td class="style6">
									    &nbsp;</td>
								</tr>

							</table>

							<div class="style19">
								<h3 class="style20">
									Output</h3>
										<textarea id="OB" cols="75" name="Output" rows="10" readonly="readonly"></textarea>
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

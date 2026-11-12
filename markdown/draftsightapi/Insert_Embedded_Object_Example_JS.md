---
title: "Insert Embedded Object Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Embedded_Object_Example_JS.htm"
---

# Insert Embedded Object Example (JS)

## Insert Embedded Object Example (JavaScript)

| Embeds a file object in a DraftSight drawing. Start DraftSight. Using the following form: Type the full path and name of the file to embed in the drawing. Click Run Macro . Inspect the drawing and the Output. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the web page and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,embedded objects">
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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsEmbeddedObject.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsColor.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsLayer.js"></script>

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
        function apiCode() {
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();
            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();
            var file = document.getElementById("File1").value;
            var link = true;
            var displayAsIcon = false;
            var dsEmbeddedObject = mSkMgr.InsertEmbeddedObjectFromFile(file, link, displayAsIcon);
            if (dsEmbeddedObject != null) {
            	var handle = dsEmbeddedObject.get_Handle();
            	printOut("Handle: " + handle);
        		var color = dsEmbeddedObject.get_Color();
				var namedColor = color.GetNamedColor();
				printOut("Color: " + namedColor);
        		var erased = dsEmbeddedObject.get_Erased();
				printOut("Erased? " + erased);
        		var layer = dsEmbeddedObject.get_Layer();
				printOut("Layer: " + layer);
        		var linescale = dsEmbeddedObject.get_LineScale();
				printOut("Line scale: " + linescale);
				var linestyle = dsEmbeddedObject.get_LineStyle();
				printOut("Line style: " + linestyle);
        		var lineweight = dsEmbeddedObject.get_LineWeight();
				printOut("Line weight: " + lineweight);
        		var visible = dsEmbeddedObject.get_Visible();
				printOut("Visible? " + visible);

        		var x1;
				var y1;
				var z1;
        		var x2;
				var y2;
				var z2;
        		var bout = dsEmbeddedObject.GetBoundingBox();
        		printOut("Opposite corners of bounding box: " + bout.X1 + "," +  bout.Y1 + "," + bout.Z1 + " and " +  bout.X2 + "," + bout.Y2 + "," + bout.Z2);

        		//Print embedded object parameters
        		var height = dsEmbeddedObject.get_Height();
				printOut("Height: " + height);
        		var width = dsEmbeddedObject.get_Width();
				printOut("Width: " + width);
        		var printquality = dsEmbeddedObject.get_PrintQuality();
				printOut("Print quality: " + printquality);
        		var linkpath = dsEmbeddedObject.GetLinkPath();
				printOut("Link path: " + linkpath);
       	 		var sourceapp = dsEmbeddedObject.GetSourceApplication();
				printOut("Source application: " + sourceapp);
        		var type = dsEmbeddedObject.GetType();
				printOut("Type of embedded object: " + type);

        		//Get position of embedded object
        		var x;
				var y;
				var z;
        		var pout = dsEmbeddedObject.GetPosition();
        		printOut("Position: " + pout.X + "," + pout.Y + "," + pout.Z);

			}
			else {
			 	printOut("File object was not embedded in the document.");
			}
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title> Insert Embedded Object Example (JS)</title>

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

    <H1> Insert Embedded Object Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            Embeds a file object in a DraftSight drawing.<ol>
                            <li>Start DraftSight.</li>
                            <li>Using the following form:<ol type="a">
                            <li>Type the full path and name of the file to embed in the drawing.</li>
							<li>Click <b>Run Macro</b>.</li>
                            </ol>
							<li>Inspect the drawing and the Output.</li>
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
										near the top of the web page and select <b>
										Allow Blocked Content</b>.</li>
									</ol>
								</blockquote></div>
                         	<hr />
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3" width="575" style="width: 650px">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style4">
                                        &nbsp;File to embed:
										<input id="File1" type="text" name="T1" size="99"></td>
                                </tr>
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Run Macro" onclick="runMacro()" />

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

---
title: "Get DimensionStyle Names and Options Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_DimensionStyle_Names_and_Options_Example_JS.htm"
---

# Get DimensionStyle Names and Options Example (JS)

## Get DimensionStyle Names and Options Example (JavaScript)

| This example shows how to get the names and options of the DimensionStyles in the document and how to export the current view of the drawing to a PNG file. Start DraftSight. Click Get DimensionStyles . Examine the Output window. Navigate to C:\ProgramFiles\Dassault Systemes\DraftSight\Examples to verify that the drawing document was exported to B-44563.PNG. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,DimensionStyles">
<meta name=MS-HKWD content="JavaScript examples,angular Dimensions">
<meta name=MS-HKWD content="JavaScript examples,dual Dimensions">
<meta name=MS-HKWD content="JavaScript examples,fit Dimensions">
<meta name=MS-HKWD content="JavaScript examples,linear Dimensions">
<meta name=MS-HKWD content="JavaScript examples,tolerance Dimensions">
<meta name=MS-HKWD content="JavaScript examples,export feature">

    <head>

    <!-- Without this line, this does not work in Internet Explorer 8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=8" />

    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

    <!-- Add your dsInterface .js Files here -->
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleManager.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocumentExporter.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleAngularDimensionOptions.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleDualDimensionOptions.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleFitOptions.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleLinearDimensionOptions.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDimensionStyleToleranceOptions.js"></script>

    <!-- This is the main block where you place the JavaScript API code -->
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

        function PrintDimensionStyleOptions(dsDimStyle) {
        	//Angular DimensionStyle options
        	var dsDimStyleAngularDimOptions  = dsDimStyle.GetDimensionStyleAngularDimensionOptions();
    		printOut("  Angular DimensionStyle options:  \n");
    		printOut("    Precision: " + dsDimStyleAngularDimOptions.get_Precision() + "\n");
    		printOut("    Format: " + dsDimStyleAngularDimOptions.get_Format() + "\n");
    		printOut("    Hide leading zeroes: " + dsDimStyleAngularDimOptions.get_HideLeadingZeroes() + "\n");
    		printOut("    Hide trailing zeroes: " + dsDimStyleAngularDimOptions.get_HideTrailingZeroes() + "\n");

    		//Dual DimensionStyle options
        	var dsDimStyleDualDimOptions  = dsDimStyle.GetDimensionStyleDualDimensionOptions();
    		printOut("  Dual DimensionStyle options:  \n");
    		printOut("    Precision: " + dsDimStyleDualDimOptions  .get_Precision() + "\n");
    		printOut("    Format: " + dsDimStyleDualDimOptions  .get_Format() + "\n");
    		printOut("    Hide leading zeroes: " + dsDimStyleDualDimOptions  .get_HideLeadingZeroes() + "\n");
    		printOut("    Hide trailing zeroes: " + dsDimStyleDualDimOptions  .get_HideTrailingZeroes() + "\n");

    		//Fit DimensionStyle options
        	var dsDimStyleFitOptions  = dsDimStyle.GetDimensionStyleFitOptions();
    		printOut("  Fit DimensionStyle options:  \n");
    		printOut("    Placement of text: " + dsDimStyleFitOptions.get_FitDimensionText() + "\n");
    		printOut("    Entity to move outside Dimension's extension lines: " + dsDimStyleFitOptions.get_FitGeometry() + "\n");
    		printOut("    Hide arrows: " + dsDimStyleFitOptions.get_HideArrows() + "\n");
    		var scales = dsDimStyleFitOptions.GetDimensionScale();
    		printOut("    Scale factor: " + scales.ScaleFactor + "\n");

    		//Linear DimensionStyle options
        	var dsDimStyleLinearDimOptions  = dsDimStyle.GetDimensionStyleLinearDimensionOptions();
    		printOut("  Linear DimensionStyle options:  \n");
    		printOut("    Precision: " + dsDimStyleLinearDimOptions.get_Precision() + "\n");
    		printOut("    Format: " + dsDimStyleLinearDimOptions.get_Format() + "\n");
    		printOut("    Hide leading zeroes: " + dsDimStyleLinearDimOptions.get_HideLeadingZeroes() + "\n");
    		printOut("    Hide trailing zeroes: " + dsDimStyleLinearDimOptions.get_HideTrailingZeroes() + "\n");

        	//Tolerance DimensionStyle options
        	var dsDimStyleToleranceOptions  = dsDimStyle.GetDimensionStyleToleranceOptions();
    		printOut("  Tolerance DimensionStyle options:  \n");
    		printOut("    Precision: " + dsDimStyleToleranceOptions.get_Precision() + "\n");
    		printOut("    Minimum value: " + dsDimStyleToleranceOptions.get_MinimumValue() + "\n");
    		printOut("    Maximum value: " + dsDimStyleToleranceOptions.get_MaximumValue() + "\n");
    		printOut("    Hide leading zeroes: " + dsDimStyleToleranceOptions.get_HideLeadingZeroes() + "\n");
    		printOut("    Hide trailing zeroes: " + dsDimStyleToleranceOptions.get_HideTrailingZeroes() + "\n");

		}

        function apiCode() {
            var mScript = new djScriptManager();
            var mApp = mScript.getApplication();
            // Abort any command currently running in DraftSight to avoid nested commands
            mApp.AbortRunningCommand();

            // Open document
            var mDoc = mApp.OpenDocument2("C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.DWG", "dsDocumentOpen_Default", "dsEncoding_Default");

			if (mDoc == null){
				printOut("Specified document was not opened. Please check the path and file name.")

			}else{

                //Get the document's DimensionStyles
				var dsDimStyleMgr = mDoc.GetDimensionStyleManager();
				var dsDimStyles = dsDimStyleMgr.GetDimensionStyles();

				for (var i in dsDimStyles){
					var dsDimStyle = dsDimStyles[i]
					var dimStyleName = dsDimStyle.get_Name();
					printOut(dimStyleName + "\n");

					//Print each DimensionStyle's options to Output
					PrintDimensionStyleOptions(dsDimStyle);
				}

                //Export the document as PNG file
                var exportDoc = mDoc.GetDocumentExporter();
                var status = exportDoc.ExportToPng("C:\\ProgramData\\Dassault Systemes\\DraftSight\\Examples\\B-44563.PNG");

                if (status){
                	printOut("Drawing successfully exported to PNG file.");

                }else{

                	printOut("Export of drwing to PNG failed!");
                }

			}

            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Get DimensionStyle Names and Options Example (JS)</title>

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
    </style>

    </head>

    <H1>Get DimensionStyle Names and Options Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							<font style="font-size: 8pt">This example shows how
							to </font><span style="font-size: 8pt">get the names
							and options of the DimensionStyles in the document
							and how to export the current view of the drawing to
							a PNG file.</span><ol>
                            <li>Start DraftSight.<li>Click <b>Get</b> <b>
							DimensionStyles</b>.<li>Examine the Output window.<li>
							Navigate to <b>C:\ProgramFiles\Dassault Systemes\DraftSight\Examples</b>
							to verify that the drawing document was <br>
							exported to
							<b>B-44563.PNG.</b></ol>
								<p><b>NOTES:</b></p>
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
                            <table class="style3">
                                <!-- Reuse this row to add more rows-->
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style6">
                                        <input id="Button1" type="button" value="Get DimensionStyles" onclick="runMacro()" />

                                    </td>
                                </tr>
                            </table>
                            <div class="style19">
                                <h3 class="style20">
                                    Output</h3>
                            <textarea id="OB" cols="100" name="Output" rows="10" readonly="readonly"></textarea>
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

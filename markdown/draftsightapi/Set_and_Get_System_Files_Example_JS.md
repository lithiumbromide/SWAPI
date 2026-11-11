---
title: "Set and Get System Files Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_System_Files_Example_JS.htm"
---

# Set and Get System Files Example (JS)

## Set and Get System Files Example (JavaScript)

| This example shows how to set some DraftSight system paths. Start DraftSight. In the following form, type the path to: Font files in Font path . Add-in applications, area Hatch patterns, customization files, etc. in Support path . Click Set . Examine Output to see the current DraftSight system files and paths. NOTES: Errors are also printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer, and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,system files">

<head>

	<!-- Without this line, this does not work in Internet Explorer 8 -->
	<meta http-equiv="X-UA-Compatible" content="IE=8" />

	<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

	<!-- Add your dsInterface .js Files here -->
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
	<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSystemFiles.js"></script>

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
			    var mSystemFiles = mApp.GetSystemFiles();

			    mApp.AbortRunningCommand();

			    //Set font path
			    var setFontArray = new Array();
			    setFontArray[0] = document.getElementById("A").value;
			    mSystemFiles.put_FontsPaths(setFontArray);

			    //Get font paths
			    var getFontArray = new Array();
			    getFontArray = mSystemFiles.get_FontsPaths();

			    //Set support path
			    var setSupportArray = new Array();
			    setSupportArray[0] = document.getElementById("B").value;
			    mSystemFiles.put_SupportPaths(setSupportArray);

			    //Get support paths
			    var getSupportArray = new Array();
			    getSupportArray = mSystemFiles.get_SupportPaths();

			    //Get drawing border paths
			    var getDrawingBorderPathsArray= new Array();
			    getDrawingBorderPathsArray= mSystemFiles.get_DrawingBorderPaths();

				//Get title block paths
			    var getTitleBlockPathsArray= new Array();
			    getTitleBlockPathsArray= mSystemFiles.get_TitleBlockPaths();

                //Print out system files
 	            printOut("System files:\n");
 	            printOut("  Custom dictionary file:                 " + mSystemFiles.get_CustomDictionaryFile() + "\n");
 	            printOut("  Dictionary file for SpellCheck:         " + mSystemFiles.get_MainDictionaryFile() + "\n");
 	            printOut("  Help file:                              " + mSystemFiles.get_HelpFile() + "\n");
 	            printOut("  Log file:                               " + mSystemFiles.get_LogFilePath() + "\n");
 	            printOut("  Location for temporary drawing files:   " + mSystemFiles.get_TempPath() + "\n");

 	            printOut("   Font paths:" + "\n");
                for(var i = 0; i < getFontArray.length; i++){
			        var arrElement = getFontArray[i];
			        printOut("      " + JSON.stringify(arrElement)+ "\n");
			    }

				printOut("   Support paths:" + "\n");
			    for(var i = 0; i < getSupportArray.length; i++){
			        var arrElement = getSupportArray[i];
			        printOut("      " + JSON.stringify(arrElement)+ "\n");
			    }

			    printOut("   Drawing border paths:" + "\n");
			    for(var i = 0; i < getDrawingBorderPathsArray.length; i++){
			        var arrElement = getDrawingBorderPathsArray[0];
			        printOut("      " + JSON.stringify(arrElement)+ "\n");
			    }

				printOut("   Title block paths:" + "\n");
			    for(var i = 0; i < getTitleBlockPathsArray.length; i++){
			        var arrElement = getTitleBlockPathsArray[0];
			        printOut("      " + JSON.stringify(arrElement)+ "\n");
			    }

			    mApp.releaseAll();
			}

</script>

    <!-- Change the title so that it shows what the API is going to be used for -->
    <title>Set and Get System Files Example (JS)</title>

    <!-- This style formats the heading -->
    <style type="text/css">
     H1 {
	border-top:1px none ##ccccff; border-bottom:1px solid #808080; font-weight: bold;
	font-size: 10pt;
	font-family: Verdana, sans-serif;
	/*border-left-style: Inset;*/
	/*border-right-style: Inset;*/
	/*border-bottom-style: none;*/
	padding-top: 4pt;
	padding-bottom: 4pt;
	border-left-color: ##ccccff;
	border-right-color: ##ccccff;
	/*border-bottom-color: ##ccccff;*/
	margin-top: -15pt;
	text-indent: .15in;
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

    <H1>Set and Get System Files Example (JavaScript)</H1>

       <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
							This example shows how to set some DraftSight system
							paths.
							<ol>
                            <li>Start DraftSight.<li>
							In the following form, type the path to:<ol type="a">
								<li>Font files in <b>Font path</b>.</li>
								<li>Add-in applications, area Hatch patterns,
								customization files, etc. in <b>Support path</b>.</li>
							</ol>
							</li>
							<li>Click <b>Set</b>.</li>
							<li>Examine <b>Output</b> to see the current DraftSight system files
							and paths.</li>
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
										<li>If using Windows
										Internet Explorer, and running scripts is
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
                                    <td class="style20" width="306">
									<b>Font path: </b>
									<input type="text" name="App" id="A" value="" size="50" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="306">
                                    <b>Support path:</b>
									<input type="text" name="App" id="B" value="" size="50" /></td>
                                </tr>

                                <tr>
									<td class="style6">
									<button id="Button1" type="button" value="Set" onclick="runMacro()">								Set</button></td>
								</tr>

                            </table>

                            <div class="style19">
                                <h3 class="style20">
                                	Output</h3>
                            			<textarea id="OB" cols="150" name="Output" rows="10" readonly="readonly"></textarea>
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

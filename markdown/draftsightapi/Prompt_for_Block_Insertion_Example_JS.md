---
title: "Prompt for Block Insertion Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Prompt_for_Block_Insertion_Example_JS.htm"
---

# Prompt for Block Insertion Example (JS)

## Prompt for Block Insertion Example (JavaScript)

| This example shows how to prompt a user for the insertion point and scale factors when inserting a Block instance. To insert a Block instance: Start DraftSight and open a drawing. To use the default values shown in the form: Click Insert Block . Click in the graphics area where you want to insert the Block Instance. Press the Enter key at each prompt in the command window, which indicates to use the default value. To change the default values shown in the form, type a value for the default: X scale factor in Default X Scale . Y scale factor in Default Y Scale . Z scale factor in Default Z Scale . Click Insert Block . Click in the graphics area where you want to insert the Block instance. Press the Enter key at each prompt in the command window, which indicates to use the default value. To specify your own values: Click Insert Block on the form. Click in the graphics area to set the Block instance's insertion point. Move the pointer and click in the graphics area again to set the Block instance's scale factors. - or - Type a value for the X, Y, and Z scale factors when prompted at the command window. Examine the drawing. NOTES: Errors and the Block instance's scale factors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, allow blocked content. |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples, Block instances">
<meta name=MS-HKWD content="JavaScript examples, Block definitions">
<meta name=MS-HKWD content="JavaScript examples, Circles">

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
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCommandMessage.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockDefinition.js"></script>
    <script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsBlockInstance.js"></script>

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

            var mDoc = mApp.GetActiveDocument();
            var mModel = mDoc.GetModel();
            var mSkMgr = mModel.GetSketchManager();

    		var X = 0;
    		var Y = 0;
    		var Z = 0;
    		var R1 = 10;
			var R2 = 15;

    		var mCircle1 = mSkMgr.InsertCircle(X, Y, Z, R1);
			var mCircle2 = mSkMgr.InsertCircle(X, Y, Z, R2);

			var longarray = new Array();
		    var entityarray = new Array();
			longarray[0] = 22;
		    longarray[1] = 22;
			entityarray[0] = mCircle1;
		    entityarray[1] = mCircle2;

			mDoc.CreateBlockDefinition("TestBlock", "Test Block", X, Y, Z, longarray, entityarray, "dsBlockDefinitionEntities_RemoveFromDrawing");

			var ScaleX = parseFloat(document.getElementById("X").value);
 		    var ScaleY = parseFloat(document.getElementById("Y").value);
		    var ScaleZ = parseFloat(document.getElementById("Z").value);

 		    <!-- var Rotation = parseFloat(document.getElementById("R").value); -->
 		    var Rotation = 0;

			var mCmdMsg = mApp.GetCommandMessage();
			var params = mCmdMsg.PromptForBlockInsertion("TestBlock", true, ScaleX, ScaleY, ScaleZ, false, Rotation);

			var PosX = params.X;
			var PosY = params.Y;
			var PosZ = params.Z;
			ScaleX = params.ScaleX;
			ScaleY = params.ScaleY;
			ScaleZ = params.ScaleZ;
			Rotation = params.Rotation;

			mSkMgr.InsertBlock2("TestBlock", PosX, PosY, PosZ, ScaleX, ScaleY, ScaleZ, Rotation);

            printOut("X scale factor: " + ScaleX + "\n");
            printOut("Y scale factor: " + ScaleY + "\n");
            printOut("Z scale factor: " + ScaleZ + "\n");

            //Type your JavaScript API code here
            mApp.releaseAll();
        }
    </script>

    <!-- Change the title so that it describes what the example demonstrates -->
    <title>Prompt for Block Insertion Example (JS)</title>

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

    <H1>Prompt for Block Insertion Example (JavaScript)</H1>

    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 55px">
                        <div class="style7">
                            This example shows how to prompt a user for the
							insertion point and scale factors
							when inserting a Block instance.<p>To insert a Block
							instance:</p>
							<ol>
                            <li>Start DraftSight and open a drawing.<li>To use the default values shown in the form:<ol>
                            <li>Click <b>Insert Block</b>.</li>
							<li>Click in the graphics area where you want to
							insert the Block Instance.</li>
							<li>Press the Enter key at each prompt in the
							command window, which indicates to use the default
							value.</li>
                            </ol>
							<li>To change the default values shown in the form,
							type a value for the default:<ol>
								<li>X scale factor in <b>Default X Scale</b>.</li>
								<li>Y scale factor in <b>Default Y</b> <b>Scale</b>.</li>
								<li>Z scale factor in <b>Default Z Scale</b>.</li>
								<li>Click <b>Insert Block</b>.</li>
								<li>Click in the graphics area where you want to
							insert the Block instance.</li>
								<li>Press the Enter key at each prompt in the command window, which indicates to use the default value.</li>
							</ol>
							<li>To specify your own values:<ol>
                            <li>Click <b>Insert Block</b> on the form.</li>
							<li>Click in the graphics area to set the Block
							instance's insertion point.</li>
							<li>Move the pointer and click in the graphics area again to set the
							Block instance's scale factors.<br>
							- or -<br>
							Type a value for the X, Y, and Z scale factors when
							prompted at the command window.</li>
                            </ol></li>
							<li>Examine the drawing.</li>
                            </ol>
							<p><b>NOTES:</b></p>
								<ul>
									<li>Errors and the Block instance's scale
									factors are printed to
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
                    <td class="style2">
                        <form name="inputform">
                            <table class="style3">
                                  <tr>
                                    <td class="style4" colspan="2">
                                        Default X Scale:&nbsp;&nbsp;&nbsp;&nbsp;<input id="X" type="text" value="1.0" name="ScaleX"class="style22" />                                    </td>
                                  </tr>
                                  <tr>
                                    <td class="style4" colspan="2">
                                        Default Y Scale:&nbsp;&nbsp;&nbsp;&nbsp;<input id="Y" type="text" value="1.0" name="ScaleY" class="style22" />                                    </td>
                                  </tr>
                                  <tr>
                                    <td class="style4" colspan="2">
                                        Default Z Scale:&nbsp;&nbsp;&nbsp;&nbsp;<input id="Z" type="text" value="1.0" name="ScaleZ" class="style22" />                                    </td>
                                 </tr>
                                 <!-- <tr>
                                    <td class="style4" colspan="2">
                                        Default Rotation:&nbsp;<input id="R" type="text" value="15.0" name="Rotation" class="style22" />
                                    </td> -->
                                </tr>
                                </tr>

                                <tr>
                                    <td colspan="2" class="style6">
                                        <input type="button" value="Insert Block" onclick="runMacro()" /><br />

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

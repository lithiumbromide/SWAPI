---
title: "Create Circular Pattern Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Circular_Pattern_Example_JS.htm"
---

# Create Circular Pattern Example (JS)

## Create Circular Pattern Example (JavaScript)

| This example creates a circular pattern of Circles in a DraftSight drawing. Start DraftSight. Using the following form, specify the parameters for the circular pattern: Type the angle between the base points of the pattern entities and the center of the pattern in Angle between pattern entities . This field is only valid if you selected Angle between and total number of elements or Fill angle and angle between elements for Pattern . Type a positive or negative value for Fill angle . The default for the angle to fill is 360° - a full circle pattern. A value of 0 is not allowed. The pattern is drawn counterclockwise for positive angles and clockwise for negative angles. This field is only valid if you selected Fill angle and angle between elements or Fill angle and total number of elements for Pattern . Type the total number of pattern entities, including the source entity in Number of pattern entities . Type the x coordinate of the base point of the pattern in Base point x . Type the y coordinate of the base point of the pattern in Base point y . Type the x coordinate of the center point of the pattern in Axis point x . Type the y coordinate of the center point of the pattern in Axis point y . Select Pattern entities about axis to rotate the entities as they are patterned, or leave this check box clear to align the entities to the source entity. Click Insert . Examine the drawing. NOTES: Errors are printed to Output. To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. If using Windows Internet Explorer and running scripts is blocked, click the Information bar near the top of the webpage and select Allow Blocked Content . |
| --- |
|  |

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<meta name=MS-HKWD content="JavaScript examples">
<meta name=MS-HKWD content="JavaScript examples,documents">
<meta name=MS-HKWD content="JavaScript examples,application">
<meta name=MS-HKWD content="JavaScript examples,Sketch Manager">
<meta name=MS-HKWD content="JavaScript examples,circular patterns">
<meta name=MS-HKWD content="JavaScript examples,Circles">

<head>
<!-- Without this line, this does not work in Internet Explorer 8 -->
<meta http-equiv="X-UA-Compatible" content="IE=8" />

<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type" />

<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>
<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>
<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsDocument.js"></script>
<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsModel.js"></script>
<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsSketchManager.js"></script>
<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsCircle.js"></script>

<!-- This is the main block where you place the JavaScript API code -->
<script type="text/javascript">

function printOut(str) {}

function loadArray() {

	var mScript = new djScriptManager();
	var mApp = mScript.getApplication();
	// abort any command currently running in DraftSight to avoid nested commands
	mApp.AbortRunningCommand();
	var mDoc = mApp.GetActiveDocument();
	var mModel = mDoc.GetModel();
	var mSkMgr = mModel.GetSketchManager();
	var EN = document.getElementById("EN").value;
	var AB = parseFloat(document.getElementById("AB").value);
	var FA = parseFloat(document.getElementById("FA").value);
	var TN = parseFloat(document.getElementById("TN").value);
	var EX = parseFloat(document.getElementById("EX").value);
	var EY = parseFloat(document.getElementById("EY").value);
	var AX = parseFloat(document.getElementById("AX").value);
	var AY = parseFloat(document.getElementById("AY").value);

	var longArray = new Array();
	longArray[0] = 22;
	longArray[1] = 22;
	longArray[2] = 22;

	//Figure out a way to implement the long array and entity array
	var entityArray = new Array();
	entityArray[0] = mSkMgr.InsertCircle(30, 30, 0, 10);
	entityArray[1] = mSkMgr.InsertCircle(60, 60, 0, 10);
	entityArray[2] = mSkMgr.InsertCircle(90, 90, 0, 10);

	var orient = true;

	var mPattern = mSkMgr.PatternCircular(EN, AB, FA, TN, EX, EY, AX, AY, orient, longArray, entityArray);

    var lowerLeftArray = [0,0,0]
    var upperRightArray = [0,0,0]
    mApp.Zoom("dsZoomRange_Fit", lowerLeftArray, upperRightArray)
    mApp.releaseAll();

	mApp.releaseAll();
}

</script>

<!-- Change the title so that it shows what the API is going to be used for -->
<title>Create Circular Pattern Example (JS)</title>
    <!-- These styles are used to format the table cells -->
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
            color: #006600;
            font-weight: bold
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

    </style>
</head>

<h1>Create Circular Pattern Example (JavaScript)</h1>
    <body>
        <table style="text-align: left; width: 860px; height: 600px; font-family: Verdana, sans-serif;" border="0"
            cellpadding="0" cellspacing="0">

            <tbody>
                <tr>
                    <td style="height: 75px;">
                        <div class="style7">
							This example creates a circular pattern
							of Circles in a DraftSight drawing.<ol>
                            <li>Start DraftSight.
														<li>Using the following
														form, specify the
														parameters for the
														circular pattern:<ol>
															<li>Type the angle
															between the base
															points of the
															pattern entities and
															the center of the
															pattern in <b>Angle
															between pattern
															entities</b>. This
															field is only valid
															if you selected <b>
															Angle between and
															total number of elements </b>or&nbsp;<b>Fill
															angle and angle
															between elements</b> for <b>
															Pattern</b>.</li>
															<li>Type a positive
															or negative value
															for <b>Fill angle</b>. The default
															for the angle to
															fill is 360° - a
															full circle pattern.
															A value of 0 is
															not allowed. The
															pattern is drawn
															counterclockwise for
															positive angles and
															clockwise for
															negative angles.
															This field is only
															valid if you
															selected <b>Fill
															angle and angle</b>
															<b>between</b> <b>
															elements</b> or <b>Fill
															angle and total
															number of elements </b>for <b>
															Pattern</b>.</li>
															<li>Type the total
															number of pattern
															entities, including
															the source entity in
															<b>Number of pattern
															entities</b>.</li>
															<li>Type the x
															coordinate of the
															base point of the
															pattern in <b>Base
															point x</b>.</li>
															<li>Type the y
															coordinate of the
															base point of the
															pattern in <b>Base
															point y</b>.</li>
															<li>Type the x
															coordinate of the
															center point of the
															pattern in <b>Axis
															point x</b>.</li>
															<li>Type the y
															coordinate of the
															center point of the
															pattern in <b>Axis
															point y</b>.</li>
															<li>Select<b>
															Pattern entities
															about axis </b>to
															rotate the entities
															as they are
															patterned, or leave
															this check box clear
															to align the
															entities to the
															source entity.</li>
															<li>Click <b>Insert</b>.</li>
														</ol>
                            <li>Examine the drawing.</li>
                            </ol>
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
                            <table class="style3" width="500" style="width: 700px">
                                <!-- Reuse this row to add more rows-->
                                <tr>
                                    <!-- Use these two cells to implement inputs, add more rows if necessarily-->
                                    <td class="style20" width="426">
                                        Pattern:</td>
                                    <td class="style20" width="264">
                                        <select name="enum" id="EN">
                                        <option value="dsBasePatternOn_AngleBetweenAndElementsNumber">Angle between and total number of elements</option>
										<option value="dsBasePatternOn_FillAngleAndAngleBetween">Fill angle and angle between elements</option>
										<option value="dsBasePatternOn_FillAngleAndElementsNumber">Fill angle and total number of elements</option>
										</select><br />
									</td>
                                </tr>
                                <!-- End of the input row -->
                                <tr>
                                    <td class="style20" width="426">
                                        Angle between pattern entities (in radians):
                                        <br /></td>
                                    <td class="style20"  width="264">
                                        <input type="text" name="AngleBetween" id="AB" value="1.5707963" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Fill angle (in radians):</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="FillAngle" id="FA" value=" 4.71238898 " /><br /></td>
                                        </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Number of pattern entities:</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="TotalNumber" id="TN" value="4" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Base point x:</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="ElementX" id="EX" value="0" /> </td>

                                </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Base point y:</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="ElementY" id="EY" value="0" /></td>

                                </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Axis point x:</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="AxisX" id="AX" value="0" /></td>
                                </tr>
                                <tr>
                                    <td class="style20" width="426">
                                        Axis point y:</td>
                                    <td class="style20" width="264">
                                        <input type="text" name="AxisY" id="AY" value="0" /></td>
                                </tr>

                                <tr>
                                    <td class="style20" width="426">
                                        &nbsp;</td>
                                    <td class="style20" width="264">
                                        &nbsp;</td>
                                </tr>

                                <tr>
                                    <td colspan="2" class="style6">
                                        <button type="button" onclick="loadArray()">Insert</button></td>
                                </tr>
                            </table>
                            <div class="style19">
                                <h3 class="style20">
                                    Output</h3>
                            		<textarea id="OB" cols="50" name="Output" rows="10" readonly="readonly"></textarea>								<hr />
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

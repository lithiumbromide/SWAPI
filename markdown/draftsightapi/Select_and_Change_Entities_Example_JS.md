---
title: "Select and Change Entities Example (JS)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Select_and_Change_Entities_Example_JS.htm"
---

# Select and Change Entities Example (JS)

## Select and Change Entities Example (JavaScript)

| This example shows how to: construct several Splines, which are displayed as the Dassault Systèmes logo in a DraftSight drawing. select the Splines as a group of entities and modify the color of one member of that group of entities. Start DraftSight. Using the following form, click Create logo and watch the lower-left corner of the drawing. The Dassault Systèmes logo is created at the origin. The letter D changes from blue to yellow. NOTE: To recreate this example: Right-click the topic and select to view the source. Save the file as an HTML file. Open the HTML file in your web browser. Start DraftSight. If using Windows Internet Explorer: Click the Information bar near the top of the webpage, select Allow Blocked Content if running scripts is blocked, and click Yes . To more easily examine the logo before and after changing the color of the letter D in the logo: Press F12 to open the Windows Internet Explorer Developer Tools. Select the Script tab. Locate and click var mSelectionManager = mDoc.GetSelectionManager(); to insert a breakpoint at that line. Click Start Debugging . Click OK to refresh the webpage. Click Create logo in the form in the webpage. Examine the logo in the drawing. The letter D is blue, the letter S is yellow, and the non-letter is red. Click Stop Debugging in Windows Internet Explorer Developer Tools. Examine the logo in the drawing. The letter D changed from blue to yellow. Click File > Exit to close Windows Internet Explorer Developer Tools. If using a web browser other than Windows Internet Explorer, click Create logo . |
| --- |
|  |

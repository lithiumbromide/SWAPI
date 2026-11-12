---
title: "Change Labels of SOLIDWORKS Triad Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Labels_of_SOLIDWORKS_Triad_Example_VB.htm"
---

# Change Labels of SOLIDWORKS Triad Example (VBA)

This example shows how to change the labels of the SOLIDWORKS triad.

```vb
'---------------------------------------
'
' Preconditions: SOLIDWORKS Design model document is open.
'
' Postconditions: The labels of the triad are
'                 changed and then changed back to
'                 their original values.
'
'---------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim rVal As String

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    rVal = swApp.SetUserPreferenceStringValue(swReferenceTriadXLabel, "AltX")
    If rVal = False Then swApp.SendMsgToUser ("ERROR: Unable to change triad label.")

    rVal = swApp.SetUserPreferenceStringValue(swReferenceTriadYLabel, "AltY")
    If rVal = False Then swApp.SendMsgToUser ("ERROR: Unable to change triad label.")

    rVal = swApp.SetUserPreferenceStringValue(swReferenceTriadZLabel, "AltZ")
    If rVal = False Then swApp.SendMsgToUser ("ERROR: Unable to change triad label.")

    swApp.SetUserPreferenceToggle swReferenceTriadUseAlternateLabels, True
    swModel.GraphicsRedraw2
    Stop 'Labels are changed

    swApp.SetUserPreferenceToggle swReferenceTriadUseAlternateLabels, False
    swModel.GraphicsRedraw2
    'Stop 'Labels are changed back to original

End Sub
```

---
title: "Update Weldment Cut List and Fire Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VB.htm"
---

# Update Weldment Cut List and Fire Post-Notify Event Example (VBA)

This example shows how to handle the post-notification event that fires

when the weldment cut list is updated.

```vb
'------------------------------------------------------
' Preconditions:
' 1. Create main module with Main module code.
' 2. Insert Class1 module with Class1 module code.
' 3. Specified file to open exists.
' 4. Run macro (F5).
'
' Postconditions:
' 1. Right-click on the Cut list folder.
' 2. Select Update from the right-click menu.
' 3. A message box displays.
' 4. Click OK.
' 5. Stop the macro.
'--------------------------------------------------------------------------
' Main module
'--------------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim swPartEvents As Class1
Dim swPart As SldWorks.PartDoc
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt")
    swDocSpecification.InteractiveComponentSelection = True
    swDocSpecification.DocumentType = swDocPART
    Set swModel = swApp.OpenDoc7(swDocSpecification)

    Set swModel = swApp.ActiveDoc
    Set swPart = swModel

    ' Set up event

    Set swPartEvents = New Class1
    Set swPartEvents.swPart = swPart
End Sub

'--------------------------------------------------------------------------
' Class1 module
'--------------------------------------------------------------------------
Public WithEvents swPart As SldWorks.PartDoc
Private Function swPart_WeldmentCutListUpdatePostNotify() As Long
    MsgBox "The cut list is updated."
End Function
```

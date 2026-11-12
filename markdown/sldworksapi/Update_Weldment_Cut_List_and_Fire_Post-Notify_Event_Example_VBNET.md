---
title: "Update Weldment Cut List and Fire Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VBNET.htm"
---

# Update Weldment Cut List and Fire Post-Notify Event Example (VB.NET)

This example shows how to handle the post-notification event that fires

when the weldment cut list is updated.

```vb
'------------------------------------------------------
' Preconditions: Specified file to open exists.
'
' Postconditions:
' 1. Right-click on the Cut list folder.
' 2. Select Update from the right-click menu.
' 3. A message box displays (look in the taskbar for the hidden dialog).
' 4. Click OK.
' 5. Stop the macro.
'------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro
    Public WithEvents swPart As PartDoc
    Public Sub main()
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
        Dim swModel As ModelDoc2
        Dim swDocSpecification As DocumentSpecification
        swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt")
        swDocSpecification.DocumentType = swDocumentTypes_e.swDocPART
        swModel = swApp.OpenDoc7(swDocSpecification)
        swModel = swApp.ActiveDoc
        swPart = swModel
        ' Set up event
        AttachEventHandlers()
    End Sub
    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub
    Sub AttachSWEvents()
        AddHandler swPart.WeldmentCutListUpdatePostNotify, AddressOf Me.swPart_WeldmentCutListUpdatePostNotify
    End Sub
    Public Function swPart_WeldmentCutListUpdatePostNotify() As Integer
        MsgBox("The cut list is updated.")
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, True)
    End Function
    Public swApp As SldWorks
End Class
```

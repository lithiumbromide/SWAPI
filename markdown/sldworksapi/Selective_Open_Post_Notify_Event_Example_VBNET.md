---
title: "Selective Open Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selective_Open_Post_Notify_Event_Example_VBNET.htm"
---

# Selective Open Post-Notify Event Example (VB.NET)

This example shows how to handle the post-notification event that fires when components are selected for Quick View/Selective Open.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. If the Large Design Review dialog displays,
'    then click OK to close it.
' 2. When prompted, select the components to open
'    and click Open Selected.
' 3. Click OK to close the message box.
' 4. If prompted to rebuild, then click Rebuild.
' 5. After reading the next message box displayed,
'    click OK to close it.
' 6. Displays only the selected components.
' 7. Inspect the Immediate Window and graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'--------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro
    Public WithEvents swAssembly As AssemblyDoc
    Public Sub main()
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)
        Dim swModel As ModelDoc2
        Dim swDocSpecification As DocumentSpecification
        swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm")
        swDocSpecification.InteractiveComponentSelection = True
        swDocSpecification.DocumentType = swDocumentTypes_e.swDocASSEMBLY
        swModel = swApp.OpenDoc7(swDocSpecification)
        swModel = swApp.ActiveDoc
        swAssembly = swModel
        ' Set up event
        AttachEventHandlers()

    End Sub
    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub
    Sub AttachSWEvents()
        AddHandler swAssembly.SelectiveOpenPostNotify, AddressOf Me.swAssembly_SelectiveOpenPostNotify
    End Sub
    Public Function swAssembly_SelectiveOpenPostNotify(ByVal NewAddedDisplayStateName As String, ByRef SelectedComponentNames As Object) As Integer
        MsgBox("A post-notification event has been fired for the selective open.")
        System.Diagnostics.Debug.Print("New display state name: " & NewAddedDisplayStateName)
        System.Diagnostics.Debug.Print("Selected component names:")
        Dim i As Long
        For i = 0 To UBound(SelectedComponentNames)
            System.Diagnostics.Debug.Print("  " & SelectedComponentNames(i))
        Next
        swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, True)
    End Function
    Public swApp As SldWorks
End Class
```

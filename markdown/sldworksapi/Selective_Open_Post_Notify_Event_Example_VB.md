---
title: "Selective Open Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selective_Open_Post_Notify_Event_Example_VB.htm"
---

# Selective Open Post-Notify Event Example (VBA)

This example shows how to handle the post-notification event that fires when components are selected for Quick View/Selective Open.

```
'------------------------------------------------------
' Preconditions:
' 1. Copy Main into the macro.
' 2. Click Insert > Class Module and copy Class1
'    into that module.
' 3. Verify that the specified assembly to open
'    exists.
' 4. Open the Immediate window.
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
'Main
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim swAssemblyEvents As Class1
Dim swAssembly As SldWorks.AssemblyDoc
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm")
    swDocSpecification.InteractiveComponentSelection = True
    swDocSpecification.DocumentType = swDocASSEMBLY
    Set swModel = swApp.OpenDoc7(swDocSpecification)

    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel

    ' Set up event

    Set swAssemblyEvents = New Class1
    Set swAssemblyEvents.swAssembly = swAssembly
End Sub
Back to top

'Class1

Public WithEvents swAssembly As SldWorks.AssemblyDoc
Private Function swAssembly_SelectiveOpenPostNotify(ByVal NewAddedDisplayStateName As String, SelectedComponentNames As Variant) As Long
    MsgBox "A post-notification event has been fired for the selective open."
    Debug.Print "New display state name: " & NewAddedDisplayStateName
    Debug.Print "Selected component names:"
    Dim i As Long
    For i = 0 To UBound(SelectedComponentNames)
        Debug.Print "  " & SelectedComponentNames(i)
    Next
End Function
Back to top
```

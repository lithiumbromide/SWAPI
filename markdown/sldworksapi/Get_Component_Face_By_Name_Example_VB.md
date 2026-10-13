---
title: "Select Component Face By Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_Face_By_Name_Example_VB.htm"
---

# Select Component Face By Name Example (VBA)

This example shows how to find and select a face using its name.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\appearances\usb_flash_drive2.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects a component.
' 2. Selects a face on that component and names it.
' 3. Traverses the component's body and gets each face
'    on that body.
' 4. When the selected face matching the named face is found,
'    prints the selected face's name to the Immediate window.
' 5. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModel As SldWorks.ModelDoc2
Dim swComp As SldWorks.Component2
Dim swFace As SldWorks.Face2
Dim boolstatus As Long
```

```
Public Sub SelectComponentFaceByName(faceName As String)
```

```
    Dim swBody As SldWorks.Body2
    Dim swSelData As SldWorks.SelectData
    Dim currentFaceName As String
```

```
    Set swSelData = swSelMgr.CreateSelectData
```

```
    ' Get the component body
    Set swBody = swComp.GetBody()
    If (swBody Is Nothing) Then
        swApp.SendMsgToUser "Component body unavailable."
        swApp.SendMsgToUser "Make sure component is not lightweight or suppressed."
        Exit Sub
    End If
```

```
    Debug.Print "Traversing faces on component's body..."
```

```
    Set swFace = swBody.GetFirstFace
    Do While Not swFace Is Nothing
        currentFaceName = swModel.GetEntityName(swFace)
        If (currentFaceName = faceName) Then
            ' Select the face
            swFace.Select4 False, swSelData
            Debug.Print "  Name of currently selected face; should match name of previously selected face: " & currentFaceName
            Exit Do
        End If
    Set swFace = swFace.GetNextFace
Loop
```

```
' Subsequent code might select a second face,
' edge, or feature, and then mate the two
' items using AssemblyDoc::AddMate5
```

```
End Sub
```

```
Sub main()
```

```
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim componentName As String
    Dim faceName As String
```

```
   Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Get active assembly document
    Set swModel = swApp.ActiveDoc()
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Select a component and get its name
    boolstatus = swModelDocExt.SelectByID2("USB_connector_shell2-1@usb_flash_drive2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swComp = swSelMgr.GetSelectedObject6(1, -1)
    componentName = swComp.Name2
    Debug.Print "Name of selected component: " & componentName
```

```
    swModel.ClearSelection2 True
```

```
    ' Select a face on the component and
    ' name it
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -6.97433509299117E-03, 8.5197071911125E-04, 5.99999999997181E-03, False, 0, Nothing, 0)
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    boolstatus = swModel.SelectedFaceProperties(0, 0, 0, 0, 0, 0, 0, True, "SideFace")
    faceName = swModel.GetEntityName(swFace)
    Debug.Print "Name of selected face on selected component: " & faceName
```

```
    SelectComponentFaceByName faceName
```

```
End Sub
```

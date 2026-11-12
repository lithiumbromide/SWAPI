---
title: "Get Entity By Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Entity_By_Name_Example.htm"
---

# Get Entity By Name Example (VBA)

This example shows how to get a face by specifying its name and changing the name. This process is commonly used with standardized parts where names can be given to objects and the objects can be accessed later.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Select a face.
'
' Postconditions:
' 1. Displays a message box containing the
'    name of the selected face.
' 2. Click OK.
' 3. Displays a message box containing
'    the new name of the selected face.
' 4. Click OK.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.PartDoc
    Dim Face As SldWorks.Face2
    Dim Model As SldWorks.ModelDoc2
    Dim ModelDocExt As SldWorks.ModelDocExtension
    Dim SelMgr As SldWorks.SelectionMgr
    Dim Entity As SldWorks.Entity
    Dim faceName As String
    Dim ret As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Get active document
    Set Part = swApp.ActiveDoc
    Set Model = Part
```

```
    ' Get face name
    Set SelMgr = Model.SelectionManager
    Set Face = SelMgr.GetSelectedObject6(1, -1)
    Set Entity = Face
    faceName = Model.GetEntityName(Entity)
```

```
    swApp.SendMsgToUser "Selected face name: " & faceName
```

```
    ' Get face by its name
    Set Face = Part.GetEntityByName(faceName, 2)
```

```
    ' Delete current face name
    ret = Part.DeleteEntityName(Entity)
```

```
    ' Change name of the face
    ret = Part.SetEntityName(Entity, "NewFaceName")
```

```
    ' If name change is successful
    If ret Then
        swApp.SendMsgToUser "Selected face name changed to: " & Model.GetEntityName(Entity)
    ' If name change failed
    Else
        swApp.SendMsgToUser "Error changing face name."
    End If
```

```
End Sub
```

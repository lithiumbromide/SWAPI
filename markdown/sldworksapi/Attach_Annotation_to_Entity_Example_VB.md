---
title: "Attach Annotation to Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Annotation_to_Entity_Example_VB.htm"
---

# Attach Annotation to Entity Example (VBA)

This example shows how to attach an annotation to a different entity.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part or drawing that has at least one
'    annotation.
' 2. Select an annotation.
' 3. Press Ctrl while selecting a face, edge, or vertex.
'
' Postconditions:
' 1. Attaches the selected annotation to the entity
'    selected in Preconditions step 3, if possible.
' 2. Examine the annotation in the graphics area.
'
' NOTE: If you open a drawing:
' * uncomment the statement for a drawing.
' * comment out the statement for a part.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelObj1 As Object
    Dim swSelObj2 As Object
    Dim swAnn As SldWorks.Annotation
    Dim vAttEntTypeArr As Variant
    Dim vAttEntArr As Variant
    Dim nSelType As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    'Select the annotation to move
    Set swSelObj1 = swSelMgr.GetSelectedObject6(1, -1)
    Set swAnn = swSelObj1.GetAnnotation
```

```
    'Part - select the entity where to move the annotation
    Set swSelObj2 = swSelMgr.GetSelectedObject6(2, -1)
```

```
    'Drawing - select the entity where to to move the annotation
    'Set swSelObj2 = swSelMgr.GetSelectedObject6(3, -1)
```

```
    Dim AttEntArr(0) As Object
    Set AttEntArr(0) = swSelObj2
    Dim vAttEntArrIn As Variant
    vAttEntArrIn = AttEntArr
```

```
    bRet = swAnn.SetAttachedEntities(vAttEntArrIn)
```

```
    Debug.Print "Name = " & swAnn.GetName
    Debug.Print "  Selection Type = " & swSelMgr.GetSelectedObjectType3(1, -1)
    Debug.Print "  Annotation Type = " & swAnn.GetType
```

```
    vAttEntArr = swAnn.GetAttachedEntities3
    vAttEntTypeArr = swAnn.GetAttachedEntityTypes
```

```
    If Not IsEmpty(vAttEntTypeArr) Then
        Debug.Assert UBound(vAttEntArr) = UBound(vAttEntTypeArr)
        For i = 0 To UBound(vAttEntTypeArr)
            'A dangling dimension has at least one entity of type swSelNOTHING
            Debug.Print "  Entity Type(" & i & ") = " & vAttEntTypeArr(i)
            Dim swSelData As SldWorks.SelectData
            Set swSelData = swSelMgr.CreateSelectData
            Call vAttEntArr(i).Select4(False, swSelData)
        Next i
    End If
```

```
End Sub
```

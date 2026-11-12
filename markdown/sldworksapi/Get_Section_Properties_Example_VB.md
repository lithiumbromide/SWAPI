---
title: "Get Section Properties for Faces from Section Planes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Section_Properties_Example_VB.htm"
---

# Get Section Properties for Faces from Section Planes Example (VBA)

This example shows how to get the section properties of the selected items.

**NOTE**: Through the user interface, it is possible to extract the section properties from various combinations of selected entities. This is accessible through the SOLIDWORKS API with IModelDocExtension::GetSectionProperties. This method has only one input parameter, an array of entities to consider with the current selection set. The entity array must only contain these types of objects: Face2 and Sketch. For planar faces and reference surfaces, this is the Face2 object. A sketch corresponds to a Sketch object. However, for a face on a section plane, there is no API object. This sample code shows how to use this method to allow for faces obtained from section planes.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part, fully resolved assembly, or drawing.
' 2. Select one of the following:
'    * Sketch
'    * Planar model face
'    * Face on a section plane
'    * Crosshatch section face in a section view
'      in a drawing or a sketch
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Maintains the selection set. (See NOTES)
' 2. Examine the Immediate window.
'
' NOTES:
' * Array of objects passed into this method are
'   added to the selection set.
' * Outputted values are the same as those obtained
'   through the user interface.
' * Reasons for failures are the same as those
'   in the user interface.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
    Const PI As Double = 3.14159
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swFeat() As SldWorks.Feature
    Dim swFaceEnt() As SldWorks.Entity
    Dim swSketch As SldWorks.Sketch
    Dim nSelType As Long
    Dim swSelObj() As Object
    Dim vSelObj As Variant
    Dim vSectionProp As Variant
    Dim nSelCount As Long
    Dim nNumObj As Long
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount
    For i = 1 To nSelCount
        nSelType = swSelMgr.GetSelectedObjectType2(i)
        Debug.Print "  SelType(" & i & ") = " & nSelType
        Select Case nSelType
            Case swSelFACES, swSelREFSURFACES
                nNumObj = nNumObj + 1
                ReDim Preserve swSelObj(nNumObj - 1)
                ReDim Preserve swFaceEnt(nNumObj - 1)
                Set swFace = swSelMgr.GetSelectedObject5(i)
                Set swFaceEnt(nNumObj - 1) = swFace
                Set swSelObj(nNumObj - 1) = swFace
            Case swSelSKETCHES
                nNumObj = nNumObj + 1
                ReDim Preserve swSelObj(nNumObj - 1)
                ReDim Preserve swFeat(nNumObj - 1)
                Set swFeat(nNumObj - 1) = swSelMgr.GetSelectedObject5(i)
                Set swSketch = swFeat(nNumObj - 1).GetSpecificFeature
                Set swSelObj(nNumObj - 1) = swSketch
                Debug.Print "    " & swFeat(nNumObj - 1).Name
```

```
            Case swSelMANIPULATORS
                ' Section face in a part or assembly when in a section view
                ' There is no corresponding API object for this,
                ' so leave it selected
        End Select
    Next i
    Debug.Print ""
```

```
    ' Deselect faces and sketches; otherwise, user-interface selections
    ' are added to array parameter; leave section faces selected
    If Not IsEmpty(swFaceEnt) Then
        For i = 0 To UBound(swFaceEnt)
            swFaceEnt(i).DeSelect
        Next i
    End If
```

```
    If Not IsEmpty(swFeat) Then
        For i = 0 To UBound(swFeat)
            swFeat(i).DeSelect
        Next i
    End If
```

```
    vSelObj = swSelObj
```

```
    ' This adds the array of faces or sketches to the selection set
    ' Because the faces or sketches have been deselected, this
    ' preserves the selection set
    vSectionProp = swModelExt.GetSectionProperties((vSelObj))
```

```
    ' Return code from:
    '   IModelDocExtension::GetSectionProperties
    '       0 = success
    '       1 = invalid input
    '       2 = selected faces are not in the same or parallel planes
    '       3 = unable to compute section properties
    Debug.Print "  Return code              = " & vSectionProp(0)
    Debug.Print ""
    Debug.Print "  Area                     = " & vSectionProp(1) * 1000000# & " mm^2"
    Debug.Print "  Centroid                 = (" & vSectionProp(2) * 1000# & ", " & vSectionProp(3) * 1000# & ", " & vSectionProp(4) * 1000# & ") mm"
    Debug.Print "  Ixx                      = " & vSectionProp(5) * 1000000000000# & " mm^4"
    Debug.Print "  Iyy                      = " & vSectionProp(6) * 1000000000000# & " mm^4"
    Debug.Print "  Izz                      = " & vSectionProp(7) * 1000000000000# & " mm^4"
    Debug.Print "  Ixy                      = " & vSectionProp(8) * 1000000000000# & " mm^4"
    Debug.Print "  Izx                      = " & vSectionProp(9) * 1000000000000# & " mm^4"
    Debug.Print "  Iyz                      = " & vSectionProp(10) * 1000000000000# & " mm^4"
    Debug.Print "  Polar MOI                = " & vSectionProp(11) * 1000000000000# & " mm^4"
    Debug.Print "  Angle princ & part axes  =  " & vSectionProp(12) * 180# / PI & " deg"
    Debug.Print "  Ix                       = " & vSectionProp(13) * 1000000000000# & " mm^4"
    Debug.Print "  Iy                       = " & vSectionProp(14) * 1000000000000# & " mm^4"
```

```
End Sub
```

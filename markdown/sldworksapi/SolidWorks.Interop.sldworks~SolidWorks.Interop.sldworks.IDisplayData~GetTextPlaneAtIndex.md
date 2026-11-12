---
title: "GetTextPlaneAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetTextPlaneAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.html"
---

# GetTextPlaneAtIndex Method (IDisplayData)

Gets the rotation matrix of the specified text relative to the X-Y plane of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextPlaneAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTextPlaneAtIndex(Index)
```

### C#

```csharp
System.object GetTextPlaneAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTextPlaneAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the text whose plane rotation matrix to retrieve (see **Remarks**)

### Return Value

Array of nine doubles of the text plane rotation matrix (see **Remarks**)

## VBA Syntax

See [DisplayData::GetTextPlaneAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetTextPlaneAtIndex.html).

## Examples

'VBA

'Preconditions:

'1. Open a part with three datum annotations in different planes.

'2. Open the Immediate window.

'Postconditions:

'For each datum annotation:

' 1. Prints the text plane rotation matrix.

' 2. Calculates the X-axis of the text plane rotated by the text angle in the XY plane.

' 3. Calculates the cross product of the X- and Z-axis to obtain the new Y-axis.

' 4. Prints the new text plane rotation matrix.

'=======================================

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim aDoc As ModelDoc2
Dim aExt As ModelDocExtension
Dim boolstatus As Boolean
Dim annotVar As Variant
Dim i As Integer
Dim j As Integer
Dim k As Integer

Sub main()

Set swApp = Application.SldWorks
Set aDoc = swApp.ActiveDoc
Set aExt = aDoc.Extension

annotVar = aExt.GetAnnotations()
If Not IsEmpty(annotVar) Then

For i = 0 To UBound(annotVar)
Dim aAnnot As Annotation
Set aAnnot = annotVar(i)

Dim swDispData As SldWorks.DisplayData
Set swDispData = aAnnot.GetDisplayData

Debug.Print "Number of texts in annotation: " & swDispData.GetTextCount()

For j = 0 To swDispData.GetTextCount()

Dim vPlane As Variant
vPlane = swDispData.**GetTextPlaneAtIndex**(j)

If Not (IsEmpty(vPlane)) Then
Debug.Print "Text : " & swDispData.GetTextAtIndex(j)
' Normalize very small positive/negative plane array values to 0
For k = 0 To 8
If vPlane(k) < 0 Then
If (vPlane(k) > -0.000001) Then
vPlane(k) = 0
End If
ElseIf (vPlane(k) < 0.000001) Then
vPlane(k) = 0
End If
Next k

Debug.Print "Normalized text plane rotation matrix: "
Debug.Print "" & vPlane(0) & " " & vPlane(1) & " " & vPlane(2)
Debug.Print "" & vPlane(3) & " " & vPlane(4) & " " & vPlane(5)
Debug.Print "" & vPlane(6) & " " & vPlane(7) & " " & vPlane(8)

Dim xAxis As Variant
Dim yAxis As Variant
Dim zAxis As Variant

' The ordering of the array returned by IDisplayData::GetTextPlaneAtIndex differs from other APIs
xAxis = Array(vPlane(0), vPlane(3), vPlane(6))
yAxis = Array(vPlane(1), vPlane(4), vPlane(7))
zAxis = Array(vPlane(2), vPlane(5), vPlane(8))

Dim angle As Double
angle = swDispData.GetTextAngleAtIndex(j)

' Rotate xAxis by angle in X-Y plane
Dim xAxisNew As Variant
xAxisNew = Array(Cos(angle) * xAxis(0) + Sin(angle) * yAxis(0), Cos(angle) * xAxis(1) + Sin(angle) * yAxis(1), Cos(angle) * xAxis(2) + Sin(angle) * yAxis(2))

' Since rotation in the X-Y plane does not change the normal (Z plane),
' take the cross product of X- and Z-axis arrays to get the new Y-axis array (Y = Z CROSS X)
yAxis = Array(zAxis(1) * xAxisNew(2) - zAxis(2) * xAxisNew(1), -(zAxis(0) * xAxisNew(2) - zAxis(2) * xAxisNew(0)), zAxis(0) * xAxisNew(1) - zAxis(1) * xAxisNew(0))

' Normalize very small positive/negative axis coordinates to 0
For k = 0 To 2
If xAxisNew(k) < 0 Then
If (xAxisNew(k) > -0.000001) Then
xAxisNew(k) = 0
End If
ElseIf (xAxisNew(k) < 0.000001) Then
xAxisNew(k) = 0
End If
Next k

For k = 0 To 2
If yAxis(k) < 0 Then
If (yAxis(k) > -0.000001) Then
yAxis(k) = 0
End If
ElseIf (yAxis(k) < 0.000001) Then
yAxis(k) = 0
End If
Next k

For k = 0 To 2
If zAxis(k) < 0 Then
If (zAxis(k) > -0.000001) Then
zAxis(k) = 0
End If
ElseIf (zAxis(k) < 0.000001) Then
zAxis(k) = 0
End If
Next k

Debug.Print "Normalized text plane matrix after rotation:"
Debug.Print "" & xAxisNew(0) & " " & xAxisNew(1) & " " & xAxisNew(2)
Debug.Print "" & yAxis(0) & " " & yAxis(1) & " " & yAxis(2)
Debug.Print "" & zAxis(0) & " " & zAxis(1) & " " & zAxis(2)

End If
Debug.Print " "
Next j
Next i
End If
End Sub

## Remarks

Use [IDisplayData::GetTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextCount.html) to specify Index.

The nine values of the returned rotation matrix (coord(`i`)) are ordered differently from other plane APIs. If you need to manipulate the text plane axes as is shown in the Example section, use the following assignments:

X-axis: coord(0), coord(3), coord(6)

Y-axis: coord(1), coord(4), coord(7)

Z-axis: coord(2), coord(5), coord(8)

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IAnnotation::GetPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.html)
[IDisplayData::GetTextAngleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAngleAtIndex.html)
[IDisplayData::GetTextAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAtIndex.html)
[IDisplayData::GetTextFontAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextFontAtIndex.html)
[IDisplayData::GetTextHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextHeightAtIndex.html)
[IDisplayData::GetTextInBoxHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxHeightAtIndex.html)
[IDisplayData::GetTextInBoxStyleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.html)
[IDisplayData::GetTextInBoxWidthAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxWidthAtIndex.html)
[IDisplayData::GetTextInvertAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.html)
[IDisplayData::GetTextLineSpacingAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.html)
[IDisplayData::GetTextPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.html)
[IDisplayData::GetTextRefPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.html)

## Availability

SOLIDWORKS 2019 SP01, Revision Number 27.1

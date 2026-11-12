---
title: "InsertAngularDimension3Point Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertAngularDimension3Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimension3Point.html"
---

# InsertAngularDimension3Point Method (ISketchManager)

Inserts an angular Dimension formed by three points.

## Syntax

### Visual Basic

```vb
Function InsertAngularDimension3Point( _
   ByVal CenterPointDblArray As System.Object, _
   ByVal AngleStartPointDblArray As System.Object, _
   ByVal AngleEndPointDblArray As System.Object, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As AngularDimension
```

### C#

```csharp
AngularDimension InsertAngularDimension3Point(
   System.object CenterPointDblArray,
   System.object AngleStartPointDblArray,
   System.object AngleEndPointDblArray,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertAngularDimension3Point(
   CenterPointDblArray : System.Object,
   AngleStartPointDblArray : System.Object,
   AngleEndPointDblArray : System.Object,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : AngularDimension;
```

### Managed Extensions for C++

```
AngularDimension* InsertAngularDimension3Point(
   System.Object* CenterPointDblArray,
   System.Object* AngleStartPointDblArray,
   System.Object* AngleEndPointDblArray,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
AngularDimension^ InsertAngularDimension3Point(
   System.Object^ CenterPointDblArray,
   System.Object^ AngleStartPointDblArray,
   System.Object^ AngleEndPointDblArray,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `CenterPointDblArray`: Array of three doubles indicating the angle's center point (vertex)
- `AngleStartPointDblArray`: Array of three doubles indicating the angle's start point
- `AngleEndPointDblArray`: Array of three doubles indicating the angle's end point
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the angular Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Angular Dimension](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension.html)

## Examples

[Create Angular Dimensions (C#)](Create_Angular_Dimensions_Example_CSharp.htm)
[Create Angular Dimensions (VB.NET)](Create_Angular_Dimensions_Example_VBNET.htm)
[Create Angular Dimensions (VBA)](Create_Angular_Dimensions_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertAngularDimension2Line Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimension2Line.html)
[ISketchManager::InsertAngularDimensionArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimensionArc.html)

## Availability

DraftSight V1R1.2

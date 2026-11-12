---
title: "InsertAngularDimensionArc Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertAngularDimensionArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimensionArc.html"
---

# InsertAngularDimensionArc Method (ISketchManager)

Inserts an angular Dimension formed by the two end points of an Arc.

## Syntax

### Visual Basic

```vb
Function InsertAngularDimensionArc( _
   ByVal Arc As CircleArc, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As AngularDimension
```

### C#

```csharp
AngularDimension InsertAngularDimensionArc(
   CircleArc Arc,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertAngularDimensionArc(
   Arc : CircleArc,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : AngularDimension;
```

### Managed Extensions for C++

```
AngularDimension* InsertAngularDimensionArc(
   CircleArc* Arc,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
AngularDimension^ InsertAngularDimensionArc(
   CircleArc^ Arc,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Arc`: [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
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
[ISketchManager::InsertAngularDimension3Point Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertAngularDimension3Point.html)

## Availability

DraftSight V1R1.2

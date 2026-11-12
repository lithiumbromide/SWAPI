---
title: "InsertRadialDimensionArc Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRadialDimensionArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRadialDimensionArc.html"
---

# InsertRadialDimensionArc Method (ISketchManager)

Inserts a radius Dimension for an Arc.

## Syntax

### Visual Basic

```vb
Function InsertRadialDimensionArc( _
   ByVal Arc As CircleArc, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As RadialDimension
```

### C#

```csharp
RadialDimension InsertRadialDimensionArc(
   CircleArc Arc,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertRadialDimensionArc(
   Arc : CircleArc,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : RadialDimension;
```

### Managed Extensions for C++

```
RadialDimension* InsertRadialDimensionArc(
   CircleArc* Arc,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
RadialDimension^ InsertRadialDimensionArc(
   CircleArc^ Arc,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Arc`: [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the radial Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Radius Dimension](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertRadialDimensionCircle Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRadialDimensionCircle.html)

## Availability

DraftSight V1R1.2

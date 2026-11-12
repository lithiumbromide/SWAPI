---
title: "InsertDiameterDimensionArc Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertDiameterDimensionArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDiameterDimensionArc.html"
---

# InsertDiameterDimensionArc Method (ISketchManager)

Inserts a diameter dimension for an Arc.

## Syntax

### Visual Basic

```vb
Function InsertDiameterDimensionArc( _
   ByVal Arc As CircleArc, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As DiameterDimension
```

### C#

```csharp
DiameterDimension InsertDiameterDimensionArc(
   CircleArc Arc,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertDiameterDimensionArc(
   Arc : CircleArc,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : DiameterDimension;
```

### Managed Extensions for C++

```
DiameterDimension* InsertDiameterDimensionArc(
   CircleArc* Arc,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
DiameterDimension^ InsertDiameterDimensionArc(
   CircleArc^ Arc,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Arc`: [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the diameter Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Diameter Dimension for an Arc](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)
[Insert and Dimenstion Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertDiameterDimensionCircle Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDiameterDimensionCircle.html)

## Availability

DraftSight V1R1.2

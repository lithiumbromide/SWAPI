---
title: "InsertDiameterDimensionCircle Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertDiameterDimensionCircle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDiameterDimensionCircle.html"
---

# InsertDiameterDimensionCircle Method (ISketchManager)

Inserts a diameter dimension for a Circle.

## Syntax

### Visual Basic

```vb
Function InsertDiameterDimensionCircle( _
   ByVal Circle As Circle, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As DiameterDimension
```

### C#

```csharp
DiameterDimension InsertDiameterDimensionCircle(
   Circle Circle,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertDiameterDimensionCircle(
   Circle : Circle,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : DiameterDimension;
```

### Managed Extensions for C++

```
DiameterDimension* InsertDiameterDimensionCircle(
   Circle* Circle,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
DiameterDimension^ InsertDiameterDimensionCircle(
   Circle^ Circle,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Circle`: [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the diameter Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Diameter Dimension for a Circle](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertDiameterDimensionArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDiameterDimensionArc.html)

## Availability

DraftSight V1R1.2

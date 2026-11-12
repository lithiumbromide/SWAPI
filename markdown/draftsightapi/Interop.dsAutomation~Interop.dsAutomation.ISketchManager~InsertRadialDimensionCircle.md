---
title: "InsertRadialDimensionCircle Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRadialDimensionCircle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRadialDimensionCircle.html"
---

# InsertRadialDimensionCircle Method (ISketchManager)

Inserts a radius Dimension for a Circle.

## Syntax

### Visual Basic

```vb
Function InsertRadialDimensionCircle( _
   ByVal Circle As Circle, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As RadialDimension
```

### C#

```csharp
RadialDimension InsertRadialDimensionCircle(
   Circle Circle,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertRadialDimensionCircle(
   Circle : Circle,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : RadialDimension;
```

### Managed Extensions for C++

```
RadialDimension* InsertRadialDimensionCircle(
   Circle* Circle,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
RadialDimension^ InsertRadialDimensionCircle(
   Circle^ Circle,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Circle`: [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
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
[ISketchManager::InsertRadialDimensionArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRadialDimensionArc.html)

## Availability

DraftSight V1R1.2

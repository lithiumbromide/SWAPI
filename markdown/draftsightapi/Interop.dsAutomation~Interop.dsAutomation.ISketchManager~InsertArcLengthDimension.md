---
title: "InsertArcLengthDimension Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArcLengthDimension"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcLengthDimension.html"
---

# InsertArcLengthDimension Method (ISketchManager)

Gets access to an arc length Dimension.

## Syntax

### Visual Basic

```vb
Function InsertArcLengthDimension( _
   ByVal Arc As CircleArc, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As ArcLengthDimension
```

### C#

```csharp
ArcLengthDimension InsertArcLengthDimension(
   CircleArc Arc,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertArcLengthDimension(
   Arc : CircleArc,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : ArcLengthDimension;
```

### Managed Extensions for C++

```
ArcLengthDimension* InsertArcLengthDimension(
   CircleArc* Arc,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
ArcLengthDimension^ InsertArcLengthDimension(
   CircleArc^ Arc,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Arc`: [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
- `DimensionPositionDblArray`: Array of three doubles indicating the point where to place the arc length Dimension
- `DimensionTextOverride`: Text with which to override the default Dimension text

### Return Value

[Arc length Dimension](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertArcLengthDimensionPartial Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcLengthDimensionPartial.html)

## Availability

DraftSight V1R1.2

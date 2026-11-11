---
title: "InsertArcLengthDimensionPartial Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArcLengthDimensionPartial"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcLengthDimensionPartial.html"
---

# InsertArcLengthDimensionPartial Method (ISketchManager)

Gets access to a partial arc length Dimension.

## Syntax

### Visual Basic

```vb
Function InsertArcLengthDimensionPartial( _
   ByVal Arc As CircleArc, _
   ByVal FirstPointDblArray As System.Object, _
   ByVal SecondPointDblArray As System.Object, _
   ByVal DimensionPositionDblArray As System.Object, _
   ByVal DimensionTextOverride As System.String _
) As ArcLengthDimension
```

### C#

```csharp
ArcLengthDimension InsertArcLengthDimensionPartial(
   CircleArc Arc,
   System.object FirstPointDblArray,
   System.object SecondPointDblArray,
   System.object DimensionPositionDblArray,
   System.string DimensionTextOverride
)
```

### JScript

```
function InsertArcLengthDimensionPartial(
   Arc : CircleArc,
   FirstPointDblArray : System.Object,
   SecondPointDblArray : System.Object,
   DimensionPositionDblArray : System.Object,
   DimensionTextOverride : System.String
) : ArcLengthDimension;
```

### Managed Extensions for C++

```
ArcLengthDimension* InsertArcLengthDimensionPartial(
   CircleArc* Arc,
   System.Object* FirstPointDblArray,
   System.Object* SecondPointDblArray,
   System.Object* DimensionPositionDblArray,
   System.string* DimensionTextOverride
)
```

### C++/CLI

```cpp
ArcLengthDimension^ InsertArcLengthDimensionPartial(
   CircleArc^ Arc,
   System.Object^ FirstPointDblArray,
   System.Object^ SecondPointDblArray,
   System.Object^ DimensionPositionDblArray,
   System.String^ DimensionTextOverride
)
```

### Parameters

- `Arc`: [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
- `FirstPointDblArray`: Array of three doubles indicating the start point on the Arc
- `SecondPointDblArray`: Array of three doubles indicating the end point on the Arc
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
[ISketchManager::InsertArcLengthDimension Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcLengthDimension.html)

## Availability

DraftSight V1R1.2

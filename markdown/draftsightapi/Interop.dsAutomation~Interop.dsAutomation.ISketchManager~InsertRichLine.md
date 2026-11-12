---
title: "InsertRichLine Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertRichLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertRichLine.html"
---

# InsertRichLine Method (ISketchManager)

Constructs a RichLine.

## Syntax

### Visual Basic

```vb
Function InsertRichLine( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Justification As dsRichLineJustification_e, _
   ByVal Scale As System.Double, _
   ByVal StyleName As System.String, _
   ByVal Closed As System.Boolean _
) As RichLine
```

### C#

```csharp
RichLine InsertRichLine(
   System.object CoordinateDblArray,
   dsRichLineJustification_e Justification,
   System.double Scale,
   System.string StyleName,
   System.bool Closed
)
```

### JScript

```
function InsertRichLine(
   CoordinateDblArray : System.Object,
   Justification : dsRichLineJustification_e,
   Scale : System.double,
   StyleName : System.String,
   Closed : System.boolean
) : RichLine;
```

### Managed Extensions for C++

```
RichLine* InsertRichLine(
   System.Object* CoordinateDblArray,
   dsRichLineJustification_e Justification,
   System.double Scale,
   System.string* StyleName,
   System.bool Closed
)
```

### C++/CLI

```cpp
RichLine^ InsertRichLine(
   System.Object^ CoordinateDblArray,
   dsRichLineJustification_e Justification,
   System.double Scale,
   System.String^ StyleName,
   System.bool Closed
)
```

### Parameters

- `CoordinateDblArray`: Array of x, y, and z coordinates indicating the start point for the RichLine and the segment vertices to define the RichLine (see **Remarks**)
- `Justification`: Justification as defined in [dsRichLineJustification_e](Interop.dsAutomation~Interop.dsAutomation.dsRichLineJustification_e.html)
- `Scale`: Scale factor; default is 1.0 and does not affect the overall LineScale factor
- `StyleName`: Name of the RichLineStyle to use
- `Closed`: True to close the RichLine, false to leave the RichLine open

### Return Value

[RichLine](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)

## Examples

[Construct RichLine (C#)](Construct_RichLine_Example_CSharp.htm)
[Construct RichLine (VB.NET)](Construct_RichLine_Example_VBNET.htm)
[Construct RichLine (VBA)](Construct_RichLine_Example_VBA.htm)

## Remarks

The size of CoordinateDblArray is (3 * (Number of vertices)). The order of the elements in the array is (x1, y1, z1, x2, y2, z2...).

The x1, y1, and z1 coordinates in the array represent the start point; all subsequent x`n`, y`n`, and z`n` coordinates represent segment vertices.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[IRichLineStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~Name.html)

## Availability

DraftSight V1R1.1

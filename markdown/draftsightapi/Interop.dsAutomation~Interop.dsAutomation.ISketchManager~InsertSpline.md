---
title: "InsertSpline Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertSpline"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertSpline.html"
---

# InsertSpline Method (ISketchManager)

Constructs a Spline.

## Syntax

### Visual Basic

```vb
Function InsertSpline( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Closed As System.Boolean, _
   ByVal StartTangencyX As System.Double, _
   ByVal StartTangencyY As System.Double, _
   ByVal StartTangencyZ As System.Double, _
   ByVal EndTangencyX As System.Double, _
   ByVal EndTangencyY As System.Double, _
   ByVal EndTangencyZ As System.Double _
) As Spline
```

### C#

```csharp
Spline InsertSpline(
   System.object CoordinateDblArray,
   System.bool Closed,
   System.double StartTangencyX,
   System.double StartTangencyY,
   System.double StartTangencyZ,
   System.double EndTangencyX,
   System.double EndTangencyY,
   System.double EndTangencyZ
)
```

### JScript

```
function InsertSpline(
   CoordinateDblArray : System.Object,
   Closed : System.boolean,
   StartTangencyX : System.double,
   StartTangencyY : System.double,
   StartTangencyZ : System.double,
   EndTangencyX : System.double,
   EndTangencyY : System.double,
   EndTangencyZ : System.double
) : Spline;
```

### Managed Extensions for C++

```
Spline* InsertSpline(
   System.Object* CoordinateDblArray,
   System.bool Closed,
   System.double StartTangencyX,
   System.double StartTangencyY,
   System.double StartTangencyZ,
   System.double EndTangencyX,
   System.double EndTangencyY,
   System.double EndTangencyZ
)
```

### C++/CLI

```cpp
Spline^ InsertSpline(
   System.Object^ CoordinateDblArray,
   System.bool Closed,
   System.double StartTangencyX,
   System.double StartTangencyY,
   System.double StartTangencyZ,
   System.double EndTangencyX,
   System.double EndTangencyY,
   System.double EndTangencyZ
)
```

### Parameters

- `CoordinateDblArray`: Array of doubles of the coordinates of the control and fit points of the Spline
- `Closed`: True if closed, false if open
- `StartTangencyX`: x coordinate of tangency vector at the Spline's starting vertex
- `StartTangencyY`: y coordinate of tangency vector at the Spline's starting vertex
- `StartTangencyZ`: z coordinate of tangency vector at the Spline's starting vertex
- `EndTangencyX`: x coordinate of tangency vector at the Spline's ending vertex
- `EndTangencyY`: y coordinate of tangency vector at the Spline's ending vertex
- `EndTangencyZ`: z coordinate of tangency vector at the Spline's ending vertex

### Return Value

[Spline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)

## Examples

[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.3

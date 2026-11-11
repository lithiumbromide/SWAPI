---
title: "InsertLine Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertLine.html"
---

# InsertLine Method (ISketchManager)

Constructs a Line.

## Syntax

### Visual Basic

```vb
Function InsertLine( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double _
) As Line
```

### C#

```csharp
Line InsertLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

### JScript

```
function InsertLine(
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   EndX : System.double,
   EndY : System.double,
   EndZ : System.double
) : Line;
```

### Managed Extensions for C++

```
Line* InsertLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

### C++/CLI

```cpp
Line^ InsertLine(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

### Parameters

- `StartX`: x coordinate where to start the Line
- `StartY`: y coordinate where to start the Line
- `StartZ`: z coordinate where to start the Line
- `EndX`: x coordinate where to end the Line
- `EndY`: y coordinate where to end the Line
- `EndZ`: z coordinate where to end the Line

### Return Value

[Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html)

## Examples

[Construct Line (C#)](Construct_Line_Example_CSharp.htm)
[Construct Line (VB.NET)](Construct_Line_Example_VBNET.htm)
[Construct Line (VBA)](Construct_Line_Example_VBA.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Attach Block Definition Annotation to Leader (C#)](Attach_Block_Definition_Annotation_to_Leader_Example_CSharp.htm)
[Attach Block Definition Annotation to Leader (VB.NET)](Attach_Block_Definition_Annotation_to_Leader_Example_VBNET.htm)
[Attach Block Definition Annotation to Leader (VBA)](Attach_Block_Definition_Annotation_to_Leader_Example_VBA.htm)
[Attach Block Definition Annotation to Leader (JavaScript)](Attach_Block_Definition_Annotation_to_Leader_Example_JS.htm)
[Load and Activate LineStyles (C#)](Load_and_Activate_LineStyles_Example_CSharp.htm)
[Load and Activate LineStyles (VB.NET)](Laod_and_Activate_LineStyles_Example_VBNET.htm)
[Load and Activate LineStyles (VBA)](Load_and_Activate_LineStyles_Example_VBA.htm)
[Load and Activate LineStyles (JavaScript)](Load_and_Activate_LineStyles_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.1

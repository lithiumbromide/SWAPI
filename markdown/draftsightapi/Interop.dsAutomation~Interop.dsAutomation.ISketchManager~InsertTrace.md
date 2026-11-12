---
title: "InsertTrace Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertTrace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertTrace.html"
---

# InsertTrace Method (ISketchManager)

Inserts a Trace, which is a 2D solid Line.

## Syntax

### Visual Basic

```vb
Function InsertTrace( _
   ByVal CoordinateDblArray As System.Object _
) As Trace
```

### C#

```csharp
Trace InsertTrace(
   System.object CoordinateDblArray
)
```

### JScript

```
function InsertTrace(
   CoordinateDblArray : System.Object
) : Trace;
```

### Managed Extensions for C++

```
Trace* InsertTrace(
   System.Object* CoordinateDblArray
)
```

### C++/CLI

```cpp
Trace^ InsertTrace(
   System.Object^ CoordinateDblArray
)
```

### Parameters

- `CoordinateDblArray`: Array of doubles of the x, y, and z coordinates of the four vertices of the Trace

### Return Value

[Trace](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)

## Examples

[Create and Change Trace (C#)](Create_and_Change_Trace_Example_CSharp.htm)
[Create and Change Trace (VB.NET)](Create_and_Change_Trace_Example_VBNET.htm)
[Create and Change Trace (VBA)](Create_and_Change_Trace_Example_VBA.htm)

## Remarks

The first and second sets of x, y, and z coordinates specify the width of the Trace. The third and fourth sets of x, y, and z coordinates specify the start and end points of the 2D solid Line, respectively.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R5.0

---
title: "InsertSimpleNote Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertSimpleNote"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertSimpleNote.html"
---

# InsertSimpleNote Method (ISketchManager)

Inserts a SimpleNote.

## Syntax

### Visual Basic

```vb
Function InsertSimpleNote( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal Height As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Value As System.String _
) As SimpleNote
```

### C#

```csharp
SimpleNote InsertSimpleNote(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double Height,
   System.double Angle,
   System.string Value
)
```

### JScript

```
function InsertSimpleNote(
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   Height : System.double,
   Angle : System.double,
   Value : System.String
) : SimpleNote;
```

### Managed Extensions for C++

```
SimpleNote* InsertSimpleNote(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double Height,
   System.double Angle,
   System.string* Value
)
```

### C++/CLI

```cpp
SimpleNote^ InsertSimpleNote(
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double Height,
   System.double Angle,
   System.String^ Value
)
```

### Parameters

- `StartX`: x coordinate for the insertion point
- `StartY`: y coordinate for the insertion point
- `StartZ`: z coordinate for the insertion point
- `Height`: Height (text size)
- `Angle`: Angle of insertion; in radians
- `Value`: Text

### Return Value

[SimpleNote](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)

## Examples

[Insert SimpleNote (C#)](Insert_SimpleNote_Example_CSharp.htm)
[Insert SimpleNote (VB.NET)](Insert_SimpleNote_Example_VBNET.htm)
[Insert SimpleNote (VBA)](Insert_SimpleNote_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.1

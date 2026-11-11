---
title: "InsertNote Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertNote"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNote.html"
---

# InsertNote Method (ISketchManager)

Inserts a Note.

## Syntax

### Visual Basic

```vb
Function InsertNote( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal StrArray As System.Object _
) As Note
```

### C#

```csharp
Note InsertNote(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.object StrArray
)
```

### JScript

```
function InsertNote(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double,
   StrArray : System.Object
) : Note;
```

### Managed Extensions for C++

```
Note* InsertNote(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.Object* StrArray
)
```

### C++/CLI

```cpp
Note^ InsertNote(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.Object^ StrArray
)
```

### Parameters

- `X1`: x coordinate of upper-left corner of Note
- `Y1`: y coordinate of upper-left corner of Note
- `Z1`: z coordinate of upper-left corner of Note
- `X2`: x coordinate of lower-right corner of Note
- `Y2`: y coordinate of lower-right corner of Note
- `Z2`: z coordinate of lower-right corner of Note
- `StrArray`: Array of strings constituting the text of the Note

### Return Value

[Note](Interop.dsAutomation~Interop.dsAutomation.INote.html)

## Examples

[Insert Notes (C#)](Insert_Notes_Example_CSharp.htm)
[Insert Notes (VB.NET)](Insert_Notes_Example_VBNET.htm)
[Insert Notes (VBA)](Insert_Notes_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[INote::InsertNoteWithParameters Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNoteWithParameters.html)

## Availability

DraftSight V1R1.1

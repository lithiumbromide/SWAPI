---
title: "SetNoteAnnotation Method (ILeader)"
project: ""
interface: "ILeader"
member: "SetNoteAnnotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~SetNoteAnnotation.html"
---

# SetNoteAnnotation Method (ILeader)

Attaches a [Note](Interop.dsAutomation~Interop.dsAutomation.INote.html) to the Leader.

## Syntax

### Visual Basic

```vb
Sub SetNoteAnnotation( _
   ByVal Text As System.String, _
   ByVal InsertPoint As MathPoint _
)
```

### C#

```csharp
void SetNoteAnnotation(
   System.string Text,
   MathPoint InsertPoint
)
```

### JScript

```
function SetNoteAnnotation(
   Text : System.String,
   InsertPoint : MathPoint
);
```

### Managed Extensions for C++

```
void SetNoteAnnotation(
   System.string* Text,
   MathPoint* InsertPoint
)
```

### C++/CLI

```cpp
void SetNoteAnnotation(
   System.String^ Text,
   MathPoint^ InsertPoint
)
```

### Parameters

- `Text`: Text for the Note to attach to the Leader
- `InsertPoint`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) where to attach the Note to the Leader

## Examples

[Attach Note and Tolerance Annotations to Leaders (C#)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_CSharp.htm)
[Attach Note and Tolerance Annotations to Leaders (VB.NET)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBNET.htm)
[Attach Note and Tolerance Annotations to Leaders (VBA)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBA.htm)
[Attach Note and Tolerance Annotations to Leaders (JavaScript)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_JS.htm)

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::GetNoteAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetNoteAnnotation.html)
[ILeader::RemoveAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveAnnotation.html)

## Availability

DraftSight V1R3.1

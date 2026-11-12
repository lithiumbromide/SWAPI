---
title: "GetNextParent Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "GetNextParent"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextParent.html"
---

# GetNextParent Method (IEdmReference5)

Enumerates the files referencing this file.

## Syntax

### Visual Basic

```vb
Function GetNextParent( _
   ByVal poPos As IEdmPos5 _
) As IEdmReference5
```

### C#

```csharp
IEdmReference5 GetNextParent(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmReference5^ GetNextParent(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of the next parent file to get

### Return Value

Parent [file](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)

## Examples

[Get Parent References of File (VB.NET)](Get_Parent_References_Example_VBNET.htm)
[Get Parent References of File (C#)](Get_Parent_References_Example_CSharp.htm)

## Remarks

Call [IEdmReference7::GetFirstParentPosition2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstParentPosition2.html) to get the position of the first referenced parent file, before you call this method the first time.

After calling this method the first time, poPos is automatically incremented every time this method is called. Call this method repeatedly to obtain the rest of the referenced parent files.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

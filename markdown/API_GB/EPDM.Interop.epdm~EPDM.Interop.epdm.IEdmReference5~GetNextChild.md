---
title: "GetNextChild Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "GetNextChild"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html"
---

# GetNextChild Method (IEdmReference5)

Enumerates the files referenced by this file.

## Syntax

### Visual Basic

```vb
Function GetNextChild( _
   ByVal poPos As IEdmPos5 _
) As IEdmReference5
```

### C#

```csharp
IEdmReference5 GetNextChild(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmReference5^ GetNextChild(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of next child file to get

### Return Value

Child [file](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

Call [IEdmReference5::GetFirstChildPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetFirstChildPosition.html) to get the position of the first referenced child file, before you call IEdmReference5::GetNextChild for the first time.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the referenced child files.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

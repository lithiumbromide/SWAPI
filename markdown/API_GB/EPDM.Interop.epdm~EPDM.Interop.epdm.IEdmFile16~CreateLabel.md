---
title: "CreateLabel Method (IEdmFile16)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile16"
member: "CreateLabel"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html"
---

# CreateLabel Method (IEdmFile16)

Creates a label with the specified name and description for this file.

## Syntax

### Visual Basic

```vb
Function CreateLabel( _
   ByVal bsName As System.String, _
   ByVal bsDescription As System.String _
) As System.Integer
```

### C#

```csharp
System.int CreateLabel(
   System.string bsName,
   System.string bsDescription
)
```

### C++/CLI

```cpp
System.int CreateLabel(
   System.String^ bsName,
   System.String^ bsDescription
)
```

### Parameters

- `bsName`: Name of the label; maximum of 255 characters
- `bsDescription`: Label description to show in the history dialog box; maximum of 2000 characters

### Return Value

ID of the file label

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

Use [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) to get the [IEdmLabel5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html) object for this label.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments in invalid.

## See Also

[IEdmFile16 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16.html)
[IEdmFile16 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16_members.html)
[IEdmFolder5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateLabel.html)
[IEdmEnumeratorVersion5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~CreateLabel.html)

## Availability

SOLIDWORKS PDM Professional 2019 SP04

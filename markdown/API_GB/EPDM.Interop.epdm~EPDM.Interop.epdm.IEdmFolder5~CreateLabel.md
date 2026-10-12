---
title: "CreateLabel Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "CreateLabel"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateLabel.html"
---

# CreateLabel Method (IEdmFolder5)

Creates a label on this folder and its subfolders.

## Syntax

### Visual Basic

```vb
Function CreateLabel( _
   ByVal bsName As System.String, _
   ByVal bsDescription As System.String, _
   Optional ByVal bRecursively As System.Boolean _
) As System.Integer
```

### C#

```csharp
System.int CreateLabel(
   System.string bsName,
   System.string bsDescription,
   System.bool bRecursively
)
```

### C++/CLI

```cpp
System.int CreateLabel(
   System.String^ bsName,
   System.String^ bsDescription,
   System.bool bRecursively
)
```

### Parameters

- `bsName`: Name of the label; maximum of 255 characters
- `bsDescription`: Label description to show in the history dialog box; maximum of 2000 characters
- `bRecursively`: Optionally, true to set the label recursively on subfolders, false to not; default is true

### Return Value

ID of the new label

## Examples

[Create Labels on Folders (VB.NET)](Create_Label_Example_VBNET.htm)
[Create Labels on Folders (C#)](Create_Label_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments in invalid.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmFolder5::GetFirstLabelPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstLabelPosition.html)
[IEdmFile16::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html)
[IEdmEnumeratorVersion5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~CreateLabel.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

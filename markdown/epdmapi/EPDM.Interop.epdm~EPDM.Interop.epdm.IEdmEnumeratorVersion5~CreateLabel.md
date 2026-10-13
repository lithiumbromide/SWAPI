---
title: "CreateLabel Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "CreateLabel"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~CreateLabel.html"
---

# CreateLabel Method (IEdmEnumeratorVersion5)

Sets a label on the latest version of this file.

## Syntax

### Visual Basic

```vb
Function CreateLabel( _
   ByVal bsName As System.String, _
   ByVal bsComment As System.String _
) As System.Integer
```

### C#

```csharp
System.int CreateLabel(
   System.string bsName,
   System.string bsComment
)
```

### C++/CLI

```cpp
System.int CreateLabel(
   System.String^ bsName,
   System.String^ bsComment
)
```

### Parameters

- `bsName`: Name of label; maximum 255 characters
- `bsComment`: Label comment; maximum 2000 characters

### Return Value

ID of the label

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)
[IEdmFile16::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile16~CreateLabel.html)
[IEdmFolder5::CreateLabel Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateLabel.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

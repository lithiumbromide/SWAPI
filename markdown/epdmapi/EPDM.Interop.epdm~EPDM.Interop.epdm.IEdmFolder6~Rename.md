---
title: "Rename Method (IEdmFolder6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder6"
member: "Rename"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~Rename.html"
---

# Rename Method (IEdmFolder6)

Renames this folder.

## Syntax

### Visual Basic

```vb
Sub Rename( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsNewName As System.String, _
   ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void Rename(
   System.int lParentWnd,
   System.string bsNewName,
   System.int lFlags
)
```

### C++/CLI

```cpp
void Rename(
   System.int lParentWnd,
   System.String^ bsNewName,
   System.int lFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsNewName`: New name of the folder
- `lFlags`: 0; reserved for future use

## Remarks

If this folder contains files with external references, this method could take an extended period of time to rewrite the include paths.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html)
[IEdmFolder6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

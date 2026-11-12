---
title: "RenameEx Method (IEdmFile6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile6"
member: "RenameEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6~RenameEx.html"
---

# RenameEx Method (IEdmFile6)

Changes the name of this file.

## Syntax

### Visual Basic

```vb
Sub RenameEx( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsNewName As System.String, _
   ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void RenameEx(
   System.int lParentWnd,
   System.string bsNewName,
   System.int lFlags
)
```

### C++/CLI

```cpp
void RenameEx(
   System.int lParentWnd,
   System.String^ bsNewName,
   System.int lFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsNewName`: New file name
- `lFlags`: 0; reserved

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html)
[IEdmFile6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

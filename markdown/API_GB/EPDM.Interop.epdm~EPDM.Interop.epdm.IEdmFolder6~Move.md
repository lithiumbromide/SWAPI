---
title: "Move Method (IEdmFolder6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder6"
member: "Move"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~Move.html"
---

# Move Method (IEdmFolder6)

Moves this folder to a new location.

## Syntax

### Visual Basic

```vb
Sub Move( _
   ByVal lParentWnd As System.Integer, _
   ByVal lNewParentID As System.Integer, _
   ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void Move(
   System.int lParentWnd,
   System.int lNewParentID,
   System.int lFlags
)
```

### C++/CLI

```cpp
void Move(
   System.int lParentWnd,
   System.int lNewParentID,
   System.int lFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lNewParentID`: ID of new parent folder
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

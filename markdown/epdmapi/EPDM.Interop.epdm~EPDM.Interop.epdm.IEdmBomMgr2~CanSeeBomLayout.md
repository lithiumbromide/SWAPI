---
title: "CanSeeBomLayout Method (IEdmBomMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr2"
member: "CanSeeBomLayout"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~CanSeeBomLayout.html"
---

# CanSeeBomLayout Method (IEdmBomMgr2)

Gets whether the specified BOM layout is visible to the specified user.

## Syntax

### Visual Basic

```vb
Function CanSeeBomLayout( _
   ByVal lLayoutId As System.Integer, _
   ByVal lUserID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool CanSeeBomLayout(
   System.int lLayoutId,
   System.int lUserID
)
```

### C++/CLI

```cpp
System.bool CanSeeBomLayout(
   System.int lLayoutId,
   System.int lUserID
)
```

### Parameters

- `lLayoutId`: BOM layout ID
- `lUserID`: User ID

### Return Value

True if visible, false if not

## Examples

See the [IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html) examples.

## See Also

[IEdmBomMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html)
[IEdmBomMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2020

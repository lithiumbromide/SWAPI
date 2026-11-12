---
title: "GetRefs Method (IEdmRefItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItem"
member: "GetRefs"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~GetRefs.html"
---

# GetRefs Method (IEdmRefItem)

Gets the references of this item.

## Syntax

### Visual Basic

```vb
Sub GetRefs( _
   ByVal eType As EdmRefType, _
   ByRef ppoRetItems() As System.Object _
)
```

### C#

```csharp
void GetRefs(
   EdmRefType eType,
   out System.object[] ppoRetItems
)
```

### C++/CLI

```cpp
void GetRefs(
   EdmRefType eType,
   [Out] System.array<Object^>^ ppoRetItems
)
```

### Parameters

- `eType`: Type of reference to get as defined in [EdmRefType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefType.html)
- `ppoRetItems`: Array of [IEdmRefItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)s; one interface pointer for each item reference

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRefItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)
[IEdmRefItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4

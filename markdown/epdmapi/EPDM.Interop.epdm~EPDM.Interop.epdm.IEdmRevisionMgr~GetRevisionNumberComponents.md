---
title: "GetRevisionNumberComponents Method (IEdmRevisionMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr"
member: "GetRevisionNumberComponents"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr~GetRevisionNumberComponents.html"
---

# GetRevisionNumberComponents Method (IEdmRevisionMgr)

Obsolete. Superseded by [IEdmRevisionMgr2::GetRevisionNumberComponents2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberComponents2.html).

## Syntax

### Visual Basic

```vb
Sub GetRevisionNumberComponents( _
   ByRef ppoComponents() As EdmRevComponent _
)
```

### C#

```csharp
void GetRevisionNumberComponents(
   out EdmRevComponent[] ppoComponents
)
```

### C++/CLI

```cpp
void GetRevisionNumberComponents(
   [Out] array<EdmRevComponent>^ ppoComponents
)
```

### Parameters

- `ppoComponents`: Array of [EdmRevComponent](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent.html) structures; one structure for each revision number component

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr.html)
[IEdmRevisionMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2007

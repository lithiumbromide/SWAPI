---
title: "AddUsers2 Method (IEdmUserMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr7"
member: "AddUsers2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddUsers2.html"
---

# AddUsers2 Method (IEdmUserMgr7)

Obsolete. Superseded by [IEdmUserMgr10::AddUsers3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr10~AddUsers3.html).

## Syntax

### Visual Basic

```vb
Sub AddUsers2( _
   ByRef ppoUserData As EdmUserData2() _
)
```

### C#

```csharp
void AddUsers2(
   out EdmUserData2[] ppoUserData
)
```

### C++/CLI

```cpp
void AddUsers2(
   [Out] array<EdmUserData2> ppoUserData
)
```

### Parameters

- `ppoUserData`: Array of [EdmUserData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html) structures; one structure for each user

## Examples

[Add Users (VB.NET)](Add_Users_Example_VBNET.htm)
[Add Users (C#)](Add_Users_Example_CSharp.htm)

## Remarks

This method supersedes [IEdmUserMgr6::AddUsers](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddUsers.html) by providing the ability to specify permissions for added users.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7.html)
[IEdmUserMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010

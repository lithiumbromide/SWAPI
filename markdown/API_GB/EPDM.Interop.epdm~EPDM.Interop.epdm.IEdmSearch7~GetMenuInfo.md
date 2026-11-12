---
title: "GetMenuInfo Method (IEdmSearch7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch7"
member: "GetMenuInfo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7~GetMenuInfo.html"
---

# GetMenuInfo Method (IEdmSearch7)

Gets information that can be used to display a quick launch menu from which the user can start the search tool and activate one of his search forms or favorites.

## Syntax

### Visual Basic

```vb
Sub GetMenuInfo( _
   ByRef ppoForms As System.String(), _
   ByRef ppoFavorites As System.String(), _
   ByRef plSysPerm As System.Integer, _
   ByRef plEdmGetMenuInfoFlags As System.Integer _
)
```

### C#

```csharp
void GetMenuInfo(
   out System.string[] ppoForms,
   out System.string[] ppoFavorites,
   out System.int plSysPerm,
   out System.int plEdmGetMenuInfoFlags
)
```

### C++/CLI

```cpp
void GetMenuInfo(
   [Out] System.array<String^> ppoForms,
   [Out] System.array<String^> ppoFavorites,
   [Out] System.int plSysPerm,
   [Out] System.int plEdmGetMenuInfoFlags
)
```

### Parameters

- `ppoForms`: Array of search forms
- `ppoFavorites`: Array of favorite searches
- `plSysPerm`: Combination of [EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html) bits for the logged-in user
- `plEdmGetMenuInfoFlags`: Combination of [EdmGetMenuInfoFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetMenuInfoFlags.html) bits

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSearch7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7.html)
[IEdmSearch7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7_members.html)

## Availability

SOLIDWORKS PDM Professional 2009

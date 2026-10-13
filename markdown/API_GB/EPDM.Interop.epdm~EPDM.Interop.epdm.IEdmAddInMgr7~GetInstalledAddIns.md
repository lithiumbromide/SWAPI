---
title: "GetInstalledAddIns Method (IEdmAddInMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr7"
member: "GetInstalledAddIns"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr7~GetInstalledAddIns.html"
---

# GetInstalledAddIns Method (IEdmAddInMgr7)

Gets information about all of the add-ins that have been installed in the vault.

## Syntax

### Visual Basic

```vb
Sub GetInstalledAddIns( _
   ByRef ppoAddIns As EdmAddInInfo2() _
)
```

### C#

```csharp
void GetInstalledAddIns(
   out EdmAddInInfo2[] ppoAddIns
)
```

### C++/CLI

```cpp
void GetInstalledAddIns(
   [Out] array<EdmAddInInfo2> ppoAddIns
)
```

### Parameters

- `ppoAddIns`: Array of [EdmAddInInfo2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html) structures, one structure for each add-in

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr7.html)
[IEdmAddInMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr7_members.html)
[IEdmAddInMgr8::GetInstalledAddIn Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~GetInstalledAddIn.html)

## Availability

SOLIDWORKS PDM Professional 2008

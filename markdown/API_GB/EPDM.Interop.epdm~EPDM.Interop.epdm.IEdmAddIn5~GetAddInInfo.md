---
title: "GetAddInInfo Method (IEdmAddIn5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddIn5"
member: "GetAddInInfo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html"
---

# GetAddInInfo Method (IEdmAddIn5)

Called by SOLIDWORKS PDM Professional to obtain information about this add-in and the commands it supports.

## Syntax

### Visual Basic

```vb
Sub GetAddInInfo( _
   ByRef poInfo As EdmAddInInfo, _
   ByVal poVault As IEdmVault5, _
   ByVal poCmdMgr As IEdmCmdMgr5 _
)
```

### C#

```csharp
void GetAddInInfo(
   out EdmAddInInfo poInfo,
   IEdmVault5 poVault,
   IEdmCmdMgr5 poCmdMgr
)
```

### C++/CLI

```cpp
void GetAddInInfo(
   [Out] EdmAddInInfo poInfo,
   IEdmVault5^ poVault,
   IEdmCmdMgr5^ poCmdMgr
)
```

### Parameters

- `poInfo`: [EdmAddInInfo structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.html); before returning this structure, populate it with information about your add-in; used by the [Administration Add-ins dialog](AdminDlg.htm) during add-in registration
- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); pointer to the active vault
- `poCmdMgr`: [IEdmCmdMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5.html); pointer to the command manager that you use to add hooks, menu commands, and toolbar buttons

## Examples

See the [IEdmAddin5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html) examples.

## Remarks

See [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html) for more information.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddIn5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)
[IEdmAddIn5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

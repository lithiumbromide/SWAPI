---
title: "GetDebugAddIns Method (IEdmAddInMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr6"
member: "GetDebugAddIns"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~GetDebugAddIns.html"
---

# GetDebugAddIns Method (IEdmAddInMgr6)

Gets information about all of the add-ins that have been installed for debugging on this machine.

## Syntax

### Visual Basic

```vb
Sub GetDebugAddIns( _
   ByRef ppoAddIns() As EdmAddInInfo2 _
)
```

### C#

```csharp
void GetDebugAddIns(
   out EdmAddInInfo2[] ppoAddIns
)
```

### C++/CLI

```cpp
void GetDebugAddIns(
   [Out] array<EdmAddInInfo2>^ ppoAddIns
)
```

### Parameters

- `ppoAddIns`: Array of [EdmAddInInfo2 structures](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html); one structure for each debug add-in

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## Remarks

You can install add-ins for debugging either of two ways:

- Right-clicking the **Add-ins** node in the SOLIDWORKS PDM Professional Administration Tool and clicking **Debug Add-ins**.
- Calling [IEdmAddInMgr6::InstallDebugAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~InstallDebugAddIn.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6.html)
[IEdmAddInMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional

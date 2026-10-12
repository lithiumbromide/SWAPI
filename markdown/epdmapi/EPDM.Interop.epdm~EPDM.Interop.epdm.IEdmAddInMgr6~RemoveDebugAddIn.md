---
title: "RemoveDebugAddIn Method (IEdmAddInMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr6"
member: "RemoveDebugAddIn"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~RemoveDebugAddIn.html"
---

# RemoveDebugAddIn Method (IEdmAddInMgr6)

Removes an add-in that has been installed for debugging.

## Syntax

### Visual Basic

```vb
Sub RemoveDebugAddIn( _
   ByVal oAddIn As System.Object _
)
```

### C#

```csharp
void RemoveDebugAddIn(
   System.object oAddIn
)
```

### C++/CLI

```cpp
void RemoveDebugAddIn(
   System.Object^ oAddIn
)
```

### Parameters

- `oAddIn`: Contains either the path to the DLL of the add-in to remove or the ID of the class that implements [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)

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

Version 6.4 of SOLIDWORKS PDM Professional or later

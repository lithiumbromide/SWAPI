---
title: "InstallDebugAddIn Method (IEdmAddInMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr6"
member: "InstallDebugAddIn"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~InstallDebugAddIn.html"
---

# InstallDebugAddIn Method (IEdmAddInMgr6)

Installs an add-in for debugging on this machine.

## Syntax

### Visual Basic

```vb
Sub InstallDebugAddIn( _
   ByVal oAddIn As System.Object _
)
```

### C#

```csharp
void InstallDebugAddIn(
   System.object oAddIn
)
```

### C++/CLI

```cpp
void InstallDebugAddIn(
   System.Object^ oAddIn
)
```

### Parameters

- `oAddIn`: Contains either the path to the DLL of the add-in to add or the ID of the class that implements [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html)

## Remarks

You can install add-ins for debugging either of two ways:

- Right-clicking the **Add-ins** node in the SOLIDWORKS PDM Professional Administration Tool and clicking **Debug Add-ins**.
- Calling this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6.html)
[IEdmAddInMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6_members.html)
[IEdmAddInMgr6::RemoveDebugAddIn Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~RemoveDebugAddIn.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional

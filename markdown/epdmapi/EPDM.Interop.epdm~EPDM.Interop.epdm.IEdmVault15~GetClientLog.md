---
title: "GetClientLog Method (IEdmVault15)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault15"
member: "GetClientLog"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault15~GetClientLog.html"
---

# GetClientLog Method (IEdmVault15)

Gets the contents of the current user's log.

## Syntax

### Visual Basic

```vb
Sub GetClientLog( _
   ByRef pbsRetLogs As System.String _
)
```

### C#

```csharp
void GetClientLog(
   out System.string pbsRetLogs
)
```

### C++/CLI

```cpp
void GetClientLog(
   [Out] System.String^ pbsRetLogs
)
```

### Parameters

- `pbsRetLogs`: Contents of the current user's log

## Examples

[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)
[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)

## Remarks

The current user's log appears when you click **SOLIDWORKS PDM Administration > Local Settings > Log File** in the SOLIDWORKS PDM Administration Tool. This method returns the full log.

## See Also

[IEdmVault15 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault15.html)
[IEdmVault15 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault15_members.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP03

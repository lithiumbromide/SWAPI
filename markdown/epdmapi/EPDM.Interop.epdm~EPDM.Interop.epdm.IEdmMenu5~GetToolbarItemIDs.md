---
title: "GetToolbarItemIDs Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "GetToolbarItemIDs"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetToolbarItemIDs.html"
---

# GetToolbarItemIDs Method (IEdmMenu5)

Gets the toolbar buttons associated with the menu commands.

## Syntax

### Visual Basic

```vb
Sub GetToolbarItemIDs( _
   ByRef ppoRetID() As System.Integer _
)
```

### C#

```csharp
void GetToolbarItemIDs(
   out System.int[] ppoRetID
)
```

### C++/CLI

```cpp
void GetToolbarItemIDs(
   [Out] System.array<int>^ ppoRetID
)
```

### Parameters

- `ppoRetID`: Array of IDs (see **Remarks**)

## Remarks

The toolbar buttons were added to SOLIDWORKS PDM Professional with the [EdmMenuFlags.EdmMenu_HasToolbarButton](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html) flag specified in the call to [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html).

C++ programmers must remember to correctly create and destroy the returned SAFEARRAY of IDs to avoid errors.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)
[IEdmMenu6::GetItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6~GetItems.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

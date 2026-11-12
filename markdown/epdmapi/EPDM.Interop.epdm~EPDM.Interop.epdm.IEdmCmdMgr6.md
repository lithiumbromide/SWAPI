---
title: "IEdmCmdMgr6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdMgr6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6.html"
---

# IEdmCmdMgr6 Interface

Allows you to add menu commands, toolbar buttons, and command hooks to SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCmdMgr6
   Inherits IEdmCmdMgr5
```

### C#

```csharp
public interface IEdmCmdMgr6 : IEdmCmdMgr5
```

### C++/CLI

```cpp
public interface class IEdmCmdMgr6 : public IEdmCmdMgr5
```

## Examples

[Create Vault View Tab Add-in (C#)](Create_Vault_View_Tab_Addin_Example_CSharp.htm)

## Remarks

This interface extends [IEdmCmdMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5.html) by providing the ability to add a custom tab to a vault view before it is opened in File Explorer.

A pointer to this interface is provided by SOLIDWORKS PDM Professional when it loads an add-in. [IEdmAddIn5::GetAddInInfo's](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) poCmdMgr contains a pointer to this interface. Within your implementation of IEdmAddIn5::GetAddInInfo, use this pointer to call:

- [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html) to add menu commands
- [IEdmCmdMgr5::AddToolbarImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddToolbarImage.html) to add toolbar buttons
- [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) to add command hooks

to SOLIDWORKS PDM Professional.

## Accessors

[IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html)

## See Also

[IEdmCmdMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Creating Menu Commands (VB.NET)](vbmenuitem.htm)
[Creating Add-in Hooks (VB.NET)](vbreactor.htm)

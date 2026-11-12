---
title: "IEdmAddInDrawButton5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInDrawButton5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInDrawButton5.html"
---

# IEdmAddInDrawButton5 Interface

Allows you to dynamically draw an add-in toolbar button.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmAddInDrawButton5
```

### C#

```csharp
public interface IEdmAddInDrawButton5
```

### C++/CLI

```cpp
public interface class IEdmAddInDrawButton5
```

## Remarks

This interface inherits from IUnknown. See [Using and Implementing IUnknown (COM)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms693423(v=vs.85).aspx).

To dynamically draw a toolbar button:

1. Create a class that implements both [IEdmAddIn5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html) and IEdmAddInDrawButton5.
2. Implement [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html), calling [IEdmCmdMgr5::AddCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.html) with lEdmMenuFlags setting the [EdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html).EdmMenu_OwnerDrawToolbarButton flag.
3. Implement [IEdmAddInDrawButton5::DrawToolbarButton](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInDrawButton5~DrawToolbarButton.html) to draw a toolbar button when called by SOLIDWORKS PDM Professional.

To draw a fixed toolbar button:

1. Call [IEdmCmdMgr5::AddToolbarImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddToolbarImage.html).
2. Call IEdmCmdMgr5::AddCmd, passing in the toolbar button image ID used in IEdmCmdMgr5::AddToolbarImage.

## See Also

[IEdmAddInDrawButton5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInDrawButton5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

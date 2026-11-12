---
title: "IEdmCmdNode Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdNode"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode.html"
---

# IEdmCmdNode Interface

Allows you to access a file changing state.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCmdNode
```

### C#

```csharp
public interface IEdmCmdNode
```

### C++/CLI

```cpp
public interface class IEdmCmdNode
```

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)
[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

A pointer to this interface is provided by SOLIDWORKS PDM Professional when one of the add-in's hooks or menu commands is executed. [IEdmAddIn5::OnCmd's](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) ppoData ([EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).mpoExtra) contains the pointer to the interface. Within your implementation of IEdmAddIn5::OnCmd, use this pointer to get the properties of the file changing state.

## Accessors

[IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)

## See Also

[IEdmCmdNode Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

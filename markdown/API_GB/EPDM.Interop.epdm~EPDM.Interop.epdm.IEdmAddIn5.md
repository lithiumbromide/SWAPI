---
title: "IEdmAddIn5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddIn5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.html"
---

# IEdmAddIn5 Interface

Allows you to create a SOLIDWORKS PDM Professional add-in.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmAddIn5
```

### C#

```csharp
public interface IEdmAddIn5
```

### C++/CLI

```cpp
public interface class IEdmAddIn5
```

## Examples

See [Add-in Applications](AddInApp.htm).

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)
[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)
[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface inherits from IUnknown. See [Using and Implementing IUnknown (COM)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms693423(v=vs.85).aspx).

To create a SOLIDWORKS PDM Professional add-in:

1. Create a class that implements this interface and its methods.
2. Add menu commands, toolbar buttons, and hooks in your implementation of [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html).
3. Add callbacks for the hooks, menu commands, and toolbar buttons in your implementation of [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html).
4. Register the add-in via the [Administration Add-ins dialog](AdminDlg.htm). During registration, SOLIDWORKS PDM Professional calls your IEdmAddIn5::GetAddInInfo method to obtain information about the add-in.

After the add-in is created and registered, SOLIDWORKS PDM Professional calls your IEdmAddIn5::OnCmd method whenever the user executes a menu command or hook from your add-in.

## See Also

[IEdmAddIn5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmAddInDrawButton5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInDrawButton5.html)

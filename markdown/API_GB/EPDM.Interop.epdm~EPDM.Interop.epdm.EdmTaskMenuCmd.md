---
title: "EdmTaskMenuCmd Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskMenuCmd"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd.html"
---

# EdmTaskMenuCmd Structure

Used by [IEdmTaskProperties::SetMenuCmds](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetMenuCmds.html) when an add-in adds menu commands to launch a task.

## Syntax

### Visual Basic

```vb
Public Structure EdmTaskMenuCmd
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmTaskMenuCmd : System.ValueType
```

### C++/CLI

```cpp
public value class EdmTaskMenuCmd : public System.ValueType
```

## Examples

struct EdmTaskMenuCmd{
integer [mlCmdID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd~mlCmdID.html)
string [mbsMenuString](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd~mbsMenuString.html);
integer [mlEdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd~mlEdmMenuFlags.html);
string [mbsStatusBarHelp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd~mbsStatusBarHelp.html);
};

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)

## See Also

[EdmTaskMenuCmd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskMenuCmd_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Programming Tasks](Tasks.htm)

## Availability

SOLIDWORKS PDM Professional 2010

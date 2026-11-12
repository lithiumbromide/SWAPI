---
title: "IEdmWorkflow6 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html"
---

# IEdmWorkflow6 Interface

Allows you to access a workflow set up using SOLIDWORKS PDM Professional's Workflow Editor.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmWorkflow6
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmWorkflow6 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmWorkflow6 : public IEdmObject5
```

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html) and supersedes [IEdmWorkflow5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5.html).

Use [IEdmWorkflowMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6.html) to enumerate the installed workflows.

## Accessors

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

[IEdmWorkflowMgr6::GetNextWorkflow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetNextWorkflow.html)

## See Also

[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

---
title: "GetFirstWorkflowPosition Method (IEdmWorkflowMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflowMgr6"
member: "GetFirstWorkflowPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetFirstWorkflowPosition.html"
---

# GetFirstWorkflowPosition Method (IEdmWorkflowMgr6)

Starts an enumeration of all the workflows in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstWorkflowPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstWorkflowPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstWorkflowPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first workflow in the enumeration

## Examples

See the [IEdmWorkflowMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6.html) examples.

## Remarks

After calling this method, pass the returned position of the first workflow to [IEdmWorkflowMgr6::GetNextWorkflow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetNextWorkflow.html) to get the first workflow in this list. Then call IEdmWorkflowMgr6::GetNextWorkflow repeatedly to get the rest of the workflows.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmWorkflowMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6.html)
[IEdmWorkflowMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

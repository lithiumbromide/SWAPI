---
title: "GetFirstTransitionPosition Method (IEdmWorkflow6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: "GetFirstTransitionPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetFirstTransitionPosition.html"
---

# GetFirstTransitionPosition Method (IEdmWorkflow6)

Starts an enumeration of the state transitions in this workflow.

## Syntax

### Visual Basic

```vb
Function GetFirstTransitionPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstTransitionPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstTransitionPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first workflow state transition in the enumeration

## Examples

[Graph a Workflow (VB.NET)](Graph_Workflow_Example_VBNET.htm)
[Graph a Workflow (C#)](Graph_Workflow_Example_CSharp.htm)

## Remarks

After calling this method, pass the returned position of the first workflow state transition to [IEdmWorkflow6::GetNextTransition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetNextTransition.html) to get the first workflow state transition in this list. Then call IEdmWorkflow6::GetNextTransition repeatedly to get the rest of the workflow state transitions.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmWorkflow6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)
[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

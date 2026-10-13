---
title: "GetNextWorkflow Method (IEdmWorkflowMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflowMgr6"
member: "GetNextWorkflow"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetNextWorkflow.html"
---

# GetNextWorkflow Method (IEdmWorkflowMgr6)

Gets the next workflow in an enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextWorkflow( _
   ByVal poPos As IEdmPos5 _
) As IEdmWorkflow6
```

### C#

```csharp
IEdmWorkflow6 GetNextWorkflow(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmWorkflow6^ GetNextWorkflow(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next workflow in the list

### Return Value

[IEdmWorkflow6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)

## Examples

See the [IEdmWorkflowMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6.html) examples.

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first workflow in the list, IEdmPos5. Call [IEdmWorkflowMgr6::GetFirstWorkflowPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6~GetFirstWorkflowPosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the workflows in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmWorkflow6.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmWorkflowMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6.html)
[IEdmWorkflowMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflowMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

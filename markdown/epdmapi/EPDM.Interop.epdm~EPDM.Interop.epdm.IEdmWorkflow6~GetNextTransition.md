---
title: "GetNextTransition Method (IEdmWorkflow6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: "GetNextTransition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetNextTransition.html"
---

# GetNextTransition Method (IEdmWorkflow6)

Gets the next workflow state transition in an enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextTransition( _
   ByVal poPos As IEdmPos5 _
) As IEdmTransition6
```

### C#

```csharp
IEdmTransition6 GetNextTransition(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmTransition6^ GetNextTransition(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next workflow state transition in the list

### Return Value

[IEdmTransition6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition6.html)

## Examples

[Graph a Workflow (VB.NET)](Graph_Workflow_Example_VBNET.htm)
[Graph a Workflow (C#)](Graph_Workflow_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first workflow state transition in the list, IEdmPos5. Call [IEdmWorkflow6::GetFirstTransitionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetFirstTransitionPosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the workflow state transitions in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmTransition6.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmWorkflow6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)
[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

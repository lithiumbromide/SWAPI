---
title: "GetAvailableTransitionList Method (IEdmBatchChangeState2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState2"
member: "GetAvailableTransitionList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~GetAvailableTransitionList.html"
---

# GetAvailableTransitionList Method (IEdmBatchChangeState2)

Gets the state transitions available for the files in this batch.

## Syntax

### Visual Basic

```vb
Sub GetAvailableTransitionList( _
   ByRef ppoTransitions As EdmChangeStateTransitionInfo() _
)
```

### C#

```csharp
void GetAvailableTransitionList(
   out EdmChangeStateTransitionInfo[] ppoTransitions
)
```

### C++/CLI

```cpp
void GetAvailableTransitionList(
   [Out] array<EdmChangeStateTransitionInfo> ppoTransitions
)
```

### Parameters

- `ppoTransitions`: Array of [EdmChangeStateTransitionInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo.html) structures; one structure for each state transition

## Examples

See the [IEdmBatchChangeState2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html)
[IEdmBatchChangeState2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2_members.html)

## Availability

SOLIDWORKS PDM Professional 2013

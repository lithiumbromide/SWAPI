---
title: "GetFirstStatePosition Method (IEdmWorkflow6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: "GetFirstStatePosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetFirstStatePosition.html"
---

# GetFirstStatePosition Method (IEdmWorkflow6)

Starts an enumeration of the states in this workflow.

## Syntax

### Visual Basic

```vb
Function GetFirstStatePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstStatePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstStatePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first workflow state in the enumeration

## Examples

See the [IEdmWorkflow6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html) examples.

## Remarks

After calling this method, pass the returned position of the first workflow state to [IEdmWorkflow6::GetNextState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetNextState.html) to get the first workflow state in this list. Then call IEdmWorkflow6::GetNextState repeatedly to get the rest of the workflow states.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmWorkflow6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)
[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

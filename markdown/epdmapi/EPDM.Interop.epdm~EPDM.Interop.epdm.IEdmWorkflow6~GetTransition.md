---
title: "GetTransition Method (IEdmWorkflow6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: "GetTransition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetTransition.html"
---

# GetTransition Method (IEdmWorkflow6)

Gets the workflow state transition with the specified ID.

## Syntax

### Visual Basic

```vb
Function GetTransition( _
   ByVal lTransitionID As System.Integer _
) As IEdmTransition6
```

### C#

```csharp
IEdmTransition6 GetTransition(
   System.int lTransitionID
)
```

### C++/CLI

```cpp
IEdmTransition6^ GetTransition(
   System.int lTransitionID
)
```

### Parameters

- `lTransitionID`: ID of workflow state transition to get

### Return Value

[IEdmTransition6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition6.html)

## Remarks

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmTransition6.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: lTransitionID is invalid.

## See Also

[IEdmWorkflow6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)
[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

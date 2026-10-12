---
title: "GetState Method (IEdmWorkflow6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmWorkflow6"
member: "GetState"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6~GetState.html"
---

# GetState Method (IEdmWorkflow6)

Gets the workflow state with the specified ID or name.

## Syntax

### Visual Basic

```vb
Function GetState( _
   ByRef poIdOrName As System.Object _
) As IEdmState6
```

### C#

```csharp
IEdmState6 GetState(
   ref System.object poIdOrName
)
```

### C++/CLI

```cpp
IEdmState6^ GetState(
   System.Object^% poIdOrName
)
```

### Parameters

- `poIdOrName`: ID or name of workflow state to get

### Return Value

[IEdmState6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState6.html); Null if poIdOrName is invalid

## Remarks

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmState6.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: poIdOrName contains an invalid name.
- E_EDM_INVALID_ID: poIdOrName contain an invalid ID.

## See Also

[IEdmWorkflow6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)
[IEdmWorkflow6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

---
title: "GetRevisionNumberIDFromState Method (IEdmRevisionMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr2"
member: "GetRevisionNumberIDFromState"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberIDFromState.html"
---

# GetRevisionNumberIDFromState Method (IEdmRevisionMgr2)

Gets the ID of the revision number used in the specified workflow state.

## Syntax

### Visual Basic

```vb
Function GetRevisionNumberIDFromState( _
   ByVal lStateID As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetRevisionNumberIDFromState(
   System.int lStateID
)
```

### C++/CLI

```cpp
System.int GetRevisionNumberIDFromState(
   System.int lStateID
)
```

### Parameters

- `lStateID`: ID of workflow state for which to get a revision number (see **Remarks**)

### Return Value

Revision number ID; 0 if no revision number is found for the specified workflow state

## Remarks

Before calling this method, set lStateID using [IEdmState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html).ID.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_WORKFLOW_STATE_ID: The supplied state ID is out of bounds.

## See Also

[IEdmRevisionMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html)
[IEdmRevisionMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03

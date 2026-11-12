---
title: "GetTransition Method (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "GetTransition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetTransition.html"
---

# GetTransition Method (IEdmState5)

Obsolete. Gets a transition from this workflow state by name.

## Syntax

### Visual Basic

```vb
Function GetTransition( _
   ByVal bsName As System.String _
) As IEdmTransition5
```

### C#

```csharp
IEdmTransition5 GetTransition(
   System.string bsName
)
```

### C++/CLI

```cpp
IEdmTransition5^ GetTransition(
   System.String^ bsName
)
```

### Parameters

- `bsName`: Name of transition from this workflow state

### Return Value

[IEdmTransition5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html); Null if no transition for bsName is found

## Remarks

This method is not supported in SOLIDWORKS PDM Professional Version 6.0 and later, because workflows in SOLIDWORKS PDM Professional 6.0 may contain several transitions with the same name. In SOLIDWORKS PDM Professional Version 5.3, the user was forced to create transitions with unique names in the workflow editor. It is, therefore, no longer possible to uniquely identify transitions by name.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmTransition5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The transition is not found.
- E_NOTIMPL: This method is obsolete as of SOLIDWORKS PDM Professional Version 6.0.

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

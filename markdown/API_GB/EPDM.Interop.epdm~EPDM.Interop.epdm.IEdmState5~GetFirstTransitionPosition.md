---
title: "GetFirstTransitionPosition Method (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "GetFirstTransitionPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstTransitionPosition.html"
---

# GetFirstTransitionPosition Method (IEdmState5)

Starts an enumeration of the transitions to and from this workflow state.

## Syntax

### Visual Basic

```vb
Function GetFirstTransitionPosition( _
   Optional ByVal bExitTransitions As System.Boolean _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstTransitionPosition(
   System.bool bExitTransitions
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstTransitionPosition(
   System.bool bExitTransitions
)
```

### Parameters

- `bExitTransitions`: Optionally true to enumerate the transitions from this workflow state, false to enumerate the transition to this workflow state; default is true

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position in the list of the first transition to or from this workflow state (see **Remarks**)

## Examples

[Get File's State Transitions (C#)](Get_Files_State_Transitions_Example_CSharp.htm)
[Get File's State Transitions (VB.NET)](Get_Files_State_Transitions_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first transition to or from this workflow state to [IEdmState5::GetNextTransition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextTransition.html) to get the first transition to or from this workflow state. Then call IEdmState5::GetNextTransition repeatedly to get the rest of the transitions to and from this workflow state.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

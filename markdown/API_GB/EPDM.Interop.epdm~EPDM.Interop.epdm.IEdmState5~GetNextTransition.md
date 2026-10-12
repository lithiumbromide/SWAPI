---
title: "GetNextTransition Method (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "GetNextTransition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextTransition.html"
---

# GetNextTransition Method (IEdmState5)

Gets the next transition to or from this workflow state.

## Syntax

### Visual Basic

```vb
Function GetNextTransition( _
   ByVal poPosition As IEdmPos5 _
) As IEdmTransition5
```

### C#

```csharp
IEdmTransition5 GetNextTransition(
   IEdmPos5 poPosition
)
```

### C++/CLI

```cpp
IEdmTransition5^ GetNextTransition(
   IEdmPos5^ poPosition
)
```

### Parameters

- `poPosition`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next transition to or from this workflow state (see **Remarks**)

### Return Value

[IEdmTransition5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)

## Examples

[Get File's State Transitions (C#)](Get_Files_State_Transitions_Example_CSharp.htm)
[Get File's State Transitions (VB.NET)](Get_Files_State_Transitions_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPosition with the interface to the position of the first transition to this workflow state, IEdmPos5. Call [IEdmState5::GetFirstTransitionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstTransitionPosition.html) to start an enumeration and obtain [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html), the position of the first transition.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the transitions to this workflow state.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers must free the interface returned, IEdmFile5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

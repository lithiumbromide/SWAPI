---
title: "FromState Property (IEdmTransition5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition5"
member: "FromState"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5~FromState.html"
---

# FromState Property (IEdmTransition5)

Gets the source state of this transition.

## Syntax

### Visual Basic

```vb
ReadOnly Property FromState As IEdmState5
```

### C#

```csharp
IEdmState5 FromState {get;}
```

### C++/CLI

```cpp
property IEdmState5^ FromState {
   IEdmState5^ get();
}
```

### Property Value

[IEdmState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html); Null if no source state exists (see **Remarks**)

## Remarks

A SOLIDWORKS PDM Professional workflow contains one transition, called AddedToFileVault, without a source state. In SOLIDWORKS PDM Professional 5.2, trying to access the FromState property of the AddedToFileVault transition results in an exception with the error code E_EDM_STATE_NOT_FOUND. In SOLIDWORKS PDM Professional 5.3 and later, the FromState property can be read without exception from the AddedToFileVault transition.

## See Also

[IEdmTransition5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)
[IEdmTransition5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

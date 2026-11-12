---
title: "Authentication Property (IEdmTransition10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition10"
member: "Authentication"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10~Authentication.html"
---

# Authentication Property (IEdmTransition10)

Gets whether this workflow transition requires a password.

## Syntax

### Visual Basic

```vb
ReadOnly Property Authentication As System.Boolean
```

### C#

```csharp
System.bool Authentication {get;}
```

### C++/CLI

```cpp
property System.bool Authentication {
   System.bool get();
}
```

### Property Value

True if this workflow transition requires a password, false if not

## Examples

See the [IEdmTransition10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10.html) examples.

## Remarks

This property corresponds to the **Authentication** check box in the Properties dialog of a transition.

## See Also

[IEdmTransition10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10.html)
[IEdmTransition10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10_members.html)
[IEdmBatchChangeState4::ChangeState2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4~ChangeState2.html)
[IEdmFile10::ChangeState2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10~ChangeState2.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP02

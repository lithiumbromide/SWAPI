---
title: "WorkflowID Property (IEdmTransition6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition6"
member: "WorkflowID"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition6~WorkflowID.html"
---

# WorkflowID Property (IEdmTransition6)

Gets the ID of the workflow to which this transition belongs.

## Syntax

### Visual Basic

```vb
ReadOnly Property WorkflowID As System.Integer
```

### C#

```csharp
System.int WorkflowID {get;}
```

### C++/CLI

```cpp
property System.int WorkflowID {
   System.int get();
}
```

### Property Value

ID of [IEdmWorkflow6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow6.html)

## Remarks

To obtain IEdmWorkflow6, call [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) with lObjectID set to this property.

## See Also

[IEdmTransition6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition6.html)
[IEdmTransition6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

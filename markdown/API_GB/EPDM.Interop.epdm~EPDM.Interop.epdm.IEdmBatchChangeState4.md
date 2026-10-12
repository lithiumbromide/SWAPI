---
title: "IEdmBatchChangeState4 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState4"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html"
---

# IEdmBatchChangeState4 Interface

Allows you to change states or revoke transitions of several files all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchChangeState4
   Inherits IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3
```

### C#

```csharp
public interface IEdmBatchChangeState4 : IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3
```

### C++/CLI

```cpp
public interface class IEdmBatchChangeState4 : public IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3
```

## Examples

[Batch Change States of Files (VB.NET)](Batch_Change_States_of_Files_Example_VBNET.htm)
[Batch Change States of Files (C#)](Batch_Change_States_of_Files_Example_CSharp.htm)

## Remarks

This interface:

- extends [IEdmBatchChangeState3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3.html) by supporting password-protected workflow transitions.
- is extended by [IEdmBatchChangeState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5.html).

## See Also

[IEdmBatchChangeState4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

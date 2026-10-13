---
title: "IEdmBatchChangeState5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5.html"
---

# IEdmBatchChangeState5 Interface

Allows you to change states or revoke transitions of several files all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchChangeState5
   Inherits IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3, IEdmBatchChangeState4
```

### C#

```csharp
public interface IEdmBatchChangeState5 : IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3, IEdmBatchChangeState4
```

### C++/CLI

```cpp
public interface class IEdmBatchChangeState5 : public IEdmBatchChangeState, IEdmBatchChangeState2, IEdmBatchChangeState3, IEdmBatchChangeState4
```

## Remarks

This interface:

- extends [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) by allowing users to include parent files in the [file reference tree to revoke transactions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html).
- is extended by [IEdmBatchChangeState6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6.html).

## See Also

[IEdmBatchChangeState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

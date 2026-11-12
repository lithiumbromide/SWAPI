---
title: "IEdmBatchDelete3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3.html"
---

# IEdmBatchDelete3 Interface

Allows you to delete several files and folders from the vault all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchDelete3
   Inherits IEdmBatchDelete, IEdmBatchDelete2
```

### C#

```csharp
public interface IEdmBatchDelete3 : IEdmBatchDelete, IEdmBatchDelete2
```

### C++/CLI

```cpp
public interface class IEdmBatchDelete3 : public IEdmBatchDelete, IEdmBatchDelete2
```

## Remarks

This interface extends [IEdmBatchDelete2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2.html) by adding [IEdmBatchDelete3::GetCommitErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3~GetCommitErrors.html) which shows the errors that occurred during [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html).

## See Also

[IEdmBatchDelete3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

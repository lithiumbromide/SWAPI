---
title: "IEdmBatchDelete2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete2"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2.html"
---

# IEdmBatchDelete2 Interface

Allows you to delete several files and folders from the vault at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchDelete2
   Inherits IEdmBatchDelete
```

### C#

```csharp
public interface IEdmBatchDelete2 : IEdmBatchDelete
```

### C++/CLI

```cpp
public interface class IEdmBatchDelete2 : public IEdmBatchDelete
```

## Remarks

This interface:

- extends [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) by providing the option to show deleted objects in the trash can in [IEdmBatchDelete2::ShowWarningDlg2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2~ShowWarningDlg2.html).
- is extended by [IEdmBatchDelete3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3.html).

## See Also

[IEdmBatchDelete2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

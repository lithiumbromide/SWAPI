---
title: "IEdmBatchChangeState Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html"
---

# IEdmBatchChangeState Interface

Allows you to change states or revoke transitions of several files at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchChangeState
```

### C#

```csharp
public interface IEdmBatchChangeState
```

### C++/CLI

```cpp
public interface class IEdmBatchChangeState
```

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchChangeState2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html).

To change the states of files:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchChangeState as a parameter.
2. Call [IEdmBatchChangeState::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~AddFile.html) to add a file to the batch of files whose states you want to change.
3. Call [IEdmBatchChangeState::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~CreateTree.html) to build the initial file reference tree.
4. Optionally call [IEdmBatchChangeState::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ShowDlg.html) to show a dialog with the affected files.
5. Call [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html) to change the states of the files added to the batch.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

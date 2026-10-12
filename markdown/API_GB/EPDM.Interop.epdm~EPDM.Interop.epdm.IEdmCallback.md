---
title: "IEdmCallback Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html"
---

# IEdmCallback Interface

Monitors the progress of a supported API operation.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmCallback
```

### C#

```csharp
public interface IEdmCallback
```

### C++/CLI

```cpp
public interface class IEdmCallback
```

## Examples

[Create Card View (VB.NET)](Create_Card_View_Example_VBNET.htm)
[Create Card View (C#)](Create_Card_View_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

This callback interface works only with API methods that provide a poCallback argument. For example:

- [IEdmFolder5::CreateCardView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateCardView.html)
- [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html)
- [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html)
- [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html)
- [IEdmBatchUpdate2::CommitUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~CommitUpdate.html)
- [IEdmClearLocalCache::CommitClear](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmClearLocalCache~CommitClear.html)
- [IEdmUserMgr8::CreateUserPicture](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~CreateUserPicture.html)
- [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html)
- [IEdmVault11::CreateNewVault](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVault.html)

To use this interface:

1. Create a new class.
2. Implement all of the methods of IEdmCallback in the new class.
3. Call one of the API methods whose progress you want to monitor, setting its poCallback argument to a pointer to the new class.

## See Also

[IEdmCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmFolder5::CreateCardView Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateCardView.html)
[IEdmEnumeratorVariable5::StoreValuesFromDatabase Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~StoreValuesFromDatabase.html)

---
title: "IEdmHistoryUpdate Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistoryUpdate"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate.html"
---

# IEdmHistoryUpdate Interface

Allows you to access the version and revision comments of files.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmHistoryUpdate
```

### C#

```csharp
public interface IEdmHistoryUpdate
```

### C++/CLI

```cpp
public interface class IEdmHistoryUpdate
```

## Examples

[Get Histories of Files (VB.NET)](Get_Histories_of_Files_Example_VBNET.htm)
[Get Histories of Files (C#)](Get_Histories_of_Files_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To use this interface:

1. Access this interface by calling IEdmVault7::CreateUtility with eType set to [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_HistoryUpdate.
2. Call [IEdmHistoryUpdate::UpdateRevisionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateRevisionComment.html) one or more times to add revision comments to the batch.
3. Call [IEdmHistoryUpdate::UpdateVersionComment](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~UpdateVersionComment.html) one or more times to add version comments to the batch.
4. Call [IEdmHistoryUpdate::CommitUpdates](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate~CommitUpdates.html) to commit the batch of changes to the database.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmHistoryUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistoryUpdate_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

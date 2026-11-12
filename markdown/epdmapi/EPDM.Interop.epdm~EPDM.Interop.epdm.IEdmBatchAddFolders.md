---
title: "IEdmBatchAddFolders Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAddFolders"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html"
---

# IEdmBatchAddFolders Interface

Allows you to add several folders to the vault all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchAddFolders
```

### C#

```csharp
public interface IEdmBatchAddFolders
```

### C++/CLI

```cpp
public interface class IEdmBatchAddFolders
```

## Examples

[Batch Add Folders (VB.NET)](Batch_Add_Folders_Example_VBNET.htm)
[Batch Add Folders (C#)](Batch_Add_Folders_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To add several folders to the vault in one batch:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchAddFolders as a parameter.
2. Call [IEdmBatchAddFolders::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html) once for each folder to add to the batch.
3. Call [IEdmBatchAddFolders::Create](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html) to commit the folders in the batch to the vault.

Using IEdmBatchAddFolders is more efficient than calling [IEdmFolder5::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFolder.html) or [IEdmFolder5::CreateFolderPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateFolderPath.html) multiple times.

Use [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html) if you need to add several files and folders to the vault.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchAddFolders Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

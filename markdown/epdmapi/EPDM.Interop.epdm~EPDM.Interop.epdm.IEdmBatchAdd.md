---
title: "IEdmBatchAdd Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html"
---

# IEdmBatchAdd Interface

Allows you to add several files and folders to the vault at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchAdd
```

### C#

```csharp
public interface IEdmBatchAdd
```

### C++/CLI

```cpp
public interface class IEdmBatchAdd
```

## Examples

[Batch Add Files and Folders to Vault (VB.NET)](Batch_Add_Files_and_Folders_Example_VBNET.htm)
[Batch Add Files and Folders to Vault (C#)](Batch_Add_Files_and_Folders_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchAdd2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd2.html).

Using IEdmBatchAdd is more efficient than calling [IEdmFolder5::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFile.html) or [IEdmFolder5::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFolder.html) multiple times.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchAdd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmBatchAddFolders Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html)

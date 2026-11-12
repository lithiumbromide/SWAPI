---
title: "IEdmBatchGet Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html"
---

# IEdmBatchGet Interface

Allows you to get several files from the vault all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchGet
```

### C#

```csharp
public interface IEdmBatchGet
```

### C++/CLI

```cpp
public interface class IEdmBatchGet
```

## Examples

[Batch Check Out Files (VB.NET)](Batch_Get_Files_Example_VBNET.htm)
[Batch Check Out Files (C#)](Batch_Get_Files_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

To get several files at once:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchGet as a parameter.
2. Call [IEdmBatchGet::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelection.html) or [IEdmBatchGet::AddSelectionEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~AddSelectionEx.html) at least once.
3. Call [IEdmBatchGet::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~CreateTree.html) to compute the file reference tree and specify get and check-out options.
4. Optionally call [IEdmBatchGet::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~ShowDlg.html) to display the Get or Check Out dialog box.
5. Call [IEdmBatchGet::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFiles.html) to get the files.

Using this interface is more efficient than calling [IEdmFile5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html) and [IEdmFile5::LockFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.html) for each file that you want to check out.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

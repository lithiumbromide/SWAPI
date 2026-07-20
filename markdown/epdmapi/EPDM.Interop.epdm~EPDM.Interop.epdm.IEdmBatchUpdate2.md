---
title: "IEdmBatchUpdate2 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate2"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html"
---

# IEdmBatchUpdate2 Interface

Allows you to set the values of several file and folder card variables all at once.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchUpdate2
```

### C#

```csharp
public interface IEdmBatchUpdate2
```

### C++/CLI

```cpp
public interface class IEdmBatchUpdate2
```

## Examples

[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)

[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See

  [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx)

  .
- supersedes IEdmBatchUpdate, which can only update file variables.

To set the values of file and folder card variables:

1. Access this interface by calling

  [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

  , passing in

  [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html)

  .EdmUtil_BatchUpdate.
2. Call

  [IEdmBatchUpdate2::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetVar.html)

  once for each file card variable you want to update. You must first check out the files whose card variables you want to update.
3. Call

  [IEdmBatchUpdate2::SetFolderVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetFolderVar.html)

  once for each folder card variable you want to update.
4. Call

  [IEdmBatchUpdate2::CommitUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~CommitUpdate.html)

  to commit all of the file and folder card variable changes.

Prior to SOLIDWORKS PDM Professional 6.2, the only way to set file card variables was to use[IEdmEnumeratorVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html), which can handle only one file or folder card variable at a time. As of SOLIDWORKS PDM Professional 6.2, you should use IEdmBatchUpdate2, which can handle several file and folder card variables at a time.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchUpdate2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

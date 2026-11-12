---
title: "IEdmBatchUnlock Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html"
---

# IEdmBatchUnlock Interface

Allows you to unlock, check in, or undo check-outs of multiple files all at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchUnlock
```

### C#

```csharp
public interface IEdmBatchUnlock
```

### C++/CLI

```cpp
public interface class IEdmBatchUnlock
```

## Examples

[Batch Check In Files (C#)](Batch_Unlock_Files_Example_CSharp.htm)
[Batch Check In Files (VB.NET)](Batch_Unlock_Files_Example_VBNET.htm)
[Access Check-in Flags in Check out Dialog (C#)](Access_Check-in_Flags_in_Check_in_Dialog_Example_CSharp.htm)
[Access Check-in Flags in Check out Dialog (VB.NET)](Access_Check-in_Flags_in_Check_in_Dialog_Example_VBNET.htm)
[Prevent Admin from Checking In File (C#)](Prevent_Admin_from_Checking_In_File_Example_CSharp.htm)
[Prevent Admin from Checking In File (VB.NET)](Prevent_Admin_from_Checking_In_File_Example_VBNET.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchUnlock2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2.html).

To unlock, check in, or undo the check-outs of multiple files in one batch:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing in [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchUnlock.
2. Call [IEdmBatchUnlock::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~AddSelection.html) to specify the files to unlock.
3. Call [IEdmBatchUnlock::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~CreateTree.html) to create the file reference tree.
4. Optionally call [IEdmBatchUnlock::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~ShowDlg.html) to display the SOLIDWORKS PDM Professional Check In or Undo Check Out dialog box.
5. Call [IEdmBatchUnlock::GetFileList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~GetFileList.html) to get the files affected by the unlock operation.
6. Call [IEdmBatchUnlock::UnlockFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~UnlockFiles.html) to perform the batch unlock operation.

Using this interface to unlock, check in, or undo check-outs is more efficient than calling [IEdmFile5::UnlockFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.html) or [IEdmFile5::UndoLockFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UndoLockFile.html) for each file.

You can obtain an [IEdmRefItemContainer](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItemContainer.html) interface from IEdmBatchUnlock by assignment (QueryInterface in C++).

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchUnlock Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

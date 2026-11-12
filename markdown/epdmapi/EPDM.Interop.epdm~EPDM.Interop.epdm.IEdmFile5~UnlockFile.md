---
title: "UnlockFile Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "UnlockFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.html"
---

# UnlockFile Method (IEdmFile5)

Checks in this file.

## Syntax

### Visual Basic

```vb
Sub UnlockFile( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsComment As System.String, _
   Optional ByVal lEdmUnlockFlags As System.Integer, _
   Optional ByVal poIEdmRefCallback As System.Object _
)
```

### C#

```csharp
void UnlockFile(
   System.int lParentWnd,
   System.string bsComment,
   System.int lEdmUnlockFlags,
   System.object poIEdmRefCallback
)
```

### C++/CLI

```cpp
void UnlockFile(
   System.int lParentWnd,
   System.String^ bsComment,
   System.int lEdmUnlockFlags,
   System.Object^ poIEdmRefCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsComment`: Version comment to show in the history dialog box
- `lEdmUnlockFlags`: Optional combination of [EdmUnlockFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockFlag.html) bits; default is EdmUnlockFlag.EdmUnlock_Simple
- `poIEdmRefCallback`: Optional Nothing or null

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

If the file or its file data card contents have changed, this method creates a new version.

[IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) is more efficient than this interface for checking in multiple files.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: The method successfully executed, but as no file is modified, SOLIDWORKS PDM Professional did not create a new version.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out by the logged-in user.
- E_EDM_LOCKED_ON_OTHER_COMPUTER: The file is not checked out on the client machine where you tried to check it in.
- E_EDM_FILE_NOT_FOUND: The file is not part of the vault.
- E_EDM_LOCAL_FILE_NOT_FOUND: There is no copy of the file in the cache folder on the client machine.
- E_EDM_FILE_SHARE_ERROR: The file is open exclusively in another program.
- E_EDM_CANCELLED_BY_USER: Not implemented.
- E_EDM_INVALID_FILE: The file format is not recognized, and you have specified to not check in such files.
- E_EDM_MISSING_MANDATORY_VALUE: The file lacks a value for a required file data card variable.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the loaded [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreUndoLock hooks did not permit the operation.
- E_EDM_FILE_NOT_REGENERATED: The file needs to be rebuilt.
- E_EDM_NO_WORKFLOW: The document does not meet the conditions of any workflow.
- E_EDM_CIRCULAR_XREF: A cyclic file reference was detected.
- E_EDM_SWDRW_SETTO_USE_INDEPENDENT_REV_TABLE: An independent type revision setting is used in the drawing.
- E_EDM_NO_DOCTYPE: The document does not meet the conditions of any category.
- E_EDM_LOCKED_IN_OTHER_FOLDER: The file is checked out in another folder.
- E_EDM_FILE_NAME_NOT_GLOBALLY_UNIQUE: The file name is not unique.
- E_EDM_TOOLBOX_FILE_LOCATED_IN_NONTOOLBOX_FOLDER: Toolbox file must be located in a Toolbox folder.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::LockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

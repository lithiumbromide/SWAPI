---
title: "EdmFileInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFileInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo.html"
---

# EdmFileInfo Structure

Information about a file or folder that is added to the vault.

## Syntax

### Visual Basic

```vb
Public Structure EdmFileInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmFileInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmFileInfo : public System.ValueType
```

## Examples

struct EdmFileInfo{
integer [mlArg](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mlArg.html);
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mlFolderID.html);
integer [mhResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mhResult.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mbsPath.html);
IEdmObject5* [mpoObject](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo~mpoObject.html);
};

## Examples

[Destroy Deleted Files in Vault (C#)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)
[Destroy Deleted Files in Vault (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)

## Remarks

Returned by [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html). One structure is returned for each file or folder added to the batch using one of the [IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)::AddXxxxx methods.

## See Also

[EdmFileInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional

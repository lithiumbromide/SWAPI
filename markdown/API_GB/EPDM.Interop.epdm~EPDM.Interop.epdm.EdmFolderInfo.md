---
title: "EdmFolderInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFolderInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo.html"
---

# EdmFolderInfo Structure

Information about a folder that is added to the vault.

## Syntax

### Visual Basic

```vb
Public Structure EdmFolderInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmFolderInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmFolderInfo : public System.ValueType
```

## Examples

struct EdmFolderInfo{
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mlFolderID.html);
string [mbsPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mbsPath.html);
integer [mlParam](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mlParam.html);
integer [mlEdmFolderInfoFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mlEdmFolderInfoFlags.html);
[IEdmFolder6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html)* [mpoFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo~mpoFolder.html);
};

## Examples

[Batch Add Folders (VB.NET)](Batch_Add_Folders_Example_VBNET.htm)
[Batch Add Folders (C#)](Batch_Add_Folders_Example_CSharp.htm)

## Remarks

Returned by [IEdmBatchAddFolders::Create](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html). One structure is returned for each folder added to the batch using [IEdmBatchAddFolders::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html).

## See Also

[EdmFolderInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional

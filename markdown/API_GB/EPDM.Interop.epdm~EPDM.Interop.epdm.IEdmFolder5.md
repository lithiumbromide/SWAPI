---
title: "IEdmFolder5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html"
---

# IEdmFolder5 Interface

Allows you to access the contents of a file system folder in the vault.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFolder5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmFolder5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFolder5 : public IEdmObject5
```

## Examples

[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)
[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)
[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmFolder6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html), which provides the ability to add files to a folder, move a folder, and rename a folder.

Use this interface to enumerate the files and subfolders of a folder.

Access the contents of a folder's data card by assigning an [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html) pointer to an IEdmFolder5 object.

To update multiple folder data cards, use [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html) which is more efficient than updating each folder data card using this interface.

## Accessors

[IEdmFile5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html)

[IEdmFile5::LockedInFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockedInFolder.html)

[IEdmFolder5::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFolder.html)

[IEdmFolder5::CreateFolderPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateFolderPath.html)

[IEdmFolder5::GetNextSubFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextSubFolder.html)

[IEdmFolder5::GetSubFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetSubFolder.html)

[IEdmFolder5::ParentFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~ParentFolder.html)

[IEdmLabel5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolder.html)

[IEdmReference5::Folder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~Folder.html)

[IEdmReference5::LockedInFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~LockedInFolder.html)

[IEdmVault5::BrowseForFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~BrowseForFolder.html)

[IEdmVault5::GetFileFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html)

[IEdmVault5::GetFolderFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFolderFromPath.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

[IEdmVault5::GetFileFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html)

[IEdmVault5::GetFolderFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFolderFromPath.html)

[IEdmVault5::RootFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~RootFolder.html)

## See Also

[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

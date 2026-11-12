---
title: "SetSearchFolders Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetSearchFolders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.html"
---

# SetSearchFolders Method (ISldWorks)

Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSearchFolders( _
   ByVal FolderType As System.Integer, _
   ByVal Folders As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FolderType As System.Integer
Dim Folders As System.String
Dim value As System.Boolean

value = instance.SetSearchFolders(FolderType, Folders)
```

### C#

```csharp
System.bool SetSearchFolders(
   System.int FolderType,
   System.string Folders
)
```

### C++/CLI

```cpp
System.bool SetSearchFolders(
   System.int FolderType,
   System.String^ Folders
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FolderType`: The search folder type; the only type currently supported is swDocumentType; for an up-to-date listing, see [swSearchFolderTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSearchFolderTypes_e.html)
- `Folders`: String containing all of the search folders; each search folder should be separated by a semicolon

### Return Value

True if the search folders were set, false if not

## VBA Syntax

See [SldWorks::SetSearchFolders](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetSearchFolders.html).

## Examples

[Get and Set Search Folders (VBA)](Get_and_Set_Search_Folders_Example_VB.htm)
[Get and Set Search Folders (VB.NET)](Get_and_Set_Search_Folders_Example_VBNET.htm)
[Get and Set Search Folders (C#)](Get_and_Set_Search_Folders_Example_CSharp.htm)

## Remarks

The search folders are used by SOLIDWORKS based on their order. Folders at the top of the list get searched first and folders at the bottom of the list get searched last.

This method does not allow you to incrementally add to the search folders list. Calling this method overwrites the existing search folder settings. If you want to add a folder to the existing search folder list, you must get the current search folder list using [ISldWorks::GetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSearchFolders.html) and then add your folder string at the appropriate location.

Search folder settings are ignored unless **Tools > Options > System Options > External References >** Search file locations for external references is selected. To get and set Search file locations for external references in the SOLIDWORKS API, use [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swUseFolderSearchRules with [ISldWorks::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) and [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html), respectively.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.html)
[ISldWorks::SetMissingReferencePathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.html)
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.html)

---
title: "GetSearchFolders Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetSearchFolders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.html"
---

# GetSearchFolders Method (ISldWorks)

Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchFolders( _
   ByVal FolderType As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FolderType As System.Integer
Dim value As System.String

value = instance.GetSearchFolders(FolderType)
```

### C#

```csharp
System.string GetSearchFolders(
   System.int FolderType
)
```

### C++/CLI

```cpp
System.String^ GetSearchFolders(
   System.int FolderType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FolderType`: Search folder type; the only type supported is swDocumentType; for an up-to-date listing, see [swSearchFolderTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSearchFolderTypes_e.html)

### Return Value

String containing all of the search folders; each search folder is separated by a semicolon

## VBA Syntax

See [SldWorks::GetSearchFolders](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetSearchFolders.html).

## Examples

[Get and Set Search Folders (VBA)](Get_and_Set_Search_Folders_Example_VB.htm)
[Get and Set Search Folders (VB.NET)](Get_and_Set_Search_Folders_Example_VBNET.htm)
[Get and Set Search Folders (C#)](Get_and_Set_Search_Folders_Example_CSharp.htm)

## Remarks

Search folder settings are ignored unless **Tools > Options > System Options > External References >** Search file locations for external references is selected. To get and set Search file locations for external references in the SOLIDWORKS API, use [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swUseFolderSearchRules with [ISldWorks::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) and [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html), respectively.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::SetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSearchFolders.html)
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.html)
[ISldWorks::SetMissingReferencePathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.html)

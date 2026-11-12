---
title: "GetSheetMetalFolder Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetSheetMetalFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetSheetMetalFolder.html"
---

# GetSheetMetalFolder Method (IFeatureManager)

Gets the interface to the sheet metal folder feature in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetMetalFolder() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.GetSheetMetalFolder()
```

### C#

```csharp
System.object GetSheetMetalFolder()
```

### C++/CLI

```cpp
System.Object^ GetSheetMetalFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISheetMetalFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFolder.html)

## VBA Syntax

See [FeatureManager::GetSheetMetalFolder](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetSheetMetalFolder.html).

## Examples

[Get Sheet Metal Folder Feature (VBA)](Get_Sheet_Metal_Folder_Feature_Example_VB.htm)
[Get Sheet Metal Folder Feature (VB.NET)](Get_Sheet_Metal_Folder_Feature_Example_VBNET.htm)
[Get Sheet Metal Folder Feature (C#)](Get_Sheet_Metal_Folder_Feature_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

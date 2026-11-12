---
title: "GetFlatPatternFolder Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetFlatPatternFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFlatPatternFolder.html"
---

# GetFlatPatternFolder Method (IFeatureManager)

Gets the interface to the flat-pattern folder feature in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlatPatternFolder() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.GetFlatPatternFolder()
```

### C#

```csharp
System.object GetFlatPatternFolder()
```

### C++/CLI

```cpp
System.Object^ GetFlatPatternFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFlatPatternFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFolder.html)

## VBA Syntax

See [FeatureManager::GetFlatPatternFolder](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetFlatPatternFolder.html).

## Examples

[Get Flat-Pattern Folder Feature (VBA)](Get_Flat_Pattern_Folder_Feature_Example_VB.htm)
[Get Flat-Pattern Folder Feature (VB.NET)](Get_Flat_Pattern_Folder_Feature_Example_VBNET.htm)
[Get Flat-Pattern Folder Feature (C#)](Get_Flat_Pattern_Folder_Feature_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

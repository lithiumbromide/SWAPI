---
title: "IFlatPatternFolder Interface"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFolder"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder.html"
---

# IFlatPatternFolder Interface

Allows access to the flat-pattern folder in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IFlatPatternFolder
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFolder
```

### C#

```csharp
public interface IFlatPatternFolder
```

### C++/CLI

```cpp
public interface class IFlatPatternFolder
```

## VBA Syntax

See [FlatPatternFolder](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFolder.html).

## Examples

[Get Flat-Pattern Folder Feature (VBA)](Get_Flat_Pattern_Folder_Feature_Example_VB.htm)
[Get Flat-Pattern Folder Feature (VB.NET)](Get_Flat_Pattern_Folder_Feature_Example_VBNET.htm)
[Get Flat-Pattern Folder Feature (C#)](Get_Flat_Pattern_Folder_Feature_Example_CSharp.htm)

## Remarks

The FeatureManager design tree of a multi-body sheet metal part created in SOLIDWORKS 2013 and later contains a flat-pattern folder with multiple flat-pattern features. This interface allows access to the flat-pattern folder.

## Accessors

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IFeatureManager::GetFlatPatternFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFlatPatternFolder.html)

## Access Diagram

[FlatPatternFolder](SWObjectModel.pdf#FlatPatternFolder)

## See Also

[IFlatPatternFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

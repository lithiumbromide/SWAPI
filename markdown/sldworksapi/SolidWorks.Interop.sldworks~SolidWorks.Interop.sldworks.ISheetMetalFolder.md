---
title: "ISheetMetalFolder Interface"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFolder"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder.html"
---

# ISheetMetalFolder Interface

Allows access to a sheet metal folder feature in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISheetMetalFolder
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFolder
```

### C#

```csharp
public interface ISheetMetalFolder
```

### C++/CLI

```cpp
public interface class ISheetMetalFolder
```

## VBA Syntax

See [SheetMetalFolder](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFolder.html).

## Examples

[Get Sheet Metal Folder Feature (VBA)](Get_Sheet_Metal_Folder_Feature_Example_VB.htm)
[Get Sheet Metal Folder Feature (VB.NET)](Get_Sheet_Metal_Folder_Feature_Example_VBNET.htm)
[Get Sheet Metal Folder Feature (C#)](Get_Sheet_Metal_Folder_Feature_Example_CSharp.htm)

## Remarks

The FeatureManager design tree of a multi-body sheet metal part created in SOLIDWORKS 2013 and later contains a sheet metal folder with multiple sheet metal features. This interface allows access to the sheet metal folder.

## Accessors

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IFeatureManager::GetSheetMetalFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetSheetMetalFolder.html)

## Access Diagram

[SheetMetalFolder](SWObjectModel.pdf#SheetMetalFolder)

## See Also

[ISheetMetalFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

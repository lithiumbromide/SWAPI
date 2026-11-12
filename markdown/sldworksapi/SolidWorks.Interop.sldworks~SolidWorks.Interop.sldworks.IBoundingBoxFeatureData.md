---
title: "IBoundingBoxFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html"
---

# IBoundingBoxFeatureData Interface

Allows access to a bounding box feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBoundingBoxFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
```

### C#

```csharp
public interface IBoundingBoxFeatureData
```

### C++/CLI

```cpp
public interface class IBoundingBoxFeatureData
```

## VBA Syntax

See [BoundingBoxFeatureData](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData.html).

## Examples

[Create Bounding Box (VBA)](Create_Bounding_Box_Example_VB.htm)
[Create Bounding Box (C#)](Create_Bounding_Box_Example_CSharp.htm)

## Remarks

Use [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.html) to clear the selection made when the bounding box feature is created.

To display or hide the bounding box sketch, call [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) to set [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swViewDispGlobalBBox to true or false, respectively.

For more information about the properties of this feature, see **SOLIDWORKS web help > Parts and Features > Reference Geometry > Bounding Boxes > Bounding Box PropertyManager**.

## Accessors

[IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[BoundingBoxFeatureData](SWObjectModel.pdf#BoundingBoxFeatureData)

## See Also

[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::GetSphericalBoxDiameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSphericalBoxDiameter.html)

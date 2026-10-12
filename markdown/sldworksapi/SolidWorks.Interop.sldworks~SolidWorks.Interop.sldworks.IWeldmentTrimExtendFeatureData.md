---
title: "IWeldmentTrimExtendFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html"
---

# IWeldmentTrimExtendFeatureData Interface

Allows access to the data that defines a weldment trim extend feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IWeldmentTrimExtendFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
```

### C#

```csharp
public interface IWeldmentTrimExtendFeatureData
```

### C++/CLI

```cpp
public interface class IWeldmentTrimExtendFeatureData
```

## VBA Syntax

See [WeldmentTrimExtendFeatureData](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData.html).

## Examples

[Get Weldment Trim Extend Corner Type (VBA)](Get_Weldment_Trim_Extend_Corner_Type_Example_VB.htm)
[Get Weldment Trim Extend Corner Type (VB.NET)](Get_Weldment_Trim_Extend_Corner_Type_Example_VBNET.htm)
[Get Weldment Trim Extend Corner Type (C#)](Get_Weldment_Trim_Extend_Corner_Type_Example_CSharp.htm)

## Remarks

Only bodies created by weldment features can be trimmed and extended. Only End Trim corner types can have multiple target and boundary bodies to trim. All other corner types can have only one target and boundary body to trim. For all other corner types, first valid body specified is used if more than one body is specified.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[WeldmentTrimExtendFeatureData](SWObjectModel.pdf#WeldmentTrimExtendFeatureData)

## See Also

[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertWeldmentTrimFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.html)
[IFeatureManager::InsertWeldmentTrimFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.html)

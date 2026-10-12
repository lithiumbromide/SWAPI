---
title: "IMirrorSolidFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html"
---

# IMirrorSolidFeatureData Interface

Allows access to a mirror solid feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMirrorSolidFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
```

### C#

```csharp
public interface IMirrorSolidFeatureData
```

### C++/CLI

```cpp
public interface class IMirrorSolidFeatureData
```

## VBA Syntax

See [MirrorSolidFeatureData](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## Remarks

After creating the mirror solid feature, use [IMirrorSolidFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~StructureSystemToPatternArray.html) to change the structure system to mirror.

For more information see the **Mirror Feature PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[MirrorSolidFeatureData](SWObjectModel.pdf#MirrorSolidFeatureData)

## See Also

[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html)
[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)

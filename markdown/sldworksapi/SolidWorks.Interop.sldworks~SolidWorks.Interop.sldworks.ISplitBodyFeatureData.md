---
title: "ISplitBodyFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html"
---

# ISplitBodyFeatureData Interface

Allows access to a Split feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISplitBodyFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
```

### C#

```csharp
public interface ISplitBodyFeatureData
```

### C++/CLI

```cpp
public interface class ISplitBodyFeatureData
```

## VBA Syntax

See [SplitBodyFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData.html).

## Examples

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

## Remarks

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either [IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html) or the **Split** feature in the user interface. You can access a split-body feature's data using the ISplitBodyFeatureData interface.
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

## Access Diagram

[SplitBodyFeatureData](SWObjectModel.pdf#SplitBodyFeatureData)

## See Also

[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.html)

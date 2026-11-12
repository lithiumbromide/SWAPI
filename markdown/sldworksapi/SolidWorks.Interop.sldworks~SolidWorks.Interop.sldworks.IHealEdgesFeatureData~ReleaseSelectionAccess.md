---
title: "ReleaseSelectionAccess Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IHealEdgesFeatureData)

Releases access to the selections that describe this heal edges feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [HealEdgesFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## Remarks

[IHealEdgesFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHealEdgesFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define the heal edges feature.

Use this method to restore the rollback state if you did not modify the fill-surface feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the heal edges feature.

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

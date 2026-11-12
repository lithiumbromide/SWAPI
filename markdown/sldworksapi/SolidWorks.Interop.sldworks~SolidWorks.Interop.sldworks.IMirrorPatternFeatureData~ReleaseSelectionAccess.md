---
title: "ReleaseSelectionAccess Method (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IMirrorPatternFeatureData)

Releases access to the selections used to define the mirror pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData

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

See [MirrorPatternFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

## Remarks

[IMirrorPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPatternFeatureData~AccessSelections.html) and [IMirrorPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPatternFeatureData~IAccessSelections2.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2000 SP2, Revision Number 8.2

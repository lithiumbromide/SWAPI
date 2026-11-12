---
title: "ReleaseSelectionAccess Method (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IMirrorSolidFeatureData)

Releases access to the selections used to define the mirror solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData

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

See [MirrorSolidFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## Remarks

[IMirrorSolidFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~AccessSelections.html) and [IMirrorSolidFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorSolidFeatureData~IAccessSelections2.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

---
title: "IGetParents Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetParents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.html"
---

# IGetParents Method (IMacroFeatureData)

Gets the parent features of this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetParents( _
   ByVal ParentCount As System.Integer, _
   ByRef PFeatures As Feature _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParentCount As System.Integer
Dim PFeatures As Feature

instance.IGetParents(ParentCount, PFeatures)
```

### C#

```csharp
void IGetParents(
   System.int ParentCount,
   out Feature PFeatures
)
```

### C++/CLI

```cpp
void IGetParents(
   System.int ParentCount,
   [Out] Feature^ PFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParentCount`: Number of parent features for this macro feature
- `PFeatures`: - in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of parents of this macro feature

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

| To get the parent features... | Use... |
| --- | --- |
| assigned to a macro feature by IMacroFeatureData::Parents or IMacroFeatureData::ISetParents | IMacroFeatureData::Parents or IMacroFeatureData::IGetParents - or- IFeature::GetParents or IFeature::IGetParents |
| of a macro feature created by first selecting objects and then calling IFeatureManager::InsertMacroFeature3 or IFeatureManager::IInsertMacroFeature3 | IMacroFeatureData::GetSelections3 or IMacroFeatureData::IGetSelections3 - or - IFeature::GetParents or IFeature::IGetParents |

Before calling this method, call [IMacroFeatureData::GetParentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetParentsCount.html) to determine the value of ParentCount.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

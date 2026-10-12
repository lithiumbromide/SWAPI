---
title: "ISetParents Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "ISetParents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParents.html"
---

# ISetParents Method (IMacroFeatureData)

Sets the parent features for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetParents( _
   ByVal ParentCount As System.Integer, _
   ByRef PFeatures As Feature _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ParentCount As System.Integer
Dim PFeatures As Feature

instance.ISetParents(ParentCount, PFeatures)
```

### C#

```csharp
void ISetParents(
   System.int ParentCount,
   ref Feature PFeatures
)
```

### C++/CLI

```cpp
void ISetParents(
   System.int ParentCount,
   Feature^% PFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParentCount`: Number of parent features for this macro feature
- `PFeatures`: - in-process, unmanaged C++: Pointer to an array of parent [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [MacroFeatureData::ISetParents](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~ISetParents.html).

## Remarks

Parent features set by this method are not persistent when the macro feature is regenerated. Reset the parent features in the [SwComFeature::Regenerate](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Regenerate.html) handler.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetParentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.html)
[IMacroFeatureData::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.html)
[IMacroFeatureData::Parents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

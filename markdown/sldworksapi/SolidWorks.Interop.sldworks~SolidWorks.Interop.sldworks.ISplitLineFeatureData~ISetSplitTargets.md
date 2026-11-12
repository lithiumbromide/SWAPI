---
title: "ISetSplitTargets Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "ISetSplitTargets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTargets.html"
---

# ISetSplitTargets Method (ISplitLineFeatureData)

Sets the faces or bodies to split.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSplitTargets( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetSplitTargets(Count, DispArr)
```

### C#

```csharp
void ISetSplitTargets(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetSplitTargets(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces or bodies to split
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to split

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SplitLineFeatureData::ISetSplitTargets](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~ISetSplitTargets.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetSplitTargetsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitTargetsCount.html)
[ISplitLineFeatureData::IGetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTargets.html)
[ISplitLineFeatureData::SplitTargets Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTargets.html)
[ISplitLineFeatureData::SplitAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitAll.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

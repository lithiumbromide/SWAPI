---
title: "ISetSplitTools Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "ISetSplitTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools.html"
---

# ISetSplitTools Method (ISplitLineFeatureData)

Sets the tools used to make the split.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSplitTools( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetSplitTools(Count, DispArr)
```

### C#

```csharp
void ISetSplitTools(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetSplitTools(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of tools used to make the split
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of tools used to make the split (see **Remarks**)

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SplitLineFeatureData::ISetSplitTools](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~ISetSplitTools.html).

## Remarks

[Reference planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), [planar model faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), and [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) are valid tools for a split.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetSplitToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount.html)
[ISplitLineFeatureData::IGetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.html)
[ISplitLineFeatureData::SplitTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

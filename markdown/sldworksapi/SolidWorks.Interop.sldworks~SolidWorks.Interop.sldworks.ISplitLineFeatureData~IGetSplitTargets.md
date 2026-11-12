---
title: "IGetSplitTargets Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "IGetSplitTargets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTargets.html"
---

# IGetSplitTargets Method (ISplitLineFeatureData)

Gets the faces or bodies to split.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplitTargets( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetSplitTargets(Count)
```

### C#

```csharp
System.object IGetSplitTargets(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetSplitTargets(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces or bodies to split

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to split

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISplitLineFeatureData::GetSplitTargetsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~GetSplitTargetsCount.html) before calling this method to determine the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTargets.html)
[ISplitLineFeatureData::SplitTargets Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTargets.html)
[ISplitLineFeatureData::SplitAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitAll.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

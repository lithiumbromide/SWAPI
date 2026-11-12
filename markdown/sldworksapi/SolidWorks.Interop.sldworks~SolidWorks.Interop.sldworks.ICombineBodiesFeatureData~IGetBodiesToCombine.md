---
title: "IGetBodiesToCombine Method (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "IGetBodiesToCombine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.html"
---

# IGetBodiesToCombine Method (ICombineBodiesFeatureData)

Gets the bodies to combine.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodiesToCombine( _
   ByVal NCount As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim NCount As System.Integer
Dim value As Body2

value = instance.IGetBodiesToCombine(NCount)
```

### C#

```csharp
Body2 IGetBodiesToCombine(
   System.int NCount
)
```

### C++/CLI

```cpp
Body2^ IGetBodiesToCombine(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of bodies to combine

### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICombineBodiesFeatureData::GetBodiesToCombineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.html) before calling this method to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)
[ICombineBodiesFeatureData::ISetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.html)
[ICombineBodiesFeatureData::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13

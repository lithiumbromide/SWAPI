---
title: "ISetBodiesToCombine Method (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "ISetBodiesToCombine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.html"
---

# ISetBodiesToCombine Method (ICombineBodiesFeatureData)

Sets the bodies to combine.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodiesToCombine( _
   ByVal NCount As System.Integer, _
   ByRef PBodiesToCombine As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim NCount As System.Integer
Dim PBodiesToCombine As Body2

instance.ISetBodiesToCombine(NCount, PBodiesToCombine)
```

### C#

```csharp
void ISetBodiesToCombine(
   System.int NCount,
   ref Body2 PBodiesToCombine
)
```

### C++/CLI

```cpp
void ISetBodiesToCombine(
   System.int NCount,
   Body2^% PBodiesToCombine
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of bodies to combine
- `PBodiesToCombine`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)
[ICombineBodiesFeatureData::GetBodiesToCombineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.html)
[ICombineBodiesFeatureData::IGetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.html)
[ICombineBodiesFeatureData::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Numjber 13

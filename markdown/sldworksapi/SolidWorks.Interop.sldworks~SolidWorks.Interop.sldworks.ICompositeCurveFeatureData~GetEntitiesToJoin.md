---
title: "GetEntitiesToJoin Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "GetEntitiesToJoin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin.html"
---

# GetEntitiesToJoin Method (ICompositeCurveFeatureData)

Gets the entities to join to create this composite curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesToJoin( _
   ByRef Type As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData
Dim Type As System.Object
Dim value As System.Object

value = instance.GetEntitiesToJoin(Type)
```

### C#

```csharp
System.object GetEntitiesToJoin(
   out System.object Type
)
```

### C++/CLI

```cpp
System.Object^ GetEntitiesToJoin(
   [Out] System.Object^ Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of entities (see **Remarks**)

## VBA Syntax

See [CompositeCurveFeatureData::GetEntitiesToJoin](ms-its:sldworksapivb6.chm::/sldworks~CompositeCurveFeatureData~GetEntitiesToJoin.html).

## Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)
[ICompositeCurveFeatureData::IGetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin.html)
[ICompositeCurveFeatureData::GetEntitiesToJoinCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

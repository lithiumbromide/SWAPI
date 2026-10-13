---
title: "IGetEntitiesToJoin Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "IGetEntitiesToJoin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin.html"
---

# IGetEntitiesToJoin Method (ICompositeCurveFeatureData)

Gets the entities to join to create this composite curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntitiesToJoin( _
   ByVal Count As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData
Dim Count As System.Integer
Dim Type As System.Integer
Dim value As System.Object

value = instance.IGetEntitiesToJoin(Count, Type)
```

### C#

```csharp
System.object IGetEntitiesToJoin(
   System.int Count,
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ IGetEntitiesToJoin(
   System.int Count,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities
- `Type`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities. Call [ICompositeCurveFeatureData::GetEntitiesToJoinCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)
[ICompositeCurveFeatureData::GetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin.html)

## Availability

SolidWork 2003 FCS, Revision Number 11.0

---
title: "ISetEntitiesToJoin Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "ISetEntitiesToJoin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~ISetEntitiesToJoin.html"
---

# ISetEntitiesToJoin Method (ICompositeCurveFeatureData)

Sets the entities to join to create this composite curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntitiesToJoin( _
   ByVal Count As System.Integer, _
   ByRef Ents As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData
Dim Count As System.Integer
Dim Ents As System.Object

instance.ISetEntitiesToJoin(Count, Ents)
```

### C#

```csharp
void ISetEntitiesToJoin(
   System.int Count,
   ref System.object Ents
)
```

### C++/CLI

```cpp
void ISetEntitiesToJoin(
   System.int Count,
   System.Object^% Ents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities
- `Ents`: in-process, unmanaged C++: Pointer to an array of entities (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)
[ICompositeCurveFeatureData::SetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~SetEntitiesToJoin.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

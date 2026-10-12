---
title: "SetEntitiesToJoin Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "SetEntitiesToJoin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~SetEntitiesToJoin.html"
---

# SetEntitiesToJoin Method (ICompositeCurveFeatureData)

Sets the entities to join to create this composite curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntitiesToJoin( _
   ByVal EntVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData
Dim EntVar As System.Object

instance.SetEntitiesToJoin(EntVar)
```

### C#

```csharp
void SetEntitiesToJoin(
   System.object EntVar
)
```

### C++/CLI

```cpp
void SetEntitiesToJoin(
   System.Object^ EntVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntVar`: Array of entities (see **Remarks**)

## VBA Syntax

See [CompositeCurveFeatureData::SetEntitiesToJoin](ms-its:sldworksapivb6.chm::/sldworks~CompositeCurveFeatureData~SetEntitiesToJoin.html).

## Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)
[ICompositeCurveFeatureData::ISetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~ISetEntitiesToJoin.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

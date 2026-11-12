---
title: "InsertEdgeMerge Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertEdgeMerge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEdgeMerge.html"
---

# InsertEdgeMerge Method (IFeatureManager)

Merges multiple edges into a single edge using the selected faces when importing data.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEdgeMerge( _
   ByVal Angular_tolerance As System.Double, _
   ByVal Edge_length_tolerance As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angular_tolerance As System.Double
Dim Edge_length_tolerance As System.Double
Dim value As Feature

value = instance.InsertEdgeMerge(Angular_tolerance, Edge_length_tolerance)
```

### C#

```csharp
Feature InsertEdgeMerge(
   System.double Angular_tolerance,
   System.double Edge_length_tolerance
)
```

### C++/CLI

```cpp
Feature^ InsertEdgeMerge(
   System.double Angular_tolerance,
   System.double Edge_length_tolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angular_tolerance`: Angular tolerance
- `Edge_length_tolerance`: Edge length tolerance

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertEdgeMerge](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertEdgeMerge.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

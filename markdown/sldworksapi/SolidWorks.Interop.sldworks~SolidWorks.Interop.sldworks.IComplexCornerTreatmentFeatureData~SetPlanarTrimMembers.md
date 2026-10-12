---
title: "SetPlanarTrimMembers Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "SetPlanarTrimMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~SetPlanarTrimMembers.html"
---

# SetPlanarTrimMembers Method (IComplexCornerTreatmentFeatureData)

Sets the planar trim member of this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlanarTrimMembers( _
   ByVal PlanarMemList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim PlanarMemList As System.Object
Dim value As System.Boolean

value = instance.SetPlanarTrimMembers(PlanarMemList)
```

### C#

```csharp
System.bool SetPlanarTrimMembers(
   System.object PlanarMemList
)
```

### C++/CLI

```cpp
System.bool SetPlanarTrimMembers(
   System.Object^ PlanarMemList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PlanarMemList`: Array of planar trim [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

### Return Value

True if planar trim members successfully set, false if not

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::SetPlanarTrimMembers](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~SetPlanarTrimMembers.html).

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

---
title: "GetConnectionPointsCount Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "GetConnectionPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.html"
---

# GetConnectionPointsCount Method (IStructuralMemberFeatureData)

Gets the number of sketch points for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectionPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer

value = instance.GetConnectionPointsCount()
```

### C#

```csharp
System.int GetConnectionPointsCount()
```

### C++/CLI

```cpp
System.int GetConnectionPointsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch points

## VBA Syntax

See [StructuralMemberFeatureData::GetConnectionPointsCount](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~GetConnectionPointsCount.html).

## Remarks

Call this method before calling [IStructuralMemberFeatureData::IGetConnectionPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html) to get the size of the array for that method.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html)
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.html)
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.html)
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "GetConnectionPoints Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "GetConnectionPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html"
---

# GetConnectionPoints Method (IStructuralMemberFeatureData)

Gets the connection points for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectionPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Object

value = instance.GetConnectionPoints()
```

### C#

```csharp
System.object GetConnectionPoints()
```

### C++/CLI

```cpp
System.Object^ GetConnectionPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) representing the connection points

## VBA Syntax

See [StructuralMemberFeatureData::GetConnectionPoints](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~GetConnectionPoints.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::IGetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html)
[IStructuralMemberFeatureData::GetConnectionPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.html)
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.html)
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.html)
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

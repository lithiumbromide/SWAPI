---
title: "IGetConnectionPoints Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "IGetConnectionPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.html"
---

# IGetConnectionPoints Method (IStructuralMemberFeatureData)

Gets the connection points for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConnectionPoints( _
   ByVal Count As System.Integer _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim value As SketchPoint

value = instance.IGetConnectionPoints(Count)
```

### C#

```csharp
SketchPoint IGetConnectionPoints(
   System.int Count
)
```

### C++/CLI

```cpp
SketchPoint^ IGetConnectionPoints(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of connection points

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) representing the connection points

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IStructuralMemberFeatureData::GetConnectionPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.html) before this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.html)
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.html)
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.html)
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

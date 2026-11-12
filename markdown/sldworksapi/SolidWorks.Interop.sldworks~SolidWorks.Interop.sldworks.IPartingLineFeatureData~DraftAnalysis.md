---
title: "DraftAnalysis Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "DraftAnalysis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html"
---

# DraftAnalysis Method (IPartingLineFeatureData)

Performs draft analysis for the input angle and the direction of pull.

## Syntax

### Visual Basic (Declaration)

```vb
Function DraftAnalysis( _
   ByVal Angle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim Angle As System.Double
Dim value As System.Boolean

value = instance.DraftAnalysis(Angle)
```

### C#

```csharp
System.bool DraftAnalysis(
   System.double Angle
)
```

### C++/CLI

```cpp
System.bool DraftAnalysis(
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Draft angle

### Return Value

True if draft analysis is performed, false if not

## VBA Syntax

See [PartingLineFeatureData::DraftAnalysis](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~DraftAnalysis.html).

## Remarks

If you want a different pull direction, then use [IPartingLineFeatureData::PullDirectionBase](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.html) to change the direction. Once this method is called, only the information for different faces (negative, positive, and so on) is generated.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Angle.html)
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.html)
[IPartingLineFeatureData::IGetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.html)
[IPartingLineFeatureData::GetFacesByTypeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.html)
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.html)
[IPartingLineFeatureData::PullDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.html)
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

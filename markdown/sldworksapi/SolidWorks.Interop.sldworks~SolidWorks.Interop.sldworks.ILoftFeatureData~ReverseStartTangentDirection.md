---
title: "ReverseStartTangentDirection Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "ReverseStartTangentDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReverseStartTangentDirection.html"
---

# ReverseStartTangentDirection Property (ILoftFeatureData)

Reverses the tangent direction for the start point of this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseStartTangentDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

instance.ReverseStartTangentDirection = value

value = instance.ReverseStartTangentDirection
```

### C#

```csharp
System.bool ReverseStartTangentDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseStartTangentDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the tangent direction for the start point, false does not

## VBA Syntax

See [LoftFeatureData::ReverseStartTangentDirection](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~ReverseStartTangentDirection.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.html)
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.html)
[ILoftFeatureData::EndConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintApplyToAll.html)
[ILoftFeatureData::EndConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngle.html)
[ILoftFeatureData::EndConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngleDirection.html)
[ILoftFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangencyType.html)
[ILoftFeatureData::EndTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangentLength.html)
[ILoftFeatureData::MaintainTangency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~MaintainTangency.html)
[ILoftFeatureData::ReverseEndTangentDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReverseEndTangentDirection.html)
[ILoftFeatureData::StartConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintApplyToAll.html)
[ILoftFeatureData::StartConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngle.html)
[ILoftFeatureData::StartConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngleDirection.html)
[ILoftFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangencyType.html)
[ILoftFeatureData::StartTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangentLength.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "StartConstraintDraftAngleDirection Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "StartConstraintDraftAngleDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngleDirection.html"
---

# StartConstraintDraftAngleDirection Property (ILoftFeatureData)

Gets or sets the direction of the angle of the draft for the start constraint for the loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartConstraintDraftAngleDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

instance.StartConstraintDraftAngleDirection = value

value = instance.StartConstraintDraftAngleDirection
```

### C#

```csharp
System.bool StartConstraintDraftAngleDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool StartConstraintDraftAngleDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the direction of the draft angle is reversed, false if not

## VBA Syntax

See [LoftFeatureData::StartConstraintDraftAngleDirection](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~StartConstraintDraftAngleDirection.html).

## Remarks

This property is only valid if [ILoftFeatureData::StartConstraintApplyToAll](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~StartConstraintApplyToAll.html) and [ILoftFeatureData::EndConstraintApplyToAll](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~EndConstraintApplyToAll.html) are True.

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
[ILoftFeatureData::ReverseStartTangentDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReverseStartTangentDirection.html)
[ILoftFeatureData::StartConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintApplyToAll.html)
[ILoftFeatureData::StartConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngle.html)
[ILoftFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangencyType.html)
[ILoftFeatureData::StartTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangentLength.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

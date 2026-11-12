---
title: "CurvatureContinuous Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "CurvatureContinuous"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html"
---

# CurvatureContinuous Property (ISimpleFilletFeatureData2)

Gets or sets whether to create a smoother curvature between adjacent surfaces for this simple fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvatureContinuous As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.CurvatureContinuous = value

value = instance.CurvatureContinuous
```

### C#

```csharp
System.bool CurvatureContinuous {get; set;}
```

### C++/CLI

```cpp
property System.bool CurvatureContinuous {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to make curvatures continuous, false to not

## VBA Syntax

See [SimpleFilletFeatureData2::CurvatureContinuous](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~CurvatureContinuous.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

This property overrides any [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting. Curvature continuous fillets are smoother than standard fillets because there is no jump in curvature at the boundary.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetHoldLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.html)
[ISimpleFilletFeatureData2::IGetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.html)
[ISimpleFilletFeatureData2::ISetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.html)
[ISimpleFilletFeatureData2::HelpPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html)
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

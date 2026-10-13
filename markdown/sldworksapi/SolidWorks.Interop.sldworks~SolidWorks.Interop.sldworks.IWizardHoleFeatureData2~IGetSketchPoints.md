---
title: "IGetSketchPoints Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "IGetSketchPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.html"
---

# IGetSketchPoints Method (IWizardHoleFeatureData2)

Gets the center-hole sketch points in this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPoints( _
   ByVal NCount As System.Integer _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim NCount As System.Integer
Dim value As SketchPoint

value = instance.IGetSketchPoints(NCount)
```

### C#

```csharp
SketchPoint IGetSketchPoints(
   System.int NCount
)
```

### C++/CLI

```cpp
SketchPoint^ IGetSketchPoints(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of center-hole sketch points

### Return Value

Array of center-hole [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [WizardHoleFeatureData2::IGetSketchPoints](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~IGetSketchPoints.html).

## Remarks

Before calling this method, call [IWizardHoleFeatureData2::GetSketchPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount.html) to get NCount.

To add or remove sketch points in a Hole Wizard feature sketch (also called a location sketch), you must edit the sketch. After editing the sketch, update the Hole Wizard feature by calling [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

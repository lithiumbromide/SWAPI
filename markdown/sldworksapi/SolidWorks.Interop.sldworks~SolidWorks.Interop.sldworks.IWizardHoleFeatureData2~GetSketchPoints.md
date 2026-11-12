---
title: "GetSketchPoints Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "GetSketchPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.html"
---

# GetSketchPoints Method (IWizardHoleFeatureData2)

Gets the center-hole sketch points in this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Object

value = instance.GetSketchPoints()
```

### C#

```csharp
System.object GetSketchPoints()
```

### C++/CLI

```cpp
System.Object^ GetSketchPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of center-hole [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [WizardHoleFeatureData2::GetSketchPoints](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~GetSketchPoints.html).

## Examples

[Get and Add Sketch Points in Hole Wizard Feature (C#)](Get_Sketch_Points_in_Wizard_Hole_Example_CSharp.htm)
[Get and Add Sketch Points in Hole Wizard Feature (VB.NET)](Get_Sketch_Points_in_Wizard_Hole_Example_VBNET.htm)
[Get and Add Sketch Points in Hole Wizard Feature (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)

## Remarks

To add or remove sketch points in a Hole Wizard feature sketch (also called a location sketch), you must edit the sketch. After editing the sketch, update the Hole Wizard feature by calling [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetSketchPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount.html)
[IWizardHoleFeatureData2::IGetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

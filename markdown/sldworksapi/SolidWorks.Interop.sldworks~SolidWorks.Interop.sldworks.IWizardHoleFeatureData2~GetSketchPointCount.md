---
title: "GetSketchPointCount Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "GetSketchPointCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount.html"
---

# GetSketchPointCount Method (IWizardHoleFeatureData2)

Gets the number of center-hole sketch points in this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPointCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

value = instance.GetSketchPointCount()
```

### C#

```csharp
System.int GetSketchPointCount()
```

### C++/CLI

```cpp
System.int GetSketchPointCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of center-hole sketch points

## VBA Syntax

See [WizardHoleFeatureData2::GetSketchPointCount](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~GetSketchPointCount.html).

## Examples

[Get and Add Sketch Points in Hole Wizard Feature (C#)](Get_Sketch_Points_in_Wizard_Hole_Example_CSharp.htm)
[Get and Add Sketch Points in Hole Wizard Feature (VB.NET)](Get_Sketch_Points_in_Wizard_Hole_Example_VBNET.htm)
[Get and Add Sketch Points in Hole Wizard Feature (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)

## Remarks

Call this method before calling [IWizardHoleFeatureData2::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

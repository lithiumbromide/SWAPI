---
title: "ThreadDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThreadDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDiameter.html"
---

# ThreadDiameter Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature thread diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.ThreadDiameter = value

value = instance.ThreadDiameter
```

### C#

```csharp
System.double ThreadDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double ThreadDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread diameter

## VBA Syntax

See [WizardHoleFeatureData2::ThreadDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThreadDiameter.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThreadAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadAngle.html)
[IWizardHoleFeatureData2::ThreadClass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadClass.html)
[IWizardHoleFeatureData2::ThreadDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDepth.html)
[IWizardHoleFeatureData2::ThreadEndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadEndCondition.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

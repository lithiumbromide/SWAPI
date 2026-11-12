---
title: "ThreadDepth Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThreadDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDepth.html"
---

# ThreadDepth Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature thread depth.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.ThreadDepth = value

value = instance.ThreadDepth
```

### C#

```csharp
System.double ThreadDepth {get; set;}
```

### C++/CLI

```cpp
property System.double ThreadDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread depth

## VBA Syntax

See [WizardHoleFeatureData2::ThreadDepth](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThreadDepth.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThreadAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadAngle.html)
[IWizardHoleFeatureData2::ThreadClass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadClass.html)
[IWizardHoleFeatureData2::ThreadEndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadEndCondition.html)
[IWizardHoleFeatureData2::ThreadClass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadClass.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "ThreadEndCondition Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThreadEndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadEndCondition.html"
---

# ThreadEndCondition Property (IWizardHoleFeatureData2)

Gets or sets the thread end condition for this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadEndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.ThreadEndCondition = value

value = instance.ThreadEndCondition
```

### C#

```csharp
System.int ThreadEndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int ThreadEndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread end condition as defined in [swWzdHoleThreadEndCondition](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleThreadEndCondition_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::ThreadEndCondition](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThreadEndCondition.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThreadAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadAngle.html)
[IWizardHoleFeatureData2::ThreadClass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadClass.html)
[IWizardHoleFeatureData2::ThreadDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDepth.html)
[IWizardHoleFeatureData2::ThreadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDiameter.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3

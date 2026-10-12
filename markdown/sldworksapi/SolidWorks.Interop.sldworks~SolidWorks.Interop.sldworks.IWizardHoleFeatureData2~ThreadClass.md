---
title: "ThreadClass Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThreadClass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadClass.html"
---

# ThreadClass Property (IWizardHoleFeatureData2)

Gets or sets the thread class for this Hole Wizard feature..

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.String

instance.ThreadClass = value

value = instance.ThreadClass
```

### C#

```csharp
System.string ThreadClass {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThreadClass {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

One of the following thread classes:

- 1B
- 2B
- 3B

## VBA Syntax

See [WizardHoleFeatureData2::ThreadClass](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThreadClass.html).

## Remarks

This property is relevant only for the ANSI inch standard.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThreadAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadAngle.html)
[IWizardHoleFeatureData2::ThreadDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDepth.html)
[IWizardHoleFeatureData2::ThreadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadDiameter.html)
[IWizardHoleFeatureData2::ThreadEndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThreadEndCondition.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

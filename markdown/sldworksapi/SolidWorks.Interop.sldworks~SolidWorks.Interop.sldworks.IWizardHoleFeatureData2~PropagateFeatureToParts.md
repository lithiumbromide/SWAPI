---
title: "PropagateFeatureToParts Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "PropagateFeatureToParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~PropagateFeatureToParts.html"
---

# PropagateFeatureToParts Property (IWizardHoleFeatureData2)

Gets whether to propagate this assembly Hole Wizard feature to the parts that it affects in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateFeatureToParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.PropagateFeatureToParts = value

value = instance.PropagateFeatureToParts
```

### C#

```csharp
System.bool PropagateFeatureToParts {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateFeatureToParts {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate this assembly Hole Wizard feature to the parts that it affects in the model, false to not

## VBA Syntax

See [WizardHoleFeatureData2::PropagateFeatureToParts](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~PropagateFeatureToParts.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AssemblyFeatureScope.html)
[IWizardHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.html)
[IWizardHoleFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelectComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

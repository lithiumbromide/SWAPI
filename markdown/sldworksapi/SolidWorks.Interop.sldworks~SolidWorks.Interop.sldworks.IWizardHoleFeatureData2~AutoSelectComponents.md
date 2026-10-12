---
title: "AutoSelectComponents Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "AutoSelectComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelectComponents.html"
---

# AutoSelectComponents Property (IWizardHoleFeatureData2)

Gets or sets whether to auto-select all components that this assembly Hole Wizard feature affects in model.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelectComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.AutoSelectComponents = value

value = instance.AutoSelectComponents
```

### C#

```csharp
System.bool AutoSelectComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSelectComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to auto-select all affected components, false to not (use the selected components only or set [IWizardHoleFeatureData2::AutoSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.html) to true)

## VBA Syntax

See [WizardHoleFeatureData2::AutoSelectComponents](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~AutoSelectComponents.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AssemblyFeatureScope.html)
[IWizardHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

---
title: "AssemblyFeatureScope Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "AssemblyFeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AssemblyFeatureScope.html"
---

# AssemblyFeatureScope Property (IWizardHoleFeatureData2)

Gets or sets whether to use scope for this assembly Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyFeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.AssemblyFeatureScope = value

value = instance.AssemblyFeatureScope
```

### C#

```csharp
System.bool AssemblyFeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.bool AssemblyFeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use feature scope, false to not

## VBA Syntax

See [WizardHoleFeatureData2::AssemblyFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~AssemblyFeatureScope.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.html)
[IWizardHoleFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelectComponents.html)
[IWizardHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~PropagateFeatureToParts.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

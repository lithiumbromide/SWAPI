---
title: "Type Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Type.html"
---

# Type Property (IWizardHoleFeatureData2)

Gets the Hole Wizard feature type.

****NOTE:** This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type as defined in [swWzdHoleTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleTypes_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::Type](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~Type.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

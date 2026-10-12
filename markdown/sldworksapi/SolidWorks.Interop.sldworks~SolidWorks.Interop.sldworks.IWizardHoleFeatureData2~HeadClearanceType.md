---
title: "HeadClearanceType Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "HeadClearanceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearanceType.html"
---

# HeadClearanceType Property (IWizardHoleFeatureData2)

Gets the type of head clearance for this countersink Hole Wizard feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property HeadClearanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.HeadClearanceType = value

value = instance.HeadClearanceType
```

### C#

```csharp
System.int HeadClearanceType {get; set;}
```

### C++/CLI

```cpp
property System.int HeadClearanceType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of head clearance as defined in [swWzdHoleCounterSinkHeadClearanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCounterSinkHeadClearanceTypes_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::HeadClearanceType](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~HeadClearanceType.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::HeadClearance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

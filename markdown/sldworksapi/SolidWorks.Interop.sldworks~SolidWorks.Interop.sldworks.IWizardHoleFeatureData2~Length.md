---
title: "Length Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Length.html"
---

# Length Property (IWizardHoleFeatureData2)

Gets or sets the length of a Hole Wizard slot feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.Length = value

value = instance.Length
```

### C#

```csharp
System.double Length {get; set;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of slot

## VBA Syntax

See [WizardHoleFeatureData2::Length](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~Length.html).

## Examples

[Insert Hole Wizard Slot and Hole (C#)](Insert_Hole_Wizard_Slot_and_Hole_Example_CSharp.htm)
[Insert Hole Wizard Slot and Hole (VB.NET)](Insert_Hole_Wizard_Slot_and_Hole_Example_VBNET.htm)
[Insert Hole Wizard Slot and Hole (VBA)](Insert_Hole_Wizard_Slot_and_Hole_Example_VB.htm)

## Remarks

This property is only valid for slots.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

---
title: "ChangeStandard Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ChangeStandard"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ChangeStandard.html"
---

# ChangeStandard Method (IWizardHoleFeatureData2)

Sets the standard for all of the parameters of the Hole Wizard feature that are driven by the database.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeStandard( _
   ByVal Standard As System.Integer, _
   ByVal FastenerType As System.Integer, _
   ByVal SSize As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim Standard As System.Integer
Dim FastenerType As System.Integer
Dim SSize As System.String
Dim value As System.Boolean

value = instance.ChangeStandard(Standard, FastenerType, SSize)
```

### C#

```csharp
System.bool ChangeStandard(
   System.int Standard,
   System.int FastenerType,
   System.string SSize
)
```

### C++/CLI

```cpp
System.bool ChangeStandard(
   System.int Standard,
   System.int FastenerType,
   System.String^ SSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Standard`: Standard as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)
- `FastenerType`: Fastener type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)
- `SSize`: Fastener size

### Return Value

True if the standard is changed, false if not

## VBA Syntax

See [WizardHoleFeatureData2::ChangeStandard](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ChangeStandard.html).

## Remarks

Use this method to change [fastener size](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.html), [fastener type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.html), and [design standard](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~Standard2.html) of a Hole Wizard feature.

If changing the standard requires you to change the type, then you must call [IWizardHoleFeatureData2::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~Type.html) before calling IWizardHoleFeatureData2::ChangeStandard.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3

---
title: "UnderHeadCounterSink Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "UnderHeadCounterSink"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~UnderHeadCounterSink.html"
---

# UnderHeadCounterSink Property (IWizardHoleFeatureData2)

Gets or sets whether the Hole Wizard feature is an underhead counter sink.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnderHeadCounterSink As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.UnderHeadCounterSink = value

value = instance.UnderHeadCounterSink
```

### C#

```csharp
System.bool UnderHeadCounterSink {get; set;}
```

### C++/CLI

```cpp
property System.bool UnderHeadCounterSink {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True if an underhead counter sink, false if not

## VBA Syntax

See

[WizardHoleFeatureData2::UnderHeadCounterSink](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~UnderHeadCounterSink.html)

.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)

[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

[IWizardHoleFeatureData2::UnderHeadCounterSinkAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~UnderHeadCounterSinkAngle.html)

[IWizardHoleFeatureData2::UnderHeadCounterSinkDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~UnderHeadCounterSinkDiameter.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1

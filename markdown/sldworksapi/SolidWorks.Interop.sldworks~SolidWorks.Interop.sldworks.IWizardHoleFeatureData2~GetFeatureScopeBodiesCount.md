---
title: "GetFeatureScopeBodiesCount Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "GetFeatureScopeBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetFeatureScopeBodiesCount.html"
---

# GetFeatureScopeBodiesCount Method (IWizardHoleFeatureData2)

Gets the number of solid bodies affected by the Hole Wizard feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

value = instance.GetFeatureScopeBodiesCount()
```

### C#

```csharp
System.int GetFeatureScopeBodiesCount()
```

### C++/CLI

```cpp
System.int GetFeatureScopeBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solid bodies affected

## VBA Syntax

See [WizardHoleFeatureData2::GetFeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~GetFeatureScopeBodiesCount.html).

## Remarks

Call this method before calling [IWizardHoleFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IGetFeatureScopeBodies.html).

If [IWizardHoleFeatureData2::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FeatureScope.html) is false, then the return value is 0.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ISetFeatureScopeBodies.html)
[IWizardHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~AutoSelect.html)
[IWizardHoleFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

---
title: "IFace Property (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "IFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~IFace.html"
---

# IFace Property (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::IFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~IFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IFace As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
Dim value As Face

instance.IFace = value

value = instance.IFace
```

### C#

```csharp
Face IFace {get; set;}
```

### C++/CLI

```cpp
property Face^ IFace {
   Face^ get();
   void set (    Face^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [WizardHoleFeatureData::IFace](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~IFace.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)

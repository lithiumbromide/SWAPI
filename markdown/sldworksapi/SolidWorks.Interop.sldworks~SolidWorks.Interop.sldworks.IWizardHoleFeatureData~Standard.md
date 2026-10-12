---
title: "Standard Property (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "Standard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~Standard.html"
---

# Standard Property (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::Standard2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~Standard2.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Standard As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
Dim value As System.String

instance.Standard = value

value = instance.Standard
```

### C#

```csharp
System.string Standard {get; set;}
```

### C++/CLI

```cpp
property System.String^ Standard {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [WizardHoleFeatureData::Standard](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~Standard.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)

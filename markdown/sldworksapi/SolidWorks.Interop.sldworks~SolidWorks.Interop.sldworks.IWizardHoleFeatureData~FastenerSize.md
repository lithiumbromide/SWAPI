---
title: "FastenerSize Property (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "FastenerSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~FastenerSize.html"
---

# FastenerSize Property (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::FastenerSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FastenerSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
Dim value As System.String

instance.FastenerSize = value

value = instance.FastenerSize
```

### C#

```csharp
System.string FastenerSize {get; set;}
```

### C++/CLI

```cpp
property System.String^ FastenerSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [WizardHoleFeatureData::FastenerSize](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~FastenerSize.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)

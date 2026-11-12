---
title: "FastenerType Property (IWizardHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData"
member: "FastenerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData~FastenerType.html"
---

# FastenerType Property (IWizardHoleFeatureData)

Obsolete. Superseded by [IWizardHoleFeatureData2::FastenerType2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FastenerType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData
Dim value As System.String

instance.FastenerType = value

value = instance.FastenerType
```

### C#

```csharp
System.string FastenerType {get; set;}
```

### C++/CLI

```cpp
property System.String^ FastenerType {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [WizardHoleFeatureData::FastenerType](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData~FastenerType.html).

## See Also

[IWizardHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData.html)
[IWizardHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData_members.html)

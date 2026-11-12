---
title: "HoleWizardData Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "HoleWizardData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~HoleWizardData.html"
---

# HoleWizardData Property (IMirrorPartFeatureData)

Gets or sets whether to import hole wizard data.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleWizardData As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.HoleWizardData = value

value = instance.HoleWizardData
```

### C#

```csharp
System.bool HoleWizardData {get; set;}
```

### C++/CLI

```cpp
property System.bool HoleWizardData {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import hole wizard data, false to not

## VBA Syntax

See [MirrorPartFeatureData::HoleWizardData](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~HoleWizardData.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

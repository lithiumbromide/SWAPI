---
title: "ImportHoleWizardData Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportHoleWizardData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportHoleWizardData.html"
---

# ImportHoleWizardData Property (IDerivedPartFeatureData)

Gets or sets whether to import Hole Wizard data with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportHoleWizardData As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportHoleWizardData = value

value = instance.ImportHoleWizardData
```

### C#

```csharp
System.bool ImportHoleWizardData {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportHoleWizardData {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its Hole Wizard data, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportHoleWizardData](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportHoleWizardData.html).

## Remarks

This property is valid only if [IDerivedPartFeatureData::ImportSolidBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.html) is true.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

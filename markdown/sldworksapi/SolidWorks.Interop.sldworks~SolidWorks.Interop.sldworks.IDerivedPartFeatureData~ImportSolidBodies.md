---
title: "ImportSolidBodies Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportSolidBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.html"
---

# ImportSolidBodies Property (IDerivedPartFeatureData)

Gets or sets whether to import solid bodies with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportSolidBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportSolidBodies = value

value = instance.ImportSolidBodies
```

### C#

```csharp
System.bool ImportSolidBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportSolidBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its solid bodies, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportSolidBodies](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportSolidBodies.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)
[IDerivedPartFeatureData::ImportModelDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportModelDimensions.html)
[IDerivedPartFeatureData::ImportHoleWizardData Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportHoleWizardData.html)
[IDerivedPartFeatureData::ImportCustomProperties Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCustomProperties.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

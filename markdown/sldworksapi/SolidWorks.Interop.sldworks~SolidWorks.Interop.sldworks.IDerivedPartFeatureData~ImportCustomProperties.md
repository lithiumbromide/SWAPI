---
title: "ImportCustomProperties Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportCustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCustomProperties.html"
---

# ImportCustomProperties Property (IDerivedPartFeatureData)

Gets or sets which custom properties to import with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportCustomProperties As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Integer

instance.ImportCustomProperties = value

value = instance.ImportCustomProperties
```

### C#

```csharp
System.int ImportCustomProperties {get; set;}
```

### C++/CLI

```cpp
property System.int ImportCustomProperties {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Custom properties to import as defined in [swImportPartCustomPropertiesToOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportPartCustomPropertiesToOptions_e.html)

## VBA Syntax

See [DerivedPartFeatureData::ImportCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportCustomProperties.html).

## Remarks

This property is valid when:

- the derived part has custom properties,

- and -

- [IDerivedPartFeatureData::ImportSolidBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.html) is set to true.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

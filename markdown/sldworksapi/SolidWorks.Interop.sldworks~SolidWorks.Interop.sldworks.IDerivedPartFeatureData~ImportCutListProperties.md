---
title: "ImportCutListProperties Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportCutListProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCutListProperties.html"
---

# ImportCutListProperties Property (IDerivedPartFeatureData)

Gets or sets whether to import cut list properties with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportCutListProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportCutListProperties = value

value = instance.ImportCutListProperties
```

### C#

```csharp
System.bool ImportCutListProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportCutListProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its cut list properties, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportCutListProperties](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportCutListProperties.html).

## Remarks

This property is valid only if:

- the derived part has cut list properties,

- and -

- [IDerivedPartFeatureData::ImportSheetMetalInformation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSheetMetalInformation.html) is not specified.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

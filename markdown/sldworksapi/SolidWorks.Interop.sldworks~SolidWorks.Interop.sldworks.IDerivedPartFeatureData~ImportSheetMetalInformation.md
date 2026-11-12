---
title: "ImportSheetMetalInformation Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportSheetMetalInformation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSheetMetalInformation.html"
---

# ImportSheetMetalInformation Property (IDerivedPartFeatureData)

Gets or sets how to import sheet metal information with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportSheetMetalInformation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Integer

instance.ImportSheetMetalInformation = value

value = instance.ImportSheetMetalInformation
```

### C#

```csharp
System.int ImportSheetMetalInformation {get; set;}
```

### C++/CLI

```cpp
property System.int ImportSheetMetalInformation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How to import sheet metal information as defined in [swImportSheetMetalInformation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportSheetMetalInformation_e.html)

## VBA Syntax

See [DerivedPartFeatureData::ImportSheetMetalInformation](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportSheetMetalInformation.html).

## Remarks

This property:

- is valid only if the part being inserted is a sheet metal part.
- is not valid if [IDerivedPartFeatureData::ImportCutListProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCutListProperties.html) is set to true.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

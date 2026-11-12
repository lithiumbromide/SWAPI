---
title: "ImportModelDimensions Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportModelDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportModelDimensions.html"
---

# ImportModelDimensions Property (IDerivedPartFeatureData)

Gets or sets whether to import model dimensions with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportModelDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportModelDimensions = value

value = instance.ImportModelDimensions
```

### C#

```csharp
System.bool ImportModelDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportModelDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its model dimensions, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportModelDimensions](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportModelDimensions.html).

## Remarks

This property is valid onlty if [IDerivedPartFeatureData::ImportSolidBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.html) is true.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

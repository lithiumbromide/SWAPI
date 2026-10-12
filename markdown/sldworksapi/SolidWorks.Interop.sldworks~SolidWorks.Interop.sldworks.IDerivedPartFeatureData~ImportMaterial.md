---
title: "ImportMaterial Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportMaterial"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportMaterial.html"
---

# ImportMaterial Property (IDerivedPartFeatureData)

Gets or sets whether to import material with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportMaterial As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportMaterial = value

value = instance.ImportMaterial
```

### C#

```csharp
System.bool ImportMaterial {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportMaterial {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its material, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportMaterial](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportMaterial.html).

## Remarks

This property is valid only while the derived part is being inserted. It is not valid while it is being edited.

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

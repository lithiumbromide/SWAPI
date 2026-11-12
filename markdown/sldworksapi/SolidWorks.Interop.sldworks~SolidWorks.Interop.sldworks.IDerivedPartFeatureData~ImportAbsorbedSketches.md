---
title: "ImportAbsorbedSketches Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportAbsorbedSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportAbsorbedSketches.html"
---

# ImportAbsorbedSketches Property (IDerivedPartFeatureData)

Gets or sets whether to import absorbed sketches with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportAbsorbedSketches As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportAbsorbedSketches = value

value = instance.ImportAbsorbedSketches
```

### C#

```csharp
System.bool ImportAbsorbedSketches {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportAbsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to its import absorbed sketches, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportAbsorbedSketches](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportAbsorbedSketches.html).

## Examples

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)
[IDerivedPartFeatureData::ImportUnAbsorbedSketches Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportUnAbsorbedSketches.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

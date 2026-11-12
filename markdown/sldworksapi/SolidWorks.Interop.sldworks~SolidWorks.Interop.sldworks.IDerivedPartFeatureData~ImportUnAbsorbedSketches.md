---
title: "ImportUnAbsorbedSketches Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportUnAbsorbedSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportUnAbsorbedSketches.html"
---

# ImportUnAbsorbedSketches Property (IDerivedPartFeatureData)

Gets or sets whether to import unabsorbed sketches with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportUnAbsorbedSketches As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportUnAbsorbedSketches = value

value = instance.ImportUnAbsorbedSketches
```

### C#

```csharp
System.bool ImportUnAbsorbedSketches {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportUnAbsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import unabsorbed sketches, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportUnAbsorbedSketches](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportUnAbsorbedSketches.html).

## Examples

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)
[IDerivedPartFeatureData::ImportAbsorbedSketches Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportAbsorbedSketches.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

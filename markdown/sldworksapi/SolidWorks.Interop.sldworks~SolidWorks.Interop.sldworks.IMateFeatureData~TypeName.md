---
title: "TypeName Property (IMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateFeatureData"
member: "TypeName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData~TypeName.html"
---

# TypeName Property (IMateFeatureData)

Gets or sets the type of this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property TypeName As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateFeatureData
Dim value As System.Integer

instance.TypeName = value

value = instance.TypeName
```

### C#

```csharp
System.int TypeName {get; set;}
```

### C++/CLI

```cpp
property System.int TypeName {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mate type as defined in [swMateType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html)

## VBA Syntax

See [MateFeatureData::TypeName](ms-its:sldworksapivb6.chm::/sldworks~MateFeatureData~TypeName.html).

## Examples

See the [IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) examples.

## See Also

[IMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html)
[IMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

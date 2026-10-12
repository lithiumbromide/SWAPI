---
title: "CylindricalOrConicalEdge Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "CylindricalOrConicalEdge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~CylindricalOrConicalEdge.html"
---

# CylindricalOrConicalEdge Property (ISweptFlangeFeatureData)

Gets or sets the linear sketch entity to propagate to the flat pattern of this cylindrical or conical swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CylindricalOrConicalEdge As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Object

instance.CylindricalOrConicalEdge = value

value = instance.CylindricalOrConicalEdge
```

### C#

```csharp
System.object CylindricalOrConicalEdge {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CylindricalOrConicalEdge {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Linear sketch entity

## VBA Syntax

See [SweptFlangeFeatureData::CylindricalOrConicalEdge](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~CylindricalOrConicalEdge.html).

## Remarks

This property is valid only:

- for cylindrical or conical swept flanges

- and -

- for [sweep paths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.html) that are sketches,

- and -

- when not creating the swept flange on an existing sheet metal feature.

For more information, read the **SOLIDWORKS Help > Sheet Metal > Using Sheet Metal Tools > Swept Flange > Creating a Conical Body with a Swept Flange** topic.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29

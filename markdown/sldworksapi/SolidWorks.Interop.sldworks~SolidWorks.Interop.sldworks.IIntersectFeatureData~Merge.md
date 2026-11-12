---
title: "Merge Property (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "Merge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~Merge.html"
---

# Merge Property (IIntersectFeatureData)

Gets or sets whether to merge included regions into one body.

## Syntax

### Visual Basic (Declaration)

```vb
Property Merge As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim value As System.Boolean

instance.Merge = value

value = instance.Merge
```

### C#

```csharp
System.bool Merge {get; set;}
```

### C++/CLI

```cpp
property System.bool Merge {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge included regions into one body, false to create a separate body for each included region

## VBA Syntax

See [IntersectFeatureData::Merge](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~Merge.html).

## Examples

See the [IIntersectFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData.html) examples.

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

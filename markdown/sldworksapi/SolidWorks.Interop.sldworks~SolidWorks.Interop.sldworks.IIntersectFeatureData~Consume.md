---
title: "Consume Property (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "Consume"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~Consume.html"
---

# Consume Property (IIntersectFeatureData)

Gets or sets whether to remove input surfaces from the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property Consume As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim value As System.Boolean

instance.Consume = value

value = instance.Consume
```

### C#

```csharp
System.bool Consume {get; set;}
```

### C++/CLI

```cpp
property System.bool Consume {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to remove input surfaces, false to not

## VBA Syntax

See [IntersectFeatureData::Consume](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~Consume.html).

## Examples

See the [IIntersectFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData.html) examples.

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

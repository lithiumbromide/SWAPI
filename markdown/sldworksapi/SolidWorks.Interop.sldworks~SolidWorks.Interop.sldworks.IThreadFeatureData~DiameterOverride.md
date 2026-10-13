---
title: "DiameterOverride Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "DiameterOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~DiameterOverride.html"
---

# DiameterOverride Property (IThreadFeatureData)

Gets or sets whether to override the diameter of the cylindrical face or helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DiameterOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Boolean

instance.DiameterOverride = value

value = instance.DiameterOverride
```

### C#

```csharp
System.bool DiameterOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool DiameterOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the diameter, false to not (default)

## VBA Syntax

See [ThreadFeatureData::DiameterOverride](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~DiameterOverride.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

If this property is set to true, use [IThreadFeatureData::Diameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Diameter.html) to specify the override diameter.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

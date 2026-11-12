---
title: "Planes Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "Planes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~Planes.html"
---

# Planes Property (IMirrorPartFeatureData)

Gets or sets whether to import planes.

## Syntax

### Visual Basic (Declaration)

```vb
Property Planes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.Planes = value

value = instance.Planes
```

### C#

```csharp
System.bool Planes {get; set;}
```

### C++/CLI

```cpp
property System.bool Planes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import planes, false to not

## VBA Syntax

See [MirrorPartFeatureData::Planes](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~Planes.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

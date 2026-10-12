---
title: "SolidBodies Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "SolidBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SolidBodies.html"
---

# SolidBodies Property (IMirrorPartFeatureData)

Gets or sets whether to import solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.SolidBodies = value

value = instance.SolidBodies
```

### C#

```csharp
System.bool SolidBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import solid bodies, false to not

## VBA Syntax

See [MirrorPartFeatureData::SolidBodies](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~SolidBodies.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

---
title: "Axes Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "Axes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~Axes.html"
---

# Axes Property (IMirrorPartFeatureData)

Gets or sets whether to import axes.

## Syntax

### Visual Basic (Declaration)

```vb
Property Axes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.Axes = value

value = instance.Axes
```

### C#

```csharp
System.bool Axes {get; set;}
```

### C++/CLI

```cpp
property System.bool Axes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import axes, false to not

## VBA Syntax

See [MirrorPartFeatureData::Axes](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~Axes.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

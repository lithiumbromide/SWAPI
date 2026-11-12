---
title: "ReverseDirection Property (IGroundPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGroundPlaneFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (IGroundPlaneFeatureData)

Gets or sets whether to reverse direction of alignment in this ground plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGroundPlaneFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the alignment of assembly faces relative to the ground plane, false to not

## VBA Syntax

See [GroundPlaneFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~GroundPlaneFeatureData~ReverseDirection.html).

## See Also

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html)
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

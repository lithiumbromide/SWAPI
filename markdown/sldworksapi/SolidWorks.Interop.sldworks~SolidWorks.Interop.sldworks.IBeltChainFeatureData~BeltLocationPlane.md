---
title: "BeltLocationPlane Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "BeltLocationPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLocationPlane.html"
---

# BeltLocationPlane Property (IBeltChainFeatureData)

Gets and sets the belt location plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeltLocationPlane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Object

instance.BeltLocationPlane = value

value = instance.BeltLocationPlane
```

### C#

```csharp
System.object BeltLocationPlane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BeltLocationPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [BeltChainFeatureData::BeltLocationPlane](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~BeltLocationPlane.html).

## Remarks

The belt sketch plane is normal to the pulley axes.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

---
title: "HatchType Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "HatchType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~HatchType.html"
---

# HatchType Property (IFaceHatch)

Gets or sets the type of this face hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property HatchType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Integer

instance.HatchType = value

value = instance.HatchType
```

### C#

```csharp
System.int HatchType {get; set;}
```

### C++/CLI

```cpp
property System.int HatchType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of face hatch as defined in [swAreaHatchFillStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAreaHatchFillStyle_e.html)

## VBA Syntax

See [FaceHatch::HatchType](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~HatchType.html).

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

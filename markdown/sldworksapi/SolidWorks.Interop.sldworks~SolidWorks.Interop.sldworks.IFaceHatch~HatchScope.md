---
title: "HatchScope Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "HatchScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~HatchScope.html"
---

# HatchScope Property (IFaceHatch)

Gets or sets the scope for this face hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property HatchScope As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Integer

instance.HatchScope = value

value = instance.HatchScope
```

### C#

```csharp
System.int HatchScope {get; set;}
```

### C++/CLI

```cpp
property System.int HatchScope {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hatch scope as defined in [swAreaHatchingScope_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAreaHatchingScope_e.html)

## VBA Syntax

See [FaceHatch::HatchScope](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~HatchScope.html).

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

---
title: "ShaftFit Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "ShaftFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~ShaftFit.html"
---

# ShaftFit Property (IStraightElementData)

Gets or sets the shaft fit for this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShaftFit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
Dim value As System.String

instance.ShaftFit = value

value = instance.ShaftFit
```

### C#

```csharp
System.string ShaftFit {get; set;}
```

### C++/CLI

```cpp
property System.String^ ShaftFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Shaft fit (see **Remarks**)

## VBA Syntax

See [StraightElementData::ShaftFit](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~ShaftFit.html).

## Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html) is set to [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard*DowelHoles.

Set this property to one of the following:

c8, c9, c11, d8, d9, d10, d11, e7, e8, e9, f6, f7, f8, g4, g5, g6, g7, h5, h6, h7, h8, h9, h10, h11, h12, h13, j5, j6, j7, j8, j9, j10, j11, k5, k6, k7, k8, k9, k10, k11, m5, m6, m7, n5, n6, n7, p5, p6, p7, r5, r6, r7, s5, s6, s7, t5, t6, t7, u5, u6, u7, v5, v6, v7, x5, x6, x7

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

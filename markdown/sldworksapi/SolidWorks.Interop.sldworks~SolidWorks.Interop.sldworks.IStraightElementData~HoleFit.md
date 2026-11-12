---
title: "HoleFit Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "HoleFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~HoleFit.html"
---

# HoleFit Property (IStraightElementData)

Gets or sets the hole fit for this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleFit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
Dim value As System.String

instance.HoleFit = value

value = instance.HoleFit
```

### C#

```csharp
System.string HoleFit {get; set;}
```

### C++/CLI

```cpp
property System.String^ HoleFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole fit (see **Remarks**)

## VBA Syntax

See [StraightElementData::HoleFit](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~HoleFit.html).

## Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html) is set to [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard*DowelHoles.

Set this property to one of the following:

C8, C9, C11, D8, D9, D10, D11, E7, E8, E9, F6, F7, F8, F9, G5, G6, G7, G8, G9, G10, H5, H6, H7, H8, H9, H10, H11, H12, H13, J6, J7, J8, J9, J10, J11, K6, K7, K8, M6, M7, M8, N6, N7, N8, N9, N10, N11, P6, P7, R7, S6, S7, T6, T7, U6, U7, V6, V7, X6, X7

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

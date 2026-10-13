---
title: "FitType Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "FitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~FitType.html"
---

# FitType Property (IStraightElementData)

Gets or sets the fit type for this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
Dim value As System.Integer

instance.FitType = value

value = instance.FitType
```

### C#

```csharp
System.int FitType {get; set;}
```

### C++/CLI

```cpp
property System.int FitType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit type as defined in [swStraightHoleFitType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightHoleFitType_e.html)

## VBA Syntax

See [StraightElementData::FitType](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~FitType.html).

## Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html) is set to [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard*ScrewClearances.

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

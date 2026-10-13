---
title: "Equation Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "Equation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.html"
---

# Equation Property (IStraightTapElementData)

Gets or sets the equation for the blind depth or offset distance of this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Equation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Integer

instance.Equation = value

value = instance.Equation
```

### C#

```csharp
System.int Equation {get; set;}
```

### C++/CLI

```cpp
property System.int Equation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Equation for the blind depth or offset distance as defined in [swStraightTapHoleEquation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightTapHoleEquation_e.html)

## VBA Syntax

See [StraightTapElementData::Equation](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~Equation.html).

## Remarks

If [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html) is set to false, and:

- [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondBlind, then this property specifies the equation for the depth of the Blind end condition. If this property is set to swStraightTapeHoleEquation_e.swStraightTapHoleEquation_UserDefinedValue, then use [IAdvancedHoleElementData::BlindDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~BlindDepth.html) to set the custom Blind depth of this hole element.
- IAdvancedHoleElementData::EndCondition is specifically set to anything other than Blind, then this property is not valid.

If IAdvancedHoleFeatureData::UseBaselineDimensions is set to true, then:

- the end condition automatically becomes swEndConditions_e.swEndCondOffsetFromSurface,

- and -

- this property specifies the equation for the offset distance. If this property is set to swStraightTapHoleEquation_e.swStraightTapHoleEquation_UserDefinedValue, then use [IAdvancedHoleElementData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.html) to set the custom offset distance of this hole element.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

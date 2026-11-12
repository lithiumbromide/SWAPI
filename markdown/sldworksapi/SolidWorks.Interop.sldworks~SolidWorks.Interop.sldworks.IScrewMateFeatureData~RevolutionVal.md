---
title: "RevolutionVal Property (IScrewMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScrewMateFeatureData"
member: "RevolutionVal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionVal.html"
---

# RevolutionVal Property (IScrewMateFeatureData)

Gets or sets either the number of revolutions one component makes for each unit length that the other component translates or the distance that one component translates for each revolution of the other component.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevolutionVal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IScrewMateFeatureData
Dim value As System.Double

instance.RevolutionVal = value

value = instance.RevolutionVal
```

### C#

```csharp
System.double RevolutionVal {get; set;}
```

### C++/CLI

```cpp
property System.double RevolutionVal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Revolution value (see **Remarks**)

## VBA Syntax

See [ScrewMateFeatureData::RevolutionVal](ms-its:sldworksapivb6.chm::/sldworks~ScrewMateFeatureData~RevolutionVal.html).

## Examples

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html) example.

## Remarks

If [IScrewMateFeatureData::RevolutionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionType.html) is set to [swScrewMateDistanceOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swScrewMateDistanceOptions_e.html):

- swDistancePerRevolution, then specify this property with the distance that one component translates for each revolution of the other component.
- swRevolutionsPerUnitLength, then specify this property with the number of revolutions of one component for each unit length that the other component translates. Set [swUserPreferencesIntegerValue_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swUnitsLinear to a unit length as defined in [swLengthUnit_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLengthUnit_e.html).

## See Also

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

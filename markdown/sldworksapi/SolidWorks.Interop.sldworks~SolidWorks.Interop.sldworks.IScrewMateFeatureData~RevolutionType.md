---
title: "RevolutionType Property (IScrewMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScrewMateFeatureData"
member: "RevolutionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionType.html"
---

# RevolutionType Property (IScrewMateFeatureData)

Gets or sets the type of revolution to specify for this screw mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevolutionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IScrewMateFeatureData
Dim value As System.Integer

instance.RevolutionType = value

value = instance.RevolutionType
```

### C#

```csharp
System.int RevolutionType {get; set;}
```

### C++/CLI

```cpp
property System.int RevolutionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of revolution as defined in [swScrewMateDistanceOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swScrewMateDistanceOptions_e.html)

## VBA Syntax

See [ScrewMateFeatureData::RevolutionType](ms-its:sldworksapivb6.chm::/sldworks~ScrewMateFeatureData~RevolutionType.html).

## Examples

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html) example.

## Remarks

If you set this property to swScrewMateDistanceOptions_e:

- swDistancePerRevolution, then specify [IScrewMateFeatureData::RevolutionVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionVal.html) with the distance that one component translates for each revolution of the other component.
- swRevolutionsPerUnitLength, then specify IScrewMateFeatureData::RevolutionVal with the number of revolutions of one component for each unit length that the other component translates.

## See Also

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

---
title: "FromToStartPoint Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "FromToStartPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.html"
---

# FromToStartPoint Property (ICosmeticWeldBeadFeatureData)

Gets or sets the position of the first weld bead with respect to the end of the selected face or edge.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromToStartPoint As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double

instance.FromToStartPoint = value

value = instance.FromToStartPoint
```

### C#

```csharp
System.double FromToStartPoint {get; set;}
```

### C++/CLI

```cpp
property System.double FromToStartPoint {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Position of the first weld bead (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::FromToStartPoint](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~FromToStartPoint.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::FromToLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.html) is true.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::FromToReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.html)
[ICosmeticWeldBeadFeatureData::FromToWeldLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

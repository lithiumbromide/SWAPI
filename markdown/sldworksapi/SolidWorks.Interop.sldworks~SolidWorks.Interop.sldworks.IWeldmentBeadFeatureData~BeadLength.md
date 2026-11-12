---
title: "BeadLength Property (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "BeadLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadLength.html"
---

# BeadLength Property (IWeldmentBeadFeatureData)

Gets or sets the length of each bead segment of the weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeadLength( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim value As System.Double

instance.BeadLength(Side) = value

value = instance.BeadLength(Side)
```

### C#

```csharp
System.double BeadLength(
   System.int Side
) {get; set;}
```

### C++/CLI

```cpp
property System.double BeadLength {
   System.double get(System.int Side);
   void set (System.int Side, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

### Property Value

Length of weld bead

## VBA Syntax

See [WeldmentBeadFeatureData::BeadLength](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~BeadLength.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

This property is only valid for intermittent or staggered types of weld beads. Use [IWeldmentBeadFeatureData::BeadType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~BeadType.html) to determine the type of weld bead.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

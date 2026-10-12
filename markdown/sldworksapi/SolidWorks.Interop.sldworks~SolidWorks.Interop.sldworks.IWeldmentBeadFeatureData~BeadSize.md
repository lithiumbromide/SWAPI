---
title: "BeadSize Property (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "BeadSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadSize.html"
---

# BeadSize Property (IWeldmentBeadFeatureData)

Gets or sets the length of the leg of the weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeadSize( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim value As System.Double

instance.BeadSize(Side) = value

value = instance.BeadSize(Side)
```

### C#

```csharp
System.double BeadSize(
   System.int Side
) {get; set;}
```

### C++/CLI

```cpp
property System.double BeadSize {
   System.double get(System.int Side);
   void set (System.int Side, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined by [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

### Property Value

Length of the leg

## VBA Syntax

See [WeldmentBeadFeatureData::BeadSize](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~BeadSize.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

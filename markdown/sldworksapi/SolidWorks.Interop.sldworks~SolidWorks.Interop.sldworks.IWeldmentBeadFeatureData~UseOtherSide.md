---
title: "UseOtherSide Property (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "UseOtherSide"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~UseOtherSide.html"
---

# UseOtherSide Property (IWeldmentBeadFeatureData)

Gets or sets whether to apply the weld bead to both sides of the intersecting faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseOtherSide As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim value As System.Boolean

instance.UseOtherSide = value

value = instance.UseOtherSide
```

### C#

```csharp
System.bool UseOtherSide {get; set;}
```

### C++/CLI

```cpp
property System.bool UseOtherSide {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply the weld bead to both sides, false to not

## VBA Syntax

See [WeldmentBeadFeatureData::UseOtherSide](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~UseOtherSide.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

This property is valid, and optional, for full length and intermittent weld beads only. Use [IWeldmentBeadFeatureData::BeadType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~BeadType.html) to determine the type of weld bead.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

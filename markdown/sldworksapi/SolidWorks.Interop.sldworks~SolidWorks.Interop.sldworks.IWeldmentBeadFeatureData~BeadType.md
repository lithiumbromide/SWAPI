---
title: "BeadType Property (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "BeadType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadType.html"
---

# BeadType Property (IWeldmentBeadFeatureData)

Gets or sets the type of weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeadType( _
   ByVal Side As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim value As System.Integer

instance.BeadType(Side) = value

value = instance.BeadType(Side)
```

### C#

```csharp
System.int BeadType(
   System.int Side
) {get; set;}
```

### C++/CLI

```cpp
property System.int BeadType {
   System.int get(System.int Side);
   void set (System.int Side, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

### Property Value

Type as defined in [swWeldBeadType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadType_e.html)

## VBA Syntax

See [WeldmentBeadFeatureData::BeadType](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~BeadType.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::UseOtherSide Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~UseOtherSide.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

---
title: "NormalCut Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "NormalCut"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut.html"
---

# NormalCut Property (IExtrudeFeatureData2)

Gets or sets whether the cut is created normal to the thickness of the sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalCut As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.NormalCut = value

value = instance.NormalCut
```

### C#

```csharp
System.bool NormalCut {get; set;}
```

### C++/CLI

```cpp
property System.bool NormalCut {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the cut is created normal to the thickness of the sheet metal part, false if not

## VBA Syntax

See [ExtrudeFeatureData2::NormalCut](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~NormalCut.html).

## Examples

[Create Cut Extrude in Sheet Metal Part (C#)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_CSharp.htm)
[Create Cut Extrude in Sheet Metal Part (VB.NET)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VBNET.htm)
[Create Cut Extrude in Sheet Metal Part (VBA)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VB.htm)

## Remarks

To optimize the geometry of the normal cut in the sheet metal part, set [IExtrudeFeatureData2::OptimizeGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry.html) to true.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision 25.0

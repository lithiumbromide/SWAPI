---
title: "OptimizeGeometry Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "OptimizeGeometry"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry.html"
---

# OptimizeGeometry Property (IExtrudeFeatureData2)

Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property OptimizeGeometry As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.OptimizeGeometry = value

value = instance.OptimizeGeometry
```

### C#

```csharp
System.bool OptimizeGeometry {get; set;}
```

### C++/CLI

```cpp
property System.bool OptimizeGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to optimize the geometry of a normal cut in a sheet metal part, false to not (see **Remarks**)

## VBA Syntax

See [ExtrudeFeatureData2::OptimizeGeometry](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~OptimizeGeometry.html).

## Examples

[Create Cut Extrude in Sheet Metal Part (C#)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_CSharp.htm)
[Create Cut Extrude in Sheet Metal Part (VB.NET)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VBNET.htm)
[Create Cut Extrude in Sheet Metal Part (VBA)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VB.htm)

## Remarks

Setting this property is only valid when [IExtrudeFeatureData2::NormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut.html) is true.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

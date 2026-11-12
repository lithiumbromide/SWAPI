---
title: "UseDefaultBendRadius Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "UseDefaultBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendRadius.html"
---

# UseDefaultBendRadius Property (IEdgeFlangeFeatureData)

Gets or sets whether to use the default sheet metal bend radius for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRadius = value

value = instance.UseDefaultBendRadius
```

### C#

```csharp
System.bool UseDefaultBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the default sheet metal bend radius of the edge flange (default), false uses a custom bend radius

## VBA Syntax

See [EdgeFlangeFeatureData::UseDefaultBendRadius](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~UseDefaultBendRadius.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2

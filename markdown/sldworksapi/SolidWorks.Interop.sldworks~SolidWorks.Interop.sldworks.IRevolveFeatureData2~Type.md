---
title: "Type Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Type.html"
---

# Type Property (IRevolveFeatureData2)

Gets or sets the revolution feature type.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of revolution as defined in [swRevolveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html)

## VBA Syntax

See [RevolveFeatureData2::Type](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~Type.html).

## Examples

[Create 360-degree Revolve Feature (VBA)](Create_360-degree_Revolve_Feature_Example_VB.htm)
[Create 360-degree Revolve Feature (VB.NET)](Create_360-degree_Revolve_Feature_Example_VBNET.htm)
[Create 360-degree Revolve Feature (C#)](Create_360-degree_Revolve_Feature_Example_CSharp.htm)

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

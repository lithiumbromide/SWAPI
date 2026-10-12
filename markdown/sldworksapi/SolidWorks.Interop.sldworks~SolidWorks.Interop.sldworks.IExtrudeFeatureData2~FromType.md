---
title: "FromType Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "FromType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.html"
---

# FromType Property (IExtrudeFeatureData2)

Gets or sets the type from which to create an extrusion.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Integer

instance.FromType = value

value = instance.FromType
```

### C#

```csharp
System.int FromType {get; set;}
```

### C++/CLI

```cpp
property System.int FromType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type from which to create an extrusion as defined in [swExtrudeFromType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExtrudeFrom_e.html)

## VBA Syntax

See [ExtrudeFeatureData2::FromType](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~FromType.html).

## Examples

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.html)
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.html)
[IExtrudeFeatureData2::SetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity.html)
[IExtrudeFeatureData2::GetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

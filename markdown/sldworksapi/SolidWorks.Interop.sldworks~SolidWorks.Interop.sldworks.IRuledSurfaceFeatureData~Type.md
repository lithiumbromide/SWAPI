---
title: "Type Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Type.html"
---

# Type Property (IRuledSurfaceFeatureData)

Gets or sets the type of ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
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

Type of ruled-surface feature as defined in [swRuledSurfaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRuledSurfaceType_e.html)

## VBA Syntax

See [RuledSurfaceFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~Type.html).

## Examples

[Get Ruled-Surface Feature Data (VBA)](Get_Ruled_Surface_Feature_Data_Example_VB.htm)
[Get Ruled-Surface Feature Data (VB.NET)](Get_Ruled_Surface_Feature_Data_Example_VBNET.htm)
[Get Ruled-Surface Feature Data (C#)](Get_Ruled_Surface_Feature_Data_Example_CSharp.htm)

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~GetDirectionReference.html)
[IRuledSurfaceFeatureData::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Angle.html)
[IRuledSurfaceFeatureData::DirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~DirectionVector.html)
[IRuledSurfaceFeatureData::UseVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~UseVector.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "LinkToThickness Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "LinkToThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~LinkToThickness.html"
---

# LinkToThickness Property (IExtrudeFeatureData2)

Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.LinkToThickness = value

value = instance.LinkToThickness
```

### C#

```csharp
System.bool LinkToThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link the depth of an extruded boss to the thickness of the base feature, false to not

## VBA Syntax

See [ExtrudeFeatureData2::LinkToThickness](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~LinkToThickness.html).

## Remarks

This property applies to [sheet metal parts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData.html) only.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

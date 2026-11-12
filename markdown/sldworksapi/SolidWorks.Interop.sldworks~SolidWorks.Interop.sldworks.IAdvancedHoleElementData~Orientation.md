---
title: "Orientation Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "Orientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Orientation.html"
---

# Orientation Property (IAdvancedHoleElementData)

Gets or sets the orientation of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Orientation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Integer

instance.Orientation = value

value = instance.Orientation
```

### C#

```csharp
System.int Orientation {get; set;}
```

### C++/CLI

```cpp
property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Orientation as defined in [swHoleElementOrientation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHoleElementOrientation_e.html) (see **Remarks**)

## VBA Syntax

See [AdvancedHoleElementData::Orientation](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~Orientation.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

This property is not valid if [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.html) is set to [swAdvWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html):

- swAdvWzdStraight
- swAdvWzdStraightTap

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

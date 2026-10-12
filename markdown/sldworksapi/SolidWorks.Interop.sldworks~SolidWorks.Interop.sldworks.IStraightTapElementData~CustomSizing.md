---
title: "CustomSizing Property (IStraightTapElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightTapElementData"
member: "CustomSizing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~CustomSizing.html"
---

# CustomSizing Property (IStraightTapElementData)

Gets or sets the custom sizing for this straight tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomSizing As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightTapElementData
Dim value As System.Integer

instance.CustomSizing = value

value = instance.CustomSizing
```

### C#

```csharp
System.int CustomSizing {get; set;}
```

### C++/CLI

```cpp
property System.int CustomSizing {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Custom sizing as defined in [swStraightTapHoleCustomSizing_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightTapHoleCustomSizing_e.html)

## VBA Syntax

See [StraightTapElementData::CustomSizing](ms-its:sldworksapivb6.chm::/sldworks~StraightTapElementData~CustomSizing.html).

## Examples

See the [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html) examples.

## See Also

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

---
title: "CustomSizing Property (ITaperedTapElementData)"
project: "SOLIDWORKS API Help"
interface: "ITaperedTapElementData"
member: "CustomSizing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~CustomSizing.html"
---

# CustomSizing Property (ITaperedTapElementData)

Gets or sets the custom sizing for this tapered tap hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomSizing As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITaperedTapElementData
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

Custom sizing as defined in [swTaperedTapCustomSizing_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTaperedTapCustomSizing_e.html)

## VBA Syntax

See [TaperedTapElementData::CustomSizing](ms-its:sldworksapivb6.chm::/sldworks~TaperedTapElementData~CustomSizing.html).

## Examples

See the [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html) examples.

## See Also

[ITaperedTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)
[ITaperedTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

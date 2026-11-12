---
title: "FastenerType Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "FastenerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html"
---

# FastenerType Property (IAdvancedHoleElementData)

Gets or sets the fastener type for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property FastenerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Integer

instance.FastenerType = value

value = instance.FastenerType
```

### C#

```csharp
System.int FastenerType {get; set;}
```

### C++/CLI

```cpp
property System.int FastenerType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole fastener type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

## VBA Syntax

See [AdvancedHoleElementData::FastenerType](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~FastenerType.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

The hole fastener must match the [IAdvancedHoleElementData::Standard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Standard.html) and be appropriate for the [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.html), or an error occurs.

If [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.html) is set to [swAdvWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html).swAdvWzdTaperTap, then this property gets and sets only swWzdHoleStandardFastenerTypes_e.*TaperedPipeTap.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

---
title: "ElementType Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "ElementType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.html"
---

# ElementType Property (IAdvancedHoleElementData)

Gets the type of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ElementType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Integer

value = instance.ElementType
```

### C#

```csharp
System.int ElementType {get;}
```

### C++/CLI

```cpp
property System.int ElementType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Advanced Hole element type as defined in [swAdvWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html)

## VBA Syntax

See [AdvancedHoleElementData::ElementType](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~ElementType.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[IAdvancedHoleElementData::Orientation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Orientation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

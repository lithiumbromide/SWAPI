---
title: "Standard Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "Standard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Standard.html"
---

# Standard Property (IAdvancedHoleElementData)

Gets or sets the hole standard used for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Standard As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Integer

instance.Standard = value

value = instance.Standard
```

### C#

```csharp
System.int Standard {get; set;}
```

### C++/CLI

```cpp
property System.int Standard {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole standard as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandards_e.html)

## VBA Syntax

See [AdvancedHoleElementData::Standard](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~Standard.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

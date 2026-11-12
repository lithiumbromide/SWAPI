---
title: "Diameter Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "Diameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Diameter.html"
---

# Diameter Property (IAdvancedHoleElementData)

Gets or sets the diameter of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property Diameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Double

instance.Diameter = value

value = instance.Diameter
```

### C#

```csharp
System.double Diameter {get; set;}
```

### C++/CLI

```cpp
property System.double Diameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of the Advanced Hole

## VBA Syntax

See [AdvancedHoleElementData::Diameter](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~Diameter.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

This property is valid only if [IAdvancedHoleElementData::DiameterOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~DiameterOverride.html) is set to true.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

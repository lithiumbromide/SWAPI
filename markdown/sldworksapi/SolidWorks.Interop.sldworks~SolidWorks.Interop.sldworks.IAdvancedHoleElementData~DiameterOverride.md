---
title: "DiameterOverride Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "DiameterOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~DiameterOverride.html"
---

# DiameterOverride Property (IAdvancedHoleElementData)

Gets or sets whether to override the diameter of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property DiameterOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Boolean

instance.DiameterOverride = value

value = instance.DiameterOverride
```

### C#

```csharp
System.bool DiameterOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool DiameterOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the diameter, false to not

## VBA Syntax

See [AdvancedHoleElementData::DiameterOverride](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~DiameterOverride.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[IAdvancedHoleElementData::Diameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Diameter.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

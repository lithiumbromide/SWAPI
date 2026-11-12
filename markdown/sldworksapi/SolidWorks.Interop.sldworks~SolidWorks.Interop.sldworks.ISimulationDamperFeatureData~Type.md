---
title: "Type Property (ISimulationDamperFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationDamperFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~Type.html"
---

# Type Property (ISimulationDamperFeatureData)

Gets the type of damper.

**NOTE: This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationDamperFeatureData
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of damper as defined in [swSimulationDamperType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationDamperType_e.html)

## VBA Syntax

See [SimulationDamperFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~SimulationDamperFeatureData~Type.html).

## Examples

See [ISimulationDamperFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationDamperFeatureData.html) examples.

## See Also

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

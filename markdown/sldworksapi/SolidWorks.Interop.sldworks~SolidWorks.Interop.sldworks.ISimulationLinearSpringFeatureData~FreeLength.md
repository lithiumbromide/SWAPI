---
title: "FreeLength Property (ISimulationLinearSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationLinearSpringFeatureData"
member: "FreeLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~FreeLength.html"
---

# FreeLength Property (ISimulationLinearSpringFeatureData)

Obsolete. Superseded by [ISimulationSpringFeatureData::FreeLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FreeLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationLinearSpringFeatureData
Dim value As System.Double

instance.FreeLength = value

value = instance.FreeLength
```

### C#

```csharp
System.double FreeLength {get; set;}
```

### C++/CLI

```cpp
property System.double FreeLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length

## VBA Syntax

See [SimulationLinearSpringFeatureData::FreeLength](ms-its:sldworksapivb6.chm::/sldworks~SimulationLinearSpringFeatureData~FreeLength.html).

## See Also

[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.html)
[ISimulationLinearSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

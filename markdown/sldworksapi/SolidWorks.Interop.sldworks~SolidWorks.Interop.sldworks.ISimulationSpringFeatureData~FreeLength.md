---
title: "FreeLength Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "FreeLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.html"
---

# FreeLength Property (ISimulationSpringFeatureData)

Gets or sets the free length (i.e., length to stretch or compress the spring) for the functional expression for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FreeLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
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

Free length

## VBA Syntax

See [SimulationSpringFeatureData::FreeLength](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~FreeLength.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## Remarks

The initial distance is the distance between the parts as currently displayed in the graphics area. Call [ISimulationSpringFeatureData::UpdateToModelChanges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~UpdateToModelChanges.html) to have the free length dynamically update to model changes while the PropertyManager page is open.

The spring does not exert any force when its length is equal to its free length.

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.html)
[ISimulationSpringFeatureData::ExponentOfSpringForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.html)
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.html)
[ISimulationSpringFeatureData::SpringConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

---
title: "ICWRadiation Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html"
---

# ICWRadiation Interface

Allows access to the radiation object used for steady state and transient thermal studies only.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWRadiation
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
```

### C#

```csharp
public interface ICWRadiation
```

### C++/CLI

```cpp
public interface class ICWRadiation
```

## VBA Syntax

See [CWRadiation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

Radiation properties can vary with time and temperature for transient studies.

Radiation is a nonlinear phenomenon, and calculations can take a long time.

View factors are calculated considering blocking effects automatically.

## Accessors

[ICWLoadsAndRestraintsManager::AddRadiation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRadiation.html)

## See Also

[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)

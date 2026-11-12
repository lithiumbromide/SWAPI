---
title: "RemoveAllPinConnectors Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveAllPinConnectors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllPinConnectors.html"
---

# RemoveAllPinConnectors Method (ICWMassPropertiesManager)

Removes all pin connectors from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllPinConnectors() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Integer

value = instance.RemoveAllPinConnectors()
```

### C#

```csharp
System.int RemoveAllPinConnectors()
```

### C++/CLI

```cpp
System.int RemoveAllPinConnectors();
```

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveAllPinConnectors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveAllPinConnectors.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemovePinConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemovePinConnectors.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

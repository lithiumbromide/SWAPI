---
title: "RemoveAllBoltConnectors Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveAllBoltConnectors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllBoltConnectors.html"
---

# RemoveAllBoltConnectors Method (ICWMassPropertiesManager)

Removes all bolt connectors from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllBoltConnectors() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Integer

value = instance.RemoveAllBoltConnectors()
```

### C#

```csharp
System.int RemoveAllBoltConnectors()
```

### C++/CLI

```cpp
System.int RemoveAllBoltConnectors();
```

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveAllBoltConnectors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveAllBoltConnectors.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveBoltConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveBoltConnectors.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

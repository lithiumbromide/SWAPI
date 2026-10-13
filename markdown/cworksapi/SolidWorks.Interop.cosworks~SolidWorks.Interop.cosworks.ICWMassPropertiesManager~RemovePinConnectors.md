---
title: "RemovePinConnectors Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemovePinConnectors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemovePinConnectors.html"
---

# RemovePinConnectors Method (ICWMassPropertiesManager)

Removes the specified pin connectors from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemovePinConnectors( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.RemovePinConnectors(NameArray)
```

### C#

```csharp
System.int RemovePinConnectors(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int RemovePinConnectors(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of the names of pin connectors to remove

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemovePinConnectors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemovePinConnectors.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllPinConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllPinConnectors.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

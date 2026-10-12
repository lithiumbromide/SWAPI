---
title: "RemoveBoltConnectors Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveBoltConnectors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveBoltConnectors.html"
---

# RemoveBoltConnectors Method (ICWMassPropertiesManager)

Removes the specified bolt connectors from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveBoltConnectors( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.RemoveBoltConnectors(NameArray)
```

### C#

```csharp
System.int RemoveBoltConnectors(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int RemoveBoltConnectors(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of the names of bolt connectors to remove

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveBoltConnectors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveBoltConnectors.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllBoltConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllBoltConnectors.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

---
title: "AddPinConnectors Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddPinConnectors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddPinConnectors.html"
---

# AddPinConnectors Method (ICWMassPropertiesManager)

Adds the specified pin connectors to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPinConnectors( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.AddPinConnectors(NameArray)
```

### C#

```csharp
System.int AddPinConnectors(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int AddPinConnectors(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of names of pin connectors

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddPinConnectors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddPinConnectors.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

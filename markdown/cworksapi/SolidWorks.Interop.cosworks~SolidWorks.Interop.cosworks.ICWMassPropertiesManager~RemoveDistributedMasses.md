---
title: "RemoveDistributedMasses Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveDistributedMasses"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveDistributedMasses.html"
---

# RemoveDistributedMasses Method (ICWMassPropertiesManager)

Removes the specified distributed masses from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveDistributedMasses( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.RemoveDistributedMasses(NameArray)
```

### C#

```csharp
System.int RemoveDistributedMasses(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int RemoveDistributedMasses(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of the names of distributed masses to remove

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveDistributedMasses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveDistributedMasses.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllDistributedMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllDistributedMasses.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

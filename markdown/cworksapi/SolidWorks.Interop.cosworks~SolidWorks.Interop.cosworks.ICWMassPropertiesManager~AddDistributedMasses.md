---
title: "AddDistributedMasses Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddDistributedMasses"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddDistributedMasses.html"
---

# AddDistributedMasses Method (ICWMassPropertiesManager)

Adds the specified distributed masses to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDistributedMasses( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.AddDistributedMasses(NameArray)
```

### C#

```csharp
System.int AddDistributedMasses(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int AddDistributedMasses(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of names of distributed masses

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddDistributedMasses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddDistributedMasses.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::AddBodies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddBodies.html)
[ICWMassPropertiesManager::AddBoltConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddBoltConnectors.html)
[ICWMassPropertiesManager::AddPinConnectors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddPinConnectors.html)
[ICWMassPropertiesManager::AddRemoteLoadMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddRemoteLoadMasses.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

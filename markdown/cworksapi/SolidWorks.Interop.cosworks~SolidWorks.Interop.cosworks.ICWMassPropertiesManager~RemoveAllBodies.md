---
title: "RemoveAllBodies Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveAllBodies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllBodies.html"
---

# RemoveAllBodies Method (ICWMassPropertiesManager)

Removes all bodies from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllBodies() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Integer

value = instance.RemoveAllBodies()
```

### C#

```csharp
System.int RemoveAllBodies()
```

### C++/CLI

```cpp
System.int RemoveAllBodies();
```

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveAllBodies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveAllBodies.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveBodies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveBodies.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

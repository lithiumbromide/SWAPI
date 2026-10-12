---
title: "RemoveAllCables Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveAllCables"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllCables.html"
---

# RemoveAllCables Method (ICWMassPropertiesManager)

Removes all cables from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllCables() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Integer

value = instance.RemoveAllCables()
```

### C#

```csharp
System.int RemoveAllCables()
```

### C++/CLI

```cpp
System.int RemoveAllCables();
```

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveAllCables](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveAllCables.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::AddCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddCables.html)
[ICWMassPropertiesManager::RemoveCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveCables.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0

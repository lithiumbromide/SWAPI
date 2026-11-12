---
title: "RemoveAllRemoteLoadMasses Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveAllRemoteLoadMasses"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllRemoteLoadMasses.html"
---

# RemoveAllRemoteLoadMasses Method (ICWMassPropertiesManager)

Removes all remote load masses from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllRemoteLoadMasses() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim value As System.Integer

value = instance.RemoveAllRemoteLoadMasses()
```

### C#

```csharp
System.int RemoveAllRemoteLoadMasses()
```

### C++/CLI

```cpp
System.int RemoveAllRemoteLoadMasses();
```

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveAllRemoteLoadMasses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveAllRemoteLoadMasses.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveRemoteLoadMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveRemoteLoadMasses.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

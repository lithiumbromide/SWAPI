---
title: "RemoveRemoteLoadMasses Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveRemoteLoadMasses"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveRemoteLoadMasses.html"
---

# RemoveRemoteLoadMasses Method (ICWMassPropertiesManager)

Removes the specified remote load masses from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveRemoteLoadMasses( _
   ByVal NameArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NameArray As System.Object
Dim value As System.Integer

value = instance.RemoveRemoteLoadMasses(NameArray)
```

### C#

```csharp
System.int RemoveRemoteLoadMasses(
   System.object NameArray
)
```

### C++/CLI

```cpp
System.int RemoveRemoteLoadMasses(
   System.Object^ NameArray
)
```

### Parameters

- `NameArray`: Array of the names of remote load masses to remove

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveRemoteLoadMasses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveRemoteLoadMasses.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllRemoteLoadMasses Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllRemoteLoadMasses.html)
[ICWMassPropertiesManager::ClearAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~ClearAll.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

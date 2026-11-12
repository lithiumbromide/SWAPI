---
title: "RemoveLinkageRods Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveLinkageRods"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveLinkageRods.html"
---

# RemoveLinkageRods Method (ICWMassPropertiesManager)

Removes the specified linkage rod connectors.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveLinkageRods( _
   ByVal NamesArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NamesArray As System.Object
Dim value As System.Integer

value = instance.RemoveLinkageRods(NamesArray)
```

### C#

```csharp
System.int RemoveLinkageRods(
   System.object NamesArray
)
```

### C++/CLI

```cpp
System.int RemoveLinkageRods(
   System.Object^ NamesArray
)
```

### Parameters

- `NamesArray`: Array of the names of linkage rod connectors to remove

### Return Value

Error code as defined by [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveLinkageRods](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveLinkageRods.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0

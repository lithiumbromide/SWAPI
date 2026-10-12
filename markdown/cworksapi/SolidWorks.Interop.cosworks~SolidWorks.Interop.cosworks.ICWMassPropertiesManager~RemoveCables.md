---
title: "RemoveCables Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "RemoveCables"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveCables.html"
---

# RemoveCables Method (ICWMassPropertiesManager)

Removes the specified cables from the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCables( _
   ByVal NamesArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NamesArray As System.Object
Dim value As System.Integer

value = instance.RemoveCables(NamesArray)
```

### C#

```csharp
System.int RemoveCables(
   System.object NamesArray
)
```

### C++/CLI

```cpp
System.int RemoveCables(
   System.Object^ NamesArray
)
```

### Parameters

- `NamesArray`: Array of names of cables

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::RemoveCables](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~RemoveCables.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::AddCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddCables.html)
[ICWMassPropertiesManager::RemoveAllCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllCables.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0

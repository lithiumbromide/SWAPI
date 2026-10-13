---
title: "AddCables Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddCables"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddCables.html"
---

# AddCables Method (ICWMassPropertiesManager)

Adds the specified cables to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCables( _
   ByVal NamesArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NamesArray As System.Object
Dim value As System.Integer

value = instance.AddCables(NamesArray)
```

### C#

```csharp
System.int AddCables(
   System.object NamesArray
)
```

### C++/CLI

```cpp
System.int AddCables(
   System.Object^ NamesArray
)
```

### Parameters

- `NamesArray`: Array of names of cables

### Return Value

Error code as defined in [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddCables](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddCables.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)
[ICWMassPropertiesManager::RemoveAllCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveAllCables.html)
[ICWMassPropertiesManager::RemoveCables Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~RemoveCables.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0

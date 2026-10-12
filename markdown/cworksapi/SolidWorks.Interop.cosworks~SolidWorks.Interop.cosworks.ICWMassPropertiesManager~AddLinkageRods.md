---
title: "AddLinkageRods Method (ICWMassPropertiesManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMassPropertiesManager"
member: "AddLinkageRods"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager~AddLinkageRods.html"
---

# AddLinkageRods Method (ICWMassPropertiesManager)

Adds the specified linkage rod connectors to the calculation of mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLinkageRods( _
   ByVal NamesArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMassPropertiesManager
Dim NamesArray As System.Object
Dim value As System.Integer

value = instance.AddLinkageRods(NamesArray)
```

### C#

```csharp
System.int AddLinkageRods(
   System.object NamesArray
)
```

### C++/CLI

```cpp
System.int AddLinkageRods(
   System.Object^ NamesArray
)
```

### Parameters

- `NamesArray`: Array of the names of linkage rod connectors to add to the mass properties calculation

### Return Value

Error code as defined by [swsSimMassPropertiesError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimMassPropertiesError_e.html)

## VBA Syntax

See [CWMassPropertiesManager::AddLinkageRods](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMassPropertiesManager~AddLinkageRods.html).

## See Also

[ICWMassPropertiesManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)
[ICWMassPropertiesManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0

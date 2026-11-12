---
title: "RemoveEntity Method (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~RemoveEntity.html"
---

# RemoveEntity Method (ICWTemperature)

Removes the entity at the specified index to which to apply the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
Dim NIndex As System.Integer

instance.RemoveEntity(NIndex)
```

### C#

```csharp
void RemoveEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of the entity to remove

## VBA Syntax

See [CWTemperature::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~RemoveEntity.html).

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)
[ICWTemperature::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

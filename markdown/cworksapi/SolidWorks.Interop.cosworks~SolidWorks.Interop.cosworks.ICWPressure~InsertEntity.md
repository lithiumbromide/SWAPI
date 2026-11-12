---
title: "InsertEntity Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~InsertEntity.html"
---

# InsertEntity Method (ICWPressure)

Inserts a face to which to apply this pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim DispEntity As System.Object

instance.InsertEntity(DispEntity)
```

### C#

```csharp
void InsertEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Face entity

## VBA Syntax

See [CWPressure::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~InsertEntity.html).

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

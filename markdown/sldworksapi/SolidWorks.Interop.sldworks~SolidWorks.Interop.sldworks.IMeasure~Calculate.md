---
title: "Calculate Method (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Calculate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Calculate.html"
---

# Calculate Method (IMeasure)

Measures the selected or specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function Calculate( _
   ByVal Entities As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim Entities As System.Object
Dim value As System.Boolean

value = instance.Calculate(Entities)
```

### C#

```csharp
System.bool Calculate(
   System.object Entities
)
```

### C++/CLI

```cpp
System.bool Calculate(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of entities to measure; if NULL, then this method measures the selected entities

### Return Value

True if the specified or selected entities are valid types and combination , false if not

## VBA Syntax

See [Measure::Calculate](ms-its:sldworksapivb6.chm::/sldworks~Measure~Calculate.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

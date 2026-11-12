---
title: "IGetBodies Method (CostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "CostPart"
member: "IGetBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart~IGetBodies.html"
---

# IGetBodies Method (CostPart)

Gets the Costing bodies in this Costing part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodies( _
   ByVal NumBodies As System.Integer _
) As CostBody
```

### Visual Basic (Usage)

```vb
Dim instance As CostPart
Dim NumBodies As System.Integer
Dim value As CostBody

value = instance.IGetBodies(NumBodies)
```

### C#

```csharp
CostBody IGetBodies(
   System.int NumBodies
)
```

### C++/CLI

```cpp
CostBody^ IGetBodies(
   System.int NumBodies
)
```

### Parameters

- `NumBodies`: Number of Costing bodies

### Return Value

- in-process, unmanaged C++: Pointer to an array of [Costing bodies](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostPart::GetBodyCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart~GetBodyCount.html) to get the NumBodies value.

## See Also

[CostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart.html)
[CostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostPart_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0

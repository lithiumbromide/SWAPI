---
title: "IGetBodies Method (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "IGetBodies"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~IGetBodies.html"
---

# IGetBodies Method (ICostPart)

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
Dim instance As ICostPart
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

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)
[ICostPart::GetBodies Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetBodies.html)

## Availability

SOLIDWORKS Costing API 2013 SP0

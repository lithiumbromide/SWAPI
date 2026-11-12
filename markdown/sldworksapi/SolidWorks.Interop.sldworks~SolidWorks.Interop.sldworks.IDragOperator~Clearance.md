---
title: "Clearance Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "Clearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Clearance.html"
---

# Clearance Property (IDragOperator)

Gets the clearance distance between the components.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Clearance( _
   ByVal NIndex As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim NIndex As System.Integer
Dim value As System.Double

value = instance.Clearance(NIndex)
```

### C#

```csharp
System.double Clearance(
   System.int NIndex
) {get;}
```

### C++/CLI

```cpp
property System.double Clearance {
   System.double get(System.int NIndex);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NIndex`: Index of the components

### Property Value

Clearance value

## VBA Syntax

See [DragOperator::Clearance](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~Clearance.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

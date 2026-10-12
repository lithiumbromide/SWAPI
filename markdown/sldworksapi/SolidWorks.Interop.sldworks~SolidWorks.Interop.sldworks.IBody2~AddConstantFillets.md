---
title: "AddConstantFillets Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddConstantFillets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddConstantFillets.html"
---

# AddConstantFillets Method (IBody2)

Creates constant radius fillets on the specified edges on this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConstantFillets( _
   ByVal Radius As System.Double, _
   ByVal EdgesToFillet As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Radius As System.Double
Dim EdgesToFillet As System.Object
Dim value As System.Object

value = instance.AddConstantFillets(Radius, EdgesToFillet)
```

### C#

```csharp
System.object AddConstantFillets(
   System.double Radius,
   System.object EdgesToFillet
)
```

### C++/CLI

```cpp
System.Object^ AddConstantFillets(
   System.double Radius,
   System.Object^ EdgesToFillet
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`: Fillet radius
- `EdgesToFillet`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to fillet

### Return Value

Array of newly created [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Body2::AddConstantFillets](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddConstantFillets.html).

## Remarks

This method does not work for sheet bodies.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14

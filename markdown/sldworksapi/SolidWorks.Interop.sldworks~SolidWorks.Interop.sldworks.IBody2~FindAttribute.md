---
title: "FindAttribute Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "FindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.html"
---

# FindAttribute Method (IBody2)

Finds an attribute on a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute

value = instance.FindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
Attribute FindAttribute(
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
Attribute^ FindAttribute(
   AttributeDef^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`: Pointer to the [attribute definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html) that you want to find
- `WhichOne`: Instance number of this type on the body (0, 1, 2, 3, and so on)

### Return Value

Pointer to the [attribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) instance

## VBA Syntax

See [Body2::FindAttribute](ms-its:sldworksapivb6.chm::/sldworks~Body2~FindAttribute.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

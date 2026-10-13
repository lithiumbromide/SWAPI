---
title: "IFindAttribute Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IFindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute.html"
---

# IFindAttribute Method (IComponent2)

Finds an attribute on a component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute

value = instance.IFindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
Attribute IFindAttribute(
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
Attribute^ IFindAttribute(
   AttributeDef^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`: Pointer to an [attribute definition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html) that you are looking for on this component
- `WhichOne`: Index number of the attribute that you want to return; there might be several attributes on this component

### Return Value

Pointer to the [attribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

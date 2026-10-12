---
title: "FindAttribute Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "FindAttribute"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.html"
---

# FindAttribute Method (IComponent2)

Finds an attribute on a component.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindAttribute( _
   ByVal AttributeDef As System.Object, _
   ByVal WhichOne As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim AttributeDef As System.Object
Dim WhichOne As System.Integer
Dim value As System.Object

value = instance.FindAttribute(AttributeDef, WhichOne)
```

### C#

```csharp
System.object FindAttribute(
   System.object AttributeDef,
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.Object^ FindAttribute(
   System.Object^ AttributeDef,
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttributeDef`: Attribute definition that you are looking for on this component
- `WhichOne`: Index number of the attribute that you want to return; there might be several attributes
  on this component

### Return Value

Pointer to the [attribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html)

## VBA Syntax

See [Component2::FindAttribute](ms-its:sldworksapivb6.chm::/sldworks~Component2~FindAttribute.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

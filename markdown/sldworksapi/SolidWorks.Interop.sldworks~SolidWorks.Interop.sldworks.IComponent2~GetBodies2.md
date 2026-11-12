---
title: "GetBodies2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.html"
---

# GetBodies2 Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBodies3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies2( _
   ByVal BodyType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As System.Object

value = instance.GetBodies2(BodyType)
```

### C#

```csharp
System.object GetBodies2(
   System.int BodyType
)
```

### C++/CLI

```cpp
System.Object^ GetBodies2(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined by [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in the component

## VBA Syntax

See [Component2::GetBodies2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetBodies2.html).

## Remarks

This method only supports solid and sheet (surface) types and part components.

The difference between this method and the now obsolete IComponent2::GetBodies is that the new method supports lightweight components. The now obsolete IComponent2::GetBodies does not.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2

---
title: "DefineType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "DefineType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~DefineType.html"
---

# DefineType Property (ISpring)

Gets or sets how the number of revolutions, pitch, and height of the spring are defined.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefineType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.DefineType = value

value = instance.DefineType
```

### C#

```csharp
System.int DefineType {get; set;}
```

### C++/CLI

```cpp
property System.int DefineType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How the number of revolutions, pitch, and height of spring are defined as defined in [swSpringDefineType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringDefineType_e.html)

## VBA Syntax

See [Spring::DefineType](ms-its:sldworksapivb6.chm::/sldworks~Spring~DefineType.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::SpringType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SpringType.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1

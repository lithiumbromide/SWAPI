---
title: "SpringType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "SpringType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SpringType.html"
---

# SpringType Property (ISpring)

Gets or sets the type of parameters that define the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpringType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.SpringType = value

value = instance.SpringType
```

### C#

```csharp
System.int SpringType {get; set;}
```

### C++/CLI

```cpp
property System.int SpringType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of parameters that define the spring as defined in [swSpringType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringType_e.html)

## VBA Syntax

See [Spring::SpringType](ms-its:sldworksapivb6.chm::/sldworks~Spring~SpringType.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::DefineType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~DefineType.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1

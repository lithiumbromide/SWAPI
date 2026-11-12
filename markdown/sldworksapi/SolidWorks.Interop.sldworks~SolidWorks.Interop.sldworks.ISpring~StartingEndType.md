---
title: "StartingEndType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "StartingEndType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType.html"
---

# StartingEndType Property (ISpring)

Gets or sets the starting end type for either an extension spring or a torsion spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingEndType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.StartingEndType = value

value = instance.StartingEndType
```

### C#

```csharp
System.int StartingEndType {get; set;}
```

### C++/CLI

```cpp
property System.int StartingEndType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Starting end type as defined in [swSpringExtensionEndType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringExtensionEndType_e.html) for an extension spring or [swSpringTorsionEndType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringTorsionEndType_e.html) for a torsion spring

## VBA Syntax

See [Spring::StartingEndType](ms-its:sldworksapivb6.chm::/sldworks~Spring~StartingEndType.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::StartingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength.html)
[ISpring::EndingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.html)
[ISpring::EndingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1

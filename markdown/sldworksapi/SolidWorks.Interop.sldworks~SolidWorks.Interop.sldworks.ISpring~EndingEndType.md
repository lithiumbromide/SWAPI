---
title: "EndingEndType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "EndingEndType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.html"
---

# EndingEndType Property (ISpring)

Gets or sets the ending end type for either an extension spring or a torsion spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndingEndType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.EndingEndType = value

value = instance.EndingEndType
```

### C#

```csharp
System.int EndingEndType {get; set;}
```

### C++/CLI

```cpp
property System.int EndingEndType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ending end type as defined in [swSpringExtensionEndType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringExtensionEndType_e.html) for an extension spring or [swSpringTorsionEndType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringTorsionEndType_e.html) for a torsion spring

## VBA Syntax

See [Spring::EndingEndType](ms-its:sldworksapivb6.chm::/sldworks~Spring~EndingEndType.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::StartingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType.html)
[ISpring::StartingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength.html)
[ISpring::EndingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1

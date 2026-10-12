---
title: "CreateSpring Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSpring"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSpring.html"
---

# CreateSpring Method (IModeler)

Creates the geometry for a spring.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpring() As Spring
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim value As Spring

value = instance.CreateSpring()
```

### C#

```csharp
Spring CreateSpring()
```

### C++/CLI

```cpp
Spring^ CreateSpring();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Spring](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring.html)

## VBA Syntax

See [Modeler::CreateSpring](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSpring.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1

---
title: "ApplicationType Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ApplicationType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ApplicationType.html"
---

# ApplicationType Property (ISldWorks)

Gets the type of this SOLIDWORKS application.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ApplicationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.ApplicationType
```

### C#

```csharp
System.int ApplicationType {get;}
```

### C++/CLI

```cpp
property System.int ApplicationType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of application as defined by [swApplicationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swApplicationType_e.html)

## VBA Syntax

See [SldWorks::ApplicationType](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ApplicationType.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1

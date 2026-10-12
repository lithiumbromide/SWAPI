---
title: "IActiveDoc Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IActiveDoc"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc.html"
---

# IActiveDoc Property (ISldWorks)

Obsolete. Superseded by [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IActiveDoc As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As ModelDoc

value = instance.IActiveDoc
```

### C#

```csharp
ModelDoc IActiveDoc {get;}
```

### C++/CLI

```cpp
property ModelDoc^ IActiveDoc {
   ModelDoc^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SldWorks::IActiveDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IActiveDoc.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

---
title: "IActivateDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IActivateDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc.html"
---

# IActivateDoc Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::ActivateDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) and [ISldWorks::IActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActivateDoc3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IActivateDoc( _
   ByVal Name As System.String _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim value As ModelDoc

value = instance.IActivateDoc(Name)
```

### C#

```csharp
ModelDoc IActivateDoc(
   System.string Name
)
```

### C++/CLI

```cpp
ModelDoc^ IActivateDoc(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [SldWorks::IActivateDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IActivateDoc.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

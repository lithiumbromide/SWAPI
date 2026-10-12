---
title: "IActivateDoc2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IActivateDoc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc2.html"
---

# IActivateDoc2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::ActivateDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) and [ISldWorks::IActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActivateDoc3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IActivateDoc2( _
   ByVal Name As System.String, _
   ByVal Silent As System.Boolean, _
   ByRef Errors As System.Integer _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim Silent As System.Boolean
Dim Errors As System.Integer
Dim value As ModelDoc

value = instance.IActivateDoc2(Name, Silent, Errors)
```

### C#

```csharp
ModelDoc IActivateDoc2(
   System.string Name,
   System.bool Silent,
   out System.int Errors
)
```

### C++/CLI

```cpp
ModelDoc^ IActivateDoc2(
   System.String^ Name,
   System.bool Silent,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Silent`:
- `Errors`:

## VBA Syntax

See [SldWorks::IActivateDoc2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IActivateDoc2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

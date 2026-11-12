---
title: "IOpenDoc3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IOpenDoc3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IOpenDoc3.html"
---

# IOpenDoc3 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IOpenDoc3( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal ReadOnly As System.Boolean, _
   ByVal ViewOnly As System.Boolean, _
   ByVal RapidDraft As System.Boolean, _
   ByVal Silent As System.Boolean, _
   ByRef Errors As System.Integer _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim ReadOnly As System.Boolean
Dim ViewOnly As System.Boolean
Dim RapidDraft As System.Boolean
Dim Silent As System.Boolean
Dim Errors As System.Integer
Dim value As ModelDoc

value = instance.IOpenDoc3(FileName, Type, ReadOnly, ViewOnly, RapidDraft, Silent, Errors)
```

### C#

```csharp
ModelDoc IOpenDoc3(
   System.string FileName,
   System.int Type,
   System.bool ReadOnly,
   System.bool ViewOnly,
   System.bool RapidDraft,
   System.bool Silent,
   out System.int Errors
)
```

### C++/CLI

```cpp
ModelDoc^ IOpenDoc3(
   System.String^ FileName,
   System.int Type,
   System.bool ReadOnly,
   System.bool ViewOnly,
   System.bool RapidDraft,
   System.bool Silent,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `Type`:
- `ReadOnly`:
- `ViewOnly`:
- `RapidDraft`:
- `Silent`:
- `Errors`:

## VBA Syntax

See [SldWorks::IOpenDoc3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IOpenDoc3.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

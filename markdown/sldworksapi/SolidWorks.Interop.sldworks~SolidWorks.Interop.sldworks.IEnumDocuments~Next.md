---
title: "Next Method (IEnumDocuments)"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments~Next.html"
---

# Next Method (IEnumDocuments)

Obsolete. Superseded by [IEnumDocuments2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2~Next.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelDoc, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments
Dim Celt As System.Integer
Dim Rgelt As ModelDoc
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out ModelDoc Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] ModelDoc^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`:
- `Rgelt`:
- `PceltFetched`:

## VBA Syntax

See [EnumDocuments::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments~Next.html).

## See Also

[IEnumDocuments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments.html)
[IEnumDocuments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments_members.html)

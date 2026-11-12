---
title: "GetAllExternalReferences3 Method (ISwDMDocument12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument12"
member: "GetAllExternalReferences3"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12~GetAllExternalReferences3.html"
---

# GetAllExternalReferences3 Method (ISwDMDocument12)

Obsolete. Superseded by [ISwDMDocument13::GetAllExternalReferences4](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllExternalReferences3( _
   ByVal pSrcOption As SwDMSearchOption, _
   ByRef brokenRefVar As System.Object, _
   ByRef IsVirtual As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument12
Dim pSrcOption As SwDMSearchOption
Dim brokenRefVar As System.Object
Dim IsVirtual As System.Object
Dim value As System.Object

value = instance.GetAllExternalReferences3(pSrcOption, brokenRefVar, IsVirtual)
```

### C#

```csharp
System.object GetAllExternalReferences3(
   SwDMSearchOption pSrcOption,
   out System.object brokenRefVar,
   out System.object IsVirtual
)
```

### C++/CLI

```cpp
System.Object^ GetAllExternalReferences3(
   SwDMSearchOption^ pSrcOption,
   [Out] System.Object^ brokenRefVar,
   [Out] System.Object^ IsVirtual
)
```

### Parameters

- `pSrcOption`:
- `brokenRefVar`:
- `IsVirtual`:

## VBA Syntax

See [SwDMDocument12::GetAllExternalReferences3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument12~GetAllExternalReferences3.html).

## See Also

[ISwDMDocument12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12.html)
[ISwDMDocument12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12_members.html)

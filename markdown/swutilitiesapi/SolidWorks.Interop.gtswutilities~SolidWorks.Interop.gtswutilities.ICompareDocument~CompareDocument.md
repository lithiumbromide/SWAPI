---
title: "CompareDocument Method (ICompareDocument)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareDocument"
member: "CompareDocument"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareDocument~CompareDocument.html"
---

# CompareDocument Method (ICompareDocument)

Obsolete. Superseded by [ICompareDocument::CompareDocument2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareDocument~CompareDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareDocument( _
   ByVal reffile As System.String, _
   ByVal modfile As System.String, _
   ByVal lOperationOptions As System.Integer, _
   ByVal lResultOptions As System.Integer, _
   ByVal reportname As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareDocument
Dim reffile As System.String
Dim modfile As System.String
Dim lOperationOptions As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim value As System.Integer

value = instance.CompareDocument(reffile, modfile, lOperationOptions, lResultOptions, reportname)
```

### C#

```csharp
System.int CompareDocument(
   System.string reffile,
   System.string modfile,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.string reportname
)
```

### C++/CLI

```cpp
System.int CompareDocument(
   System.String^ reffile,
   System.String^ modfile,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.String^ reportname
)
```

### Parameters

- `reffile`:
- `modfile`:
- `lOperationOptions`:
- `lResultOptions`:
- `reportname`:

## VBA Syntax

See [ICompareDocument::CompareDocument](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareDocument~CompareDocument.html).

## See Also

[ICompareDocument Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareDocument.html)
[ICompareDocument Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareDocument_members.html)

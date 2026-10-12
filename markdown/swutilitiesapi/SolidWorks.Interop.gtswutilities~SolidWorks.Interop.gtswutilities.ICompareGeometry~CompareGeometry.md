---
title: "CompareGeometry Method (ICompareGeometry)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareGeometry"
member: "CompareGeometry"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry~CompareGeometry.html"
---

# CompareGeometry Method (ICompareGeometry)

Obsolete. Superseded by [ICompareGeometry::CompareGeometry2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareGeometry~CompareGeometry2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareGeometry( _
   ByVal reffile As System.String, _
   ByVal modfile As System.String, _
   ByVal lOperationOptions As System.Integer, _
   ByVal lResultOptions As System.Integer, _
   ByVal reportname As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareGeometry
Dim reffile As System.String
Dim modfile As System.String
Dim lOperationOptions As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim value As System.Integer

value = instance.CompareGeometry(reffile, modfile, lOperationOptions, lResultOptions, reportname)
```

### C#

```csharp
System.int CompareGeometry(
   System.string reffile,
   System.string modfile,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.string reportname
)
```

### C++/CLI

```cpp
System.int CompareGeometry(
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

See [ICompareGeometry::CompareGeometry](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareGeometry~CompareGeometry.html).

## See Also

[ICompareGeometry Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry.html)
[ICompareGeometry Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry_members.html)

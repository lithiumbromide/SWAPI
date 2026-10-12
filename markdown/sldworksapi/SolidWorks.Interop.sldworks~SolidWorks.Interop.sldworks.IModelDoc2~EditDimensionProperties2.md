---
title: "EditDimensionProperties2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditDimensionProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDimensionProperties2.html"
---

# EditDimensionProperties2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::EditDimensionProperties3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditDimensionProperties3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EditDimensionProperties2( _
   ByVal TolType As System.Integer, _
   ByVal TolMax As System.Double, _
   ByVal TolMin As System.Double, _
   ByVal TolMaxFit As System.String, _
   ByVal TolMinFit As System.String, _
   ByVal UseDocPrec As System.Boolean, _
   ByVal Precision As System.Integer, _
   ByVal ArrowsIn As System.Integer, _
   ByVal UseDocArrows As System.Boolean, _
   ByVal Arrow1 As System.Integer, _
   ByVal Arrow2 As System.Integer, _
   ByVal PrefixText As System.String, _
   ByVal SuffixText As System.String, _
   ByVal ShowValue As System.Boolean, _
   ByVal CalloutText1 As System.String, _
   ByVal CalloutText2 As System.String, _
   ByVal CenterText As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim TolType As System.Integer
Dim TolMax As System.Double
Dim TolMin As System.Double
Dim TolMaxFit As System.String
Dim TolMinFit As System.String
Dim UseDocPrec As System.Boolean
Dim Precision As System.Integer
Dim ArrowsIn As System.Integer
Dim UseDocArrows As System.Boolean
Dim Arrow1 As System.Integer
Dim Arrow2 As System.Integer
Dim PrefixText As System.String
Dim SuffixText As System.String
Dim ShowValue As System.Boolean
Dim CalloutText1 As System.String
Dim CalloutText2 As System.String
Dim CenterText As System.Boolean
Dim value As System.Boolean

value = instance.EditDimensionProperties2(TolType, TolMax, TolMin, TolMaxFit, TolMinFit, UseDocPrec, Precision, ArrowsIn, UseDocArrows, Arrow1, Arrow2, PrefixText, SuffixText, ShowValue, CalloutText1, CalloutText2, CenterText)
```

### C#

```csharp
System.bool EditDimensionProperties2(
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.string TolMaxFit,
   System.string TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2,
   System.string PrefixText,
   System.string SuffixText,
   System.bool ShowValue,
   System.string CalloutText1,
   System.string CalloutText2,
   System.bool CenterText
)
```

### C++/CLI

```cpp
System.bool EditDimensionProperties2(
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.String^ TolMaxFit,
   System.String^ TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2,
   System.String^ PrefixText,
   System.String^ SuffixText,
   System.bool ShowValue,
   System.String^ CalloutText1,
   System.String^ CalloutText2,
   System.bool CenterText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TolType`:
- `TolMax`:
- `TolMin`:
- `TolMaxFit`:
- `TolMinFit`:
- `UseDocPrec`:
- `Precision`:
- `ArrowsIn`:
- `UseDocArrows`:
- `Arrow1`:
- `Arrow2`:
- `PrefixText`:
- `SuffixText`:
- `ShowValue`:
- `CalloutText1`:
- `CalloutText2`:
- `CenterText`:

## VBA Syntax

See [ModelDoc2::EditDimensionProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditDimensionProperties2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

---
title: "EditDatumTargetSymbol Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "EditDatumTargetSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditDatumTargetSymbol.html"
---

# EditDatumTargetSymbol Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::EditDatumTargetSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditDatumTargetSymbol.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EditDatumTargetSymbol( _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String, _
   ByVal AreaStyle As System.Short, _
   ByVal AreaOutside As System.Boolean, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal ValueStr1 As System.String, _
   ByVal ValueStr2 As System.String, _
   ByVal ArrowsSmart As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderLineStyle As System.Short, _
   ByVal LeaderBent As System.Boolean, _
   ByVal ShowArea As System.Boolean, _
   ByVal ShowSymbol As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
Dim AreaStyle As System.Short
Dim AreaOutside As System.Boolean
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim ValueStr1 As System.String
Dim ValueStr2 As System.String
Dim ArrowsSmart As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderLineStyle As System.Short
Dim LeaderBent As System.Boolean
Dim ShowArea As System.Boolean
Dim ShowSymbol As System.Boolean
Dim value As System.Boolean

value = instance.EditDatumTargetSymbol(Datum1, Datum2, Datum3, AreaStyle, AreaOutside, Value1, Value2, ValueStr1, ValueStr2, ArrowsSmart, ArrowStyle, LeaderLineStyle, LeaderBent, ShowArea, ShowSymbol)
```

### C#

```csharp
System.bool EditDatumTargetSymbol(
   System.string Datum1,
   System.string Datum2,
   System.string Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.string ValueStr1,
   System.string ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
)
```

### C++/CLI

```cpp
System.bool EditDatumTargetSymbol(
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.String^ ValueStr1,
   System.String^ ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Datum1`:
- `Datum2`:
- `Datum3`:
- `AreaStyle`:
- `AreaOutside`:
- `Value1`:
- `Value2`:
- `ValueStr1`:
- `ValueStr2`:
- `ArrowsSmart`:
- `ArrowStyle`:
- `LeaderLineStyle`:
- `LeaderBent`:
- `ShowArea`:
- `ShowSymbol`:

## VBA Syntax

See [ModelDoc::EditDatumTargetSymbol](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~EditDatumTargetSymbol.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

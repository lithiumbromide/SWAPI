---
title: "IInsertBOMBalloon2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IInsertBOMBalloon2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertBOMBalloon2.html"
---

# IInsertBOMBalloon2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IInsertBOMBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertBOMBalloon2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertBOMBalloon2( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As Note

value = instance.IInsertBOMBalloon2(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

### C#

```csharp
Note IInsertBOMBalloon2(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

### C++/CLI

```cpp
Note^ IInsertBOMBalloon2(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`:
- `Size`:
- `UpperTextStyle`:
- `UpperText`:
- `LowerTextStyle`:
- `LowerText`:

## VBA Syntax

See [ModelDoc::IInsertBOMBalloon2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IInsertBOMBalloon2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

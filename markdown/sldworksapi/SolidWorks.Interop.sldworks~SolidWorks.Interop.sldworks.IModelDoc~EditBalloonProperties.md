---
title: "EditBalloonProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "EditBalloonProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditBalloonProperties.html"
---

# EditBalloonProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::EditBalloonProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditBalloonProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EditBalloonProperties( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As System.Object
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
Dim value As System.Object

value = instance.EditBalloonProperties(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

### C#

```csharp
System.object EditBalloonProperties(
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
System.Object^ EditBalloonProperties(
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

See [ModelDoc::EditBalloonProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~EditBalloonProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

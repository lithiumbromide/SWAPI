---
title: "EditBalloonProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditBalloonProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditBalloonProperties.html"
---

# EditBalloonProperties Method (IModelDoc2)

Obsolete. Superseded by [INote::SetBalloon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~SetBalloon.html) and [INote::SetBomBalloonText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~SetBomBalloonText.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::EditBalloonProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditBalloonProperties.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

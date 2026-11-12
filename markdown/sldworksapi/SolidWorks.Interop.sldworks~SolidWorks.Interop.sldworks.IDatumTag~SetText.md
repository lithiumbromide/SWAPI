---
title: "SetText Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "SetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetText.html"
---

# SetText Method (IDatumTag)

Sets the text of this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetText( _
   ByVal WhichText As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim WhichText As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.SetText(WhichText, Text)
```

### C#

```csharp
System.bool SetText(
   System.int WhichText,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool SetText(
   System.int WhichText,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Text to set as defined in [swDatumTagTextParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTagTextParts_e.html)
- `Text`: New content for the specified WhichText

### Return Value

True if successful, false if not

## VBA Syntax

See [DatumTag::SetText](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~SetText.html).

## Examples

[Set Text in Datum Tags and GTols (VBA)](Set_Text_in_Datum_Tags_and_GTols_Example_VB.htm)
[Set Text in Datum Tags and GTols (VB.NET)](Set_Text_in_Datum_Tags_and_GTols_Example_VBNET.htm)
[Set Text in Datum Tags and GTols (C#)](Set_Text_in_Datum_Tags_and_GTols_Example_CSharp.htm)

## Remarks

After calling this method, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) to see the new text.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)

## Availability

SOLIDWORKS 2011 SP03, Revision Number 19.3

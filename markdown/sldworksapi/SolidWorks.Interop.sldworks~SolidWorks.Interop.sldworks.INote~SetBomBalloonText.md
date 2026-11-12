---
title: "SetBomBalloonText Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetBomBalloonText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html"
---

# SetBomBalloonText Method (INote)

Sets the text for this BOM balloon note.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBomBalloonText( _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As System.Boolean

value = instance.SetBomBalloonText(UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

### C#

```csharp
System.bool SetBomBalloonText(
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

### C++/CLI

```cpp
System.bool SetBomBalloonText(
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperTextStyle`: Style for the upper text as defined in [swDetailingNoteTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetailingNoteTextContent_e.html)
- `UpperText`: Upper text
- `LowerTextStyle`: Style for the lower text as defined in [swDetailingNoteTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetailingNoteTextContent_e.html)
- `LowerText`: Lower text

### Return Value

True if successfully returned, false if not

## VBA Syntax

See [Note::SetBomBalloonText](ms-its:sldworksapivb6.chm::/sldworks~Note~SetBomBalloonText.html).

## Examples

[Set BOM Balloon Text (VBA)](Set_BOM_Balloon_Example_VB.htm)
[Get Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)
[Get Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## Remarks

If the upper- or lower-text style is swBalloonTextQuantity or swBalloonTextItemNumber, then SOLIDWORKS ignores the specified upper or lower text.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.html)
[INote::GetBalloonSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html)
[INote::GetBalloonStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html)
[INote::GetBalloonStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.html)
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html)
[INote::GetBomBalloonTextStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.html)
[INote::HasBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.html)
[INote::IsBomBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[INote::IsStackedBalloonMaster Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[IModelDocExtension::InsertBOMBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

---
title: "InsertNoteWithParameters Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertNoteWithParameters"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNoteWithParameters.html"
---

# InsertNoteWithParameters Method (ISketchManager)

Inserts and formats the Note as specified.

## Syntax

### Visual Basic

```vb
Function InsertNoteWithParameters( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal StrArray As System.Object, _
   ByVal Angle As System.Double, _
   ByVal Height As System.Double, _
   ByVal Justify As dsNoteJustification_e, _
   ByVal LineSpacingStyle As dsNoteLineSpacingStyle_e, _
   ByVal LineSpaceDistance As System.Double, _
   ByVal TextStyle As System.String, _
   ByVal Width As System.Double _
) As Note
```

### C#

```csharp
Note InsertNoteWithParameters(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.object StrArray,
   System.double Angle,
   System.double Height,
   dsNoteJustification_e Justify,
   dsNoteLineSpacingStyle_e LineSpacingStyle,
   System.double LineSpaceDistance,
   System.string TextStyle,
   System.double Width
)
```

### JScript

```
function InsertNoteWithParameters(
   X1 : System.double,
   Y1 : System.double,
   Z1 : System.double,
   X2 : System.double,
   Y2 : System.double,
   Z2 : System.double,
   StrArray : System.Object,
   Angle : System.double,
   Height : System.double,
   Justify : dsNoteJustification_e,
   LineSpacingStyle : dsNoteLineSpacingStyle_e,
   LineSpaceDistance : System.double,
   TextStyle : System.String,
   Width : System.double
) : Note;
```

### Managed Extensions for C++

```
Note* InsertNoteWithParameters(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.Object* StrArray,
   System.double Angle,
   System.double Height,
   dsNoteJustification_e Justify,
   dsNoteLineSpacingStyle_e LineSpacingStyle,
   System.double LineSpaceDistance,
   System.string* TextStyle,
   System.double Width
)
```

### C++/CLI

```cpp
Note^ InsertNoteWithParameters(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.Object^ StrArray,
   System.double Angle,
   System.double Height,
   dsNoteJustification_e Justify,
   dsNoteLineSpacingStyle_e LineSpacingStyle,
   System.double LineSpaceDistance,
   System.String^ TextStyle,
   System.double Width
)
```

### Parameters

- `X1`: x coordinate of the upper-left corner of the Note
- `Y1`: y coordinate of the upper-left corner of the Note
- `Z1`: z coordinate of the upper-left corner of the Note
- `X2`: x coordinate of the lower-right corner of the Note
- `Y2`: y coordinate of the lower-right corner of the Note
- `Z2`: z coordinate of the lower-right corner of the Note
- `StrArray`: Array of strings constituting the text of the Note
- `Angle`: Angle of rotation of the Note
- `Height`: Height of text in the Note
- `Justify`: Justification as defined in [dsNoteJustification_e](Interop.dsAutomation~Interop.dsAutomation.dsNoteJustification_e.html)
- `LineSpacingStyle`: Line spacing style as defined in [dsNoteLineSpacingStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsNoteLineSpacingStyle_e.html)
- `LineSpaceDistance`: Distance between each line in the Note
- `TextStyle`: [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Name.html) in the Note
- `Width`: Width of the Note

### Return Value

[Note](Interop.dsAutomation~Interop.dsAutomation.INote.html)

## Examples

[Insert Notes with Parameters (C#)](Insert_Notes_with_Parameters_Example_CSharp.htm)
[Insert Notes with Parameters (VB.NET)](Insert_Notes_with_Parameters_Example_VBNET.htm)
[Insert Notes with Parameters (VBA)](Insert_Notes_with_Parameters_Example_VBA.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)

## Remarks

DraftSight automatically calculates the height of the note's bounding box and modifies it based on the Justify parameter.

| This bounding box boundary... | Is calculated when Justify is... |  |
| --- | --- | --- |
| Top | dsNoteJustification_BottomLeft, dsNoteJustification_BottomCenter, or dsNoteJustification_BottomRight |  |
| Bottom | dsNoteJustification_TopLeft, dsNoteJustification_TopCenter, or dsNoteJustification_TopRight |  |
| Top and bottom | dsNoteJustification_MiddleLeft, dsNoteJustification_MiddleCenter, or dsNoteJustification_MiddleRight |  |

The Width parameter setting determines word wrapping. The Height parameter is the default height of the note's text.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[INote:InsertNote Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertNote.html)

## Availability

DraftSight V1R1.1

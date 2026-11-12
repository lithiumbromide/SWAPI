---
title: "InsertCurvedText Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertCurvedText"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCurvedText.html"
---

# InsertCurvedText Method (ISketchManager)

Inserts the specified text along the curve of the specified Arc.

## Syntax

### Visual Basic

```vb
Function InsertCurvedText( _
   ByVal Contents As System.String, _
   ByVal CircleArc As CircleArc _
) As ArcAlignedText
```

### C#

```csharp
ArcAlignedText InsertCurvedText(
   System.string Contents,
   CircleArc CircleArc
)
```

### JScript

```
function InsertCurvedText(
   Contents : System.String,
   CircleArc : CircleArc
) : ArcAlignedText;
```

### Managed Extensions for C++

```
ArcAlignedText* InsertCurvedText(
   System.string* Contents,
   CircleArc* CircleArc
)
```

### C++/CLI

```cpp
ArcAlignedText^ InsertCurvedText(
   System.String^ Contents,
   CircleArc^ CircleArc
)
```

### Parameters

- `Contents`: Text string
- `CircleArc`: [ICircleArc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

### Return Value

[IArcAlignedText](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)

## Examples

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Open c:\ProgramData\Dassault Systemes\DraftSight\Examples\pump housing.dwg.
' 6. Run the macro.
'
' Postconditions: Creates an Arc with "Curved Text" in the
' lower-left area of the drawing.
'----------------------------------------------------------------
Option Explicit
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim circlearc1 As DraftSight.CircleArc
    Dim arcAlignedText As DraftSight.arcAlignedText
    Dim curvedTextSettings As DraftSight.CurvedSettings
    Dim typeface As String
    Dim Bold As Boolean
    Dim Italic As Boolean
    Dim Charset As Long
    Dim pitchAndFamily As Long
    Dim dsSheet As DraftSight.Sheet
    Dim dsVarSheets As Variant
```

```
    Set dsApp = GetObject(, "DraftSight.Application")

    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        Set dsModel = dsDoc.GetModel()
        Set dsSketchManager = dsModel.GetSketchManager()
        Set circlearc1 = dsSketchManager.InsertArc(7.36982486789842, 1.85302055152848, 0#, 5.20869124502084, 1.54022710953838, 2.99868519349434)
        Set arcAlignedText = dsSketchManager.InsertCurvedText("Curved Text", circlearc1)
        Set curvedTextSettings = arcAlignedText.GetCurvedTextSettings
        curvedTextSettings.GetFontParameters typeface, Bold, Italic, Charset, pitchAndFamily
```

```
    Else
```

```
        MsgBox "No drawing open in DraftSight"
```

```
    End If
End Sub
```

## Remarks

After you create the curved text using this method, use [ICurvedSettings](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings.html) to set its properties.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)

## Availability

DraftSight 2018 SP2

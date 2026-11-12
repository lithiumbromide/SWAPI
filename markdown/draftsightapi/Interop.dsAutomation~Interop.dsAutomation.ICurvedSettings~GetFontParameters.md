---
title: "GetFontParameters Method (ICurvedSettings)"
project: ""
interface: "ICurvedSettings"
member: "GetFontParameters"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings~GetFontParameters.html"
---

# GetFontParameters Method (ICurvedSettings)

Gets the parameters of a Windows font for this curved text.

## Syntax

### Visual Basic

```vb
Sub GetFontParameters( _
   ByRef Typeface As System.String, _
   ByRef Bold As System.Boolean, _
   ByRef Italic As System.Boolean, _
   ByRef Charset As System.Integer, _
   ByRef PitchAndFamily As System.Integer _
)
```

### C#

```csharp
void GetFontParameters(
   out System.string Typeface,
   out System.bool Bold,
   out System.bool Italic,
   out System.int Charset,
   out System.int PitchAndFamily
)
```

### JScript

```
function GetFontParameters(
   Typeface : System.String,
   Bold : System.boolean,
   Italic : System.boolean,
   Charset : System.int,
   PitchAndFamily : System.int
);
```

### Managed Extensions for C++

```
void GetFontParameters(
   [PARAMFLAG::Out] System.string* Typeface,
   [PARAMFLAG::Out] System.bool Bold,
   [PARAMFLAG::Out] System.bool Italic,
   [PARAMFLAG::Out] System.int Charset,
   [PARAMFLAG::Out] System.int PitchAndFamily
)
```

### C++/CLI

```cpp
void GetFontParameters(
   [Out] System.String^ Typeface,
   [Out] System.bool Bold,
   [Out] System.bool Italic,
   [Out] System.int Charset,
   [Out] System.int PitchAndFamily
)
```

### Parameters

- `Typeface`: File name of the Windows font
- `Bold`: True if the Windows font is bold, false if not
- `Italic`: True if the Windows font is italic, false if not
- `Charset`: Windows character set identifier
- `PitchAndFamily`: Windows pitch and character family identifier

## Examples

See the [ISketchManager::InsertCurvedText](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCurvedText.html) example.

## See Also

[ICurvedSettings Interface](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings.html)
[ICurvedSettings Members](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings_members.html)
[ICurvedSettings::SetFontParameters Method ()](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings~SetFontParameters.html)

## Availability

DraftSight 2018 SP2

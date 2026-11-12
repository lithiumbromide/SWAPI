---
title: "SetFontParameters Method (ICurvedSettings)"
project: ""
interface: "ICurvedSettings"
member: "SetFontParameters"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings~SetFontParameters.html"
---

# SetFontParameters Method (ICurvedSettings)

Sets the parameters of a Windows font for this curved text.

## Syntax

### Visual Basic

```vb
Sub SetFontParameters( _
   ByVal Typeface As System.String, _
   ByVal Bold As System.Boolean, _
   ByVal Italic As System.Boolean, _
   ByVal Charset As System.Integer, _
   ByVal PitchAndFamily As System.Integer _
)
```

### C#

```csharp
void SetFontParameters(
   System.string Typeface,
   System.bool Bold,
   System.bool Italic,
   System.int Charset,
   System.int PitchAndFamily
)
```

### JScript

```
function SetFontParameters(
   Typeface : System.String,
   Bold : System.boolean,
   Italic : System.boolean,
   Charset : System.int,
   PitchAndFamily : System.int
);
```

### Managed Extensions for C++

```
void SetFontParameters(
   System.string* Typeface,
   System.bool Bold,
   System.bool Italic,
   System.int Charset,
   System.int PitchAndFamily
)
```

### C++/CLI

```cpp
void SetFontParameters(
   System.String^ Typeface,
   System.bool Bold,
   System.bool Italic,
   System.int Charset,
   System.int PitchAndFamily
)
```

### Parameters

- `Typeface`: File name of the Windows font
- `Bold`: True if the Windows font is bold, false if not
- `Italic`: True if the Windows font is italic, false if not
- `Charset`: Windows character set identifier
- `PitchAndFamily`: Windows pitch and character family identifier

## See Also

[ICurvedSettings Interface](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings.html)
[ICurvedSettings Members](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings_members.html)
[ICurvedSettings::GetFontParameters Method ()](Interop.dsAutomation~Interop.dsAutomation.ICurvedSettings~GetFontParameters.html)

## Availability

DraftSight 2018 SP2

---
title: "SetFontParameters Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "SetFontParameters"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~SetFontParameters.html"
---

# SetFontParameters Method (ITextStyle)

Sets the parameters of a Windows font for the TextStyle.

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
- `Bold`: True to bold the Windows font, false to not
- `Italic`: True to italicize the Windows font, false to not
- `Charset`: Windows character set identifier
- `PitchAndFamily`: Windows pitch and character family identifier

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::GetFontParameters Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetFontParameters.html)

## Availability

DraftSight V1R1.1

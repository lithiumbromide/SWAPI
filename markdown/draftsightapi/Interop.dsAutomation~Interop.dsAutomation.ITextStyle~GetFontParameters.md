---
title: "GetFontParameters Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "GetFontParameters"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetFontParameters.html"
---

# GetFontParameters Method (ITextStyle)

Gets the parameters of a Windows font for the TextStyle.

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

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::SetFontParameters Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~SetFontParameters.html)

## Availability

DraftSight V1R1.1

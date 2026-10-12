---
title: "swCheckSpellingOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCheckSpellingOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckSpellingOptions_e.html"
---

# swCheckSpellingOptions_e Enumeration

Spell check options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCheckSpellingOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCheckSpellingOptions_e
```

### C#

```csharp
public enum swCheckSpellingOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCheckSpellingOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSpellingIgnoreCapitalizedWords | 8 or 0x8; Capitalized words are not checked |
| swSpellingIgnoreInternetAndFiles | 16 or 0x10; Words containing a web address are not checked |
| swSpellingIgnoreMixedCase | 2 or 0x2; Words that are mixed-case (upper case and lowercase, e.g., eDrawings) are not checked |
| swSpellingIgnoreUpperCase | 1 or 0x1; Words that are all uppercase are not checked |
| swSpellingIgnoreWordsWithNumbers | 4 or 0x4; Words containing both letters and numbers are not checked |
| swSpellingLeaveEngineRunning | 32 or 0x20; Do not stop Microsoft Word, which is the spell-check engine, after checking the first and any subsequent annotations if you have a significant number of annotations to spell check; however, on the last use of IAnnotation::CheckSpelling , you must disable this flag so that Microsoft Word is shut down after that call |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)

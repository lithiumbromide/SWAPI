---
title: "swUserPreferenceStringListValue_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swUserPreferenceStringListValue_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringListValue_e.html"
---

# swUserPreferenceStringListValue_e Enumeration

User-preference enumerators for system options and document properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swUserPreferenceStringListValue_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swUserPreferenceStringListValue_e
```

### C#

```csharp
public enum swUserPreferenceStringListValue_e : System.Enum
```

### C++/CLI

```cpp
public enum class swUserPreferenceStringListValue_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDxfMappingFiles | 0 = This setting is persistent across SOLIDWORKS sessions; you can also interactively get or set the custom map file setting by clicking File, Save As, .dxf or .dwg as Save as type , and Options ; separate each string in the list by a line feed (e.g., the vbLf constant in Visual Basic). |
| swEmodelAttachmentList | 2 = Sets which configurations for which to generate and attach STEP files |
| swEmodelSelectionList | 1 = Sets which configurations or sheets to save when publishing an eDrawings |

## Remarks

Use this enumeration with [ISldWorks::GetUserPreferenceStringListValue](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.html) and [ISldWorks::SetUserPreferenceStringListValue](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
[swUserPreferenceDoubleValue_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceDoubleValue_e.html)
[swUserPreferenceIntegerValue_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html)
[swUserPreferenceStringValue_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.html)
[swUserPreferenceTextFormat_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceTextFormat_e.html)
[swUserPreferenceToggle_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html)

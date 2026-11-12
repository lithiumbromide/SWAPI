---
title: "swPresentationOpts_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPresentationOpts_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPresentationOpts_e.html"
---

# swPresentationOpts_e Enumeration

SOLIDWORKS Presentation options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPresentationOpts_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPresentationOpts_e
```

### C#

```csharp
public enum swPresentationOpts_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPresentationOpts_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPresentationOpts_ActiveView | 32 or 0x20 |
| swPresentationOpts_Animations | 4 or 0x4 |
| swPresentationOpts_BackView | 2048 or 0x800 |
| swPresentationOpts_BottomView | 128 or 0x80 |
| swPresentationOpts_CameraMovement | 16 or 0x10 |
| swPresentationOpts_ChkOpenPassword3DPDF | 1073741824 or 0x40000000; |
| swPresentationOpts_CompressTesselation | 8388608 or 0x800000 |
| swPresentationOpts_CreateAttachSTEP242 | 262144 or 0x40000 |
| swPresentationOpts_DimetricView | 32768 or 0x8000 |
| swPresentationOpts_DisableCopying3DPDF | 67108864 or 0x4000000 |
| swPresentationOpts_DisableEditing3DPDF | 33554432 or 0x2000000 |
| swPresentationOpts_DisablePrinting3DPDF | 16777216 or 0x1000000 |
| swPresentationOpts_ExcludeFromAnnoView | 131072 or 0x20000 |
| swPresentationOpts_Explodes | 8 or 0x8 |
| swPresentationOpts_FrontView | 1024 or 0x400 |
| swPresentationOpts_HighAccuracy | 1048576 or 0x100000 |
| swPresentationOpts_IsometricView | 8192 or 0x2000 |
| swPresentationOpts_LeftView | 256 or 0x100 |
| swPresentationOpts_LowAccuracy | 524288 or 0x80000 |
| swPresentationOpts_MaxAccuracy | 4194304 or 0x400000 |
| swPresentationOpts_MedAccuracy | 2097152 or 0x200000 |
| swPresentationOpts_None | 0 or 0x0 |
| swPresentationOpts_NormalView | 4096 or 0x1000 |
| swPresentationOpts_OpenPDF | 65536 or 0x10000 |
| swPresentationOpts_PDFPreview | 268435456 or 0x10000000 |
| swPresentationOpts_Pres | 1 or 0x1 |
| swPresentationOpts_RightView | 512 or 0x200 |
| swPresentationOpts_ShowOnlyGraphicalData | 134217728 or 0x8000000 |
| swPresentationOpts_SingleHTML | 536870912 or 0x20000000; Option to export HTML from 3DPDF |
| swPresentationOpts_TopView | 64 or 0x40 |
| swPresentationOpts_TrimetricView | 16384 or 0x4000 |
| swPresentationOpts_U3D | 2 or 0x2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)

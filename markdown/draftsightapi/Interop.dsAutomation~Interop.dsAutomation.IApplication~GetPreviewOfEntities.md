---
title: "GetPreviewOfEntities Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetPreviewOfEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewOfEntities.html"
---

# GetPreviewOfEntities Method (IApplication)

Creates a preview bitmap of the specified entities and returns a byte array of the bitmap.

## Syntax

### Visual Basic

```vb
Function GetPreviewOfEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal Format As dsBitmapFormat_e, _
   ByVal PreviewRange As dsPreviewRange_e, _
   ByVal NamedView As System.String, _
   ByVal WinMin As MathPoint, _
   ByVal WinMax As MathPoint, _
   ByVal Width As System.Integer, _
   ByVal Height As System.Integer, _
   ByRef BitmapByteArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetPreviewOfEntities(
   System.object EntitiesArray,
   dsBitmapFormat_e Format,
   dsPreviewRange_e PreviewRange,
   System.string NamedView,
   MathPoint WinMin,
   MathPoint WinMax,
   System.int Width,
   System.int Height,
   out System.object BitmapByteArray
)
```

### JScript

```
function GetPreviewOfEntities(
   EntitiesArray : System.Object,
   Format : dsBitmapFormat_e,
   PreviewRange : dsPreviewRange_e,
   NamedView : System.String,
   WinMin : MathPoint,
   WinMax : MathPoint,
   Width : System.int,
   Height : System.int,
   BitmapByteArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetPreviewOfEntities(
   System.Object* EntitiesArray,
   dsBitmapFormat_e Format,
   dsPreviewRange_e PreviewRange,
   System.string* NamedView,
   MathPoint* WinMin,
   MathPoint* WinMax,
   System.int Width,
   System.int Height,
   [PARAMFLAG::Out] System.Object* BitmapByteArray
)
```

### C++/CLI

```cpp
System.bool GetPreviewOfEntities(
   System.Object^ EntitiesArray,
   dsBitmapFormat_e Format,
   dsPreviewRange_e PreviewRange,
   System.String^ NamedView,
   MathPoint^ WinMin,
   MathPoint^ WinMax,
   System.int Width,
   System.int Height,
   [Out] System.Object^ BitmapByteArray
)
```

### Parameters

- `EntitiesArray`: Array of entities for the preview bitmap
- `Format`: Format of the preview bitmap as defined in [dsBitmapFormat_e](Interop.dsAutomation~Interop.dsAutomation.dsBitmapFormat_e.html)
- `PreviewRange`: Preview bitmap range as defined in [dsPreviewRange_e](Interop.dsAutomation~Interop.dsAutomation.dsPreviewRange_e.html)
- `NamedView`: Name of the view if PreviewRange is set to dsPreviewRange_NamedView
- `WinMin`: [Corner](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the window area if PreviewRange is set to dsPreviewRange_SpecifyWindow; otherwise, a null value
- `WinMax`: [Opposite corner](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the window area if PreviewRange is set to dsPreviewRange_SpecifyWindow; otherwise, a null value
- `Width`: Width of the preview bitmap
- `Height`: Height of the preview bitmap
- `BitmapByteArray`: Byte array of the preview bitmap

### Return Value

True if the preview bitmap is created, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetPreviewBitmap Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmap.html)
[IApplication::GetPreviewBitmapBytes Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapBytes.html)
[IApplication::GetPreviewBitmapFile Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapFile.html)

## Availability

DraftSight V1R4.0

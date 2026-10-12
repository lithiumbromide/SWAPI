---
title: "GetDisplayStyle Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetDisplayStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle.html"
---

# GetDisplayStyle Method (IDatumTag)

Gets the display style of this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Integer

value = instance.GetDisplayStyle()
```

### C#

```csharp
System.int GetDisplayStyle()
```

### C++/CLI

```cpp
System.int GetDisplayStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Display style as defined in [swDatumDisplayType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumDisplayType_e.html) (see **Remarks**)

## VBA Syntax

See [DatumTag::GetDisplayStyle](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetDisplayStyle.html).

## Remarks

This method does not return swDatumDisplayType_Default if the datum tag is set to use the document default setting. Instead, either swDatumDisplayType_Roundgb or swDatumDisplayType_Square is returned.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetUseDocDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle.html)
[IDatumTag::SetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4

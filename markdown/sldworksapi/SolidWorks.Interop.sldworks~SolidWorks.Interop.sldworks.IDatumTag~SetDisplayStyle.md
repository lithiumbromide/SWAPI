---
title: "SetDisplayStyle Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "SetDisplayStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle.html"
---

# SetDisplayStyle Method (IDatumTag)

Sets the display style of this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplayStyle( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean

value = instance.SetDisplayStyle(UseDoc, Style)
```

### C#

```csharp
System.bool SetDisplayStyle(
   System.bool UseDoc,
   System.int Style
)
```

### C++/CLI

```cpp
System.bool SetDisplayStyle(
   System.bool UseDoc,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to use the document setting for the datum tag's display style, false to not
- `Style`: Display style as defined in [swDatumDisplayType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumDisplayType_e.html)

### Return Value

True if the specified display style is set, false if not

## VBA Syntax

See [DatumTag::SetDisplayStyle](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~SetDisplayStyle.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle.html)
[IDatumTag::GetUseDocDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4

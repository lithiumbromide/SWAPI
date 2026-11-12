---
title: "GetUseDocDisplayStyle Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetUseDocDisplayStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle.html"
---

# GetUseDocDisplayStyle Method (IDatumTag)

Gets whether this datum tag uses the document setting for its display style.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocDisplayStyle() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Boolean

value = instance.GetUseDocDisplayStyle()
```

### C#

```csharp
System.bool GetUseDocDisplayStyle()
```

### C++/CLI

```cpp
System.bool GetUseDocDisplayStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to use the document setting for the datum feature symbol's display style, false to use local display style

## VBA Syntax

See [DatumTag::GetUseDocDisplayStyle](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetUseDocDisplayStyle.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle.html)
[IDatumTag::SetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4

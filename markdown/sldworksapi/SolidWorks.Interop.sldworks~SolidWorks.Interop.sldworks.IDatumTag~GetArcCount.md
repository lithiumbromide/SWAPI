---
title: "GetArcCount Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetArcCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcCount.html"
---

# GetArcCount Method (IDatumTag)

Gets the number of arc items in this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Integer

value = instance.GetArcCount()
```

### C#

```csharp
System.int GetArcCount()
```

### C++/CLI

```cpp
System.int GetArcCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arcs

## VBA Syntax

See [DatumTag::GetArcCount](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetArcCount.html).

## Remarks

Call this method before calling [IDatumTag::GetArcAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetArcAtIndex.html) or [IDatumTag::IGetArcAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~IGetArcAtIndex.html).

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcAtIndex.html)
[IDatumTag::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetArcAtIndex.html)

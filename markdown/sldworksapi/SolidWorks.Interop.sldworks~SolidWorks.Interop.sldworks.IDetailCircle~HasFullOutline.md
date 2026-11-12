---
title: "HasFullOutline Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "HasFullOutline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline.html"
---

# HasFullOutline Method (IDetailCircle)

Gets whether this detail circle has a full outline in the detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasFullOutline() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Boolean

value = instance.HasFullOutline()
```

### C#

```csharp
System.bool HasFullOutline()
```

### C++/CLI

```cpp
System.bool HasFullOutline();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the detail circle has a full outline in the detail view, false if not

## VBA Syntax

See [DetailCircle::HasFullOutline](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~HasFullOutline.html).

## Remarks

This method is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.html) is false.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetFullOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

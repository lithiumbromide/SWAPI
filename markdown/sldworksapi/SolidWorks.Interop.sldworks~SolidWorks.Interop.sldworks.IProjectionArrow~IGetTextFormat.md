---
title: "IGetTextFormat Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "IGetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetTextFormat.html"
---

# IGetTextFormat Method (IProjectionArrow)

Gets the format of the text for this projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextFormat() As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As TextFormat

value = instance.IGetTextFormat()
```

### C#

```csharp
TextFormat IGetTextFormat()
```

### C++/CLI

```cpp
TextFormat^ IGetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [ProjectionArrow::IGetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~IGetTextFormat.html).

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetTextFormat.html)
[IProjectionArrow::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetUseDocTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

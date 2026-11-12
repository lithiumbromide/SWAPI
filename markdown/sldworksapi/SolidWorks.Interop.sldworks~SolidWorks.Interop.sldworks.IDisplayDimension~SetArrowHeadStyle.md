---
title: "SetArrowHeadStyle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetArrowHeadStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle.html"
---

# SetArrowHeadStyle Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::SetArrowHeadStyle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetArrowHeadStyle( _
   ByVal UseDoc As System.Boolean, _
   ByVal ArrowHeadStyle As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim ArrowHeadStyle As System.Integer

instance.SetArrowHeadStyle(UseDoc, ArrowHeadStyle)
```

### C#

```csharp
void SetArrowHeadStyle(
   System.bool UseDoc,
   System.int ArrowHeadStyle
)
```

### C++/CLI

```cpp
void SetArrowHeadStyle(
   System.bool UseDoc,
   System.int ArrowHeadStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`:
- `ArrowHeadStyle`:

## VBA Syntax

See [DisplayDimension::SetArrowHeadStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetArrowHeadStyle.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

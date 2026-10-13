---
title: "SetLinkedText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetLinkedText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.html"
---

# SetLinkedText Method (IDisplayDimension)

Sets the text to link to this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLinkedText( _
   ByVal BstrLinkedText As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim BstrLinkedText As System.String
Dim value As System.Integer

value = instance.SetLinkedText(BstrLinkedText)
```

### C#

```csharp
System.int SetLinkedText(
   System.string BstrLinkedText
)
```

### C++/CLI

```cpp
System.int SetLinkedText(
   System.String^ BstrLinkedText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BstrLinkedText`: Text to link to this display dimension

### Return Value

Error code as defined in [swLinkDimensionError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLinkDimensionError_e.html)

## VBA Syntax

See [DisplayDimension::SetLinkedText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetLinkedText.html).

## Remarks

- Dimension types must be the same, for example: linear to linea , angular to angular, and so on.
- Angular dimensions must be in the same quadrant.
- Dimensions cannot shared by another named group.
- Dimensions with dissimilar ranges cannot be shared.
- Dimensions cannot driven by equations, read-only, driven sketch dimensions, or reference dimensions.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.html)
[IDisplayDimension::Unlink Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.html)
[IDisplayDimension::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.html)

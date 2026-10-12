---
title: "ShowBubbleTooltip Method (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "ShowBubbleTooltip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~ShowBubbleTooltip.html"
---

# ShowBubbleTooltip Method (IPropertyManagerPageControl)

Displays a bubble ToolTip containing the specified title, message, and bitmap.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltip( _
   ByVal Title As System.String, _
   ByVal Message As System.String, _
   ByVal BmpFile As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim Title As System.String
Dim Message As System.String
Dim BmpFile As System.String

instance.ShowBubbleTooltip(Title, Message, BmpFile)
```

### C#

```csharp
void ShowBubbleTooltip(
   System.string Title,
   System.string Message,
   System.string BmpFile
)
```

### C++/CLI

```cpp
void ShowBubbleTooltip(
   System.String^ Title,
   System.String^ Message,
   System.String^ BmpFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Title`: Title to display in bubble ToolTip
- `Message`: Message to display in bubble ToolTip
- `BmpFile`: Path and filename of bitmap to display in bubble ToolTip

## VBA Syntax

See [PropertyManagerPageControl::ShowBubbleTooltip](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~ShowBubbleTooltip.html).

## Examples

See the [IPropertyManagerPageControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html) examples.

## Remarks

A bubble ToolTip is useful for validating data typed or selected by users in controls on a PropertyManager page.

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

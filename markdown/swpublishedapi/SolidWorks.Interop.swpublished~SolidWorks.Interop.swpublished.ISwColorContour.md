---
title: "ISwColorContour Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour.html"
---

# ISwColorContour Interface

Obsolete. Superseded by [ISwColorContour1](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwColorContour
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour
```

### C#

```csharp
public interface ISwColorContour
```

### C++/CLI

```cpp
public interface class ISwColorContour
```

## VBA Syntax

See [SwColorContour](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour.html).

## Remarks

This SwColorContour object and its methods let your implemented interface:

- Render the model using colors that are application-defined at specific locations for criteria like temperature, thickness, stress, and so on.
- Display values associated with the colors at the cursor location.

To use SwColorContour:

1. Implement the SOLIDWORKS SwColorContour interface.
2. Install your implemented interface in the SOLIDWORKS software using [IModelDocExtension::InstallModelColorizer](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InstallModelColorizer.html).
3. Remove your implemented interface from the SOLIDWORKS software using [IModelDocExtension::RemoveModelColorizer](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~RemoveModelColorizer.html) when you want to stop your implemented interface.

NOTE: Only one color and display interface can be active at any one time. The last color and display interface installed is the active one. If you remove that color and display interface, then the color and display interface installed before it becomes the active color and display interface.

See SOLIDWORKS Help for details about SOLIDWORKS Curvature Display.

To use this interface in a SOLIDWORKS VB.NET or C# macro or add-in, see [ComVisibleAttribute in VB.NET and C# Macros and Add-ins](sldworksapiprogguide.chm::/OVERVIEW/ComVisibleAttribute_in_VSTA_macros.htm).

## See Also

[ISwColorContour Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)

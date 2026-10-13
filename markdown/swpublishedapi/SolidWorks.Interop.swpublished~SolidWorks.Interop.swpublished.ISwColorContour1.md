---
title: "ISwColorContour1 Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour1"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1.html"
---

# ISwColorContour1 Interface

Allows access to the color and display values of curvature in a SOLIDWORKS model.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwColorContour1
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour1
```

### C#

```csharp
public interface ISwColorContour1
```

### C++/CLI

```cpp
public interface class ISwColorContour1
```

## VBA Syntax

See [SwColorContour1](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour1.html).

## Examples

[Custom Colorize a Model Example (C#)](Custom_Colorize_a_Model_Example_CSharp.htm)
[Custom Colorize a Model Example (VB.NET)](Custom_Colorize_a_Model_Example_VBNET.htm)

## Remarks

When implemented, the methods of this interface allow you to assign colors and display values of curvature in a SOLIDWORKS model.

To use ISwColorContour1:

1. Implement the ISwColorContour1 interface in an add-in class.
2. Install the implemented interface in the SOLIDWORKS software using [IModelDocExtension::InstallModelColorizer](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InstallModelColorizer.html).
3. Run the add-in and open a model document in SOLIDWORKS.
4. In SOLIDWORKS select **View > Display > Curvature.** The model is colorized by the implemented interface.
5. When you finalize the application, remove the implemented interface from the SOLIDWORKS software using [IModelDocExtension::RemoveModelColorizer](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~RemoveModelColorizer.html).

NOTE: Only one color and display interface can be active at any one time. The last color and display interface installed is the active one. If you remove that color and display interface, then the color and display interface installed before it becomes the active color and display interface.

This interface overrides the color and display functionality of the SOLIDWORKS Curvature tool. See SOLIDWORKS Help for details about the SOLIDWORKS Curvature tool.

To use this interface in a SOLIDWORKS VB.NET or C# macro or add-in, see [ComVisibleAttribute in VB.NET and C# Macros and Add-ins](sldworksapiprogguide.chm::/OVERVIEW/ComVisibleAttribute_in_VSTA_macros.htm).

## See Also

[ISwColorContour1 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)

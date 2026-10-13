---
title: "IGetVisualProperties Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "IGetVisualProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetVisualProperties.html"
---

# IGetVisualProperties Method (IAnnotation)

Gets the visual properties of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisualProperties() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.IGetVisualProperties()
```

### C#

```csharp
System.int IGetVisualProperties()
```

### C++/CLI

```cpp
System.int IGetVisualProperties();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 5 longs (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of longs:

[`color, style, width, layerID, layerOverride` ]

where:

| color | COLORREF returned as an integer. Return value can be 0 or -1 for default color. |
| --- | --- |
| style | Line style as defined in swLineStyles_e . |
| width | Line width as defined in swLineWeights_e . |
| layerID | Integer value indicating which layer holds this entity. The Layer object can be obtained by passing this integer value to ILayerMgr::GetLayerById or ILayerMgr::IGetLayerById . |
| layerOverride | Integer with bit flags set to determine which properties, if any, have been overridden with respect to the layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if layerOverride was returned as 3, we know the color and style have been specifically set for this annotation and might not match the default values associated with this annotations layer. |

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::IGetVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetVisualProperties.html)

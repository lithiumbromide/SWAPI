---
title: "GetBkgdImageDisplayAreaAspectRatio Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetBkgdImageDisplayAreaAspectRatio"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetBkgdImageDisplayAreaAspectRatio.html"
---

# GetBkgdImageDisplayAreaAspectRatio Method (IModelView)

Gets the aspect ratio (width/height) of the area of the window where the background image is displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBkgdImageDisplayAreaAspectRatio() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

value = instance.GetBkgdImageDisplayAreaAspectRatio()
```

### C#

```csharp
System.double GetBkgdImageDisplayAreaAspectRatio()
```

### C++/CLI

```cpp
System.double GetBkgdImageDisplayAreaAspectRatio();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Aspect ratio (width/height) of the area of the window where the background image is displayed, or -1 if there is no background image or if the image covers the entire window

## VBA Syntax

See [ModelView::GetBkgdImageDisplayAreaAspectRatio](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetBkgdImageDisplayAreaAspectRatio.html).

## Remarks

For use with ray-trace rendering engines to match SOLIDWORKS' display.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

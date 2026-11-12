---
title: "IGetDimension Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IGetDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetDimension.html"
---

# IGetDimension Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::GetDimension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetDimension2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDimension() As Dimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As Dimension

value = instance.IGetDimension()
```

### C#

```csharp
Dimension IGetDimension()
```

### C++/CLI

```cpp
Dimension^ IGetDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to an [IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object

## VBA Syntax

See [DisplayDimension::IGetDimension](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IGetDimension.html).

## Remarks

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object in the SOLIDWORKS API.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension.html)
[IFeature::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.html)
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.html)
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.html)
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.html)

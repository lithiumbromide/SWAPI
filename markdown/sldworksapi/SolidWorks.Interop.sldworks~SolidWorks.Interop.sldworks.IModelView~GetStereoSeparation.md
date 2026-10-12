---
title: "GetStereoSeparation Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetStereoSeparation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetStereoSeparation.html"
---

# GetStereoSeparation Method (IModelView)

Obsolete and not superseded. Functionality no longer implemented.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStereoSeparation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Object

value = instance.GetStereoSeparation()
```

### C#

```csharp
System.object GetStereoSeparation()
```

### C++/CLI

```cpp
System.Object^ GetStereoSeparation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 2 doubles representing the stereo magnitude and stereo parallax balance settings

## VBA Syntax

See [ModelView::GetStereoSeparation](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetStereoSeparation.html).

## Remarks

This method checks the two stereoscopic display values which can be set by using [IModelView::SetStereoSeparation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~SetStereoSeparation.html) or [IModelView::ISetStereoSeparation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~ISetStereoSeparation.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

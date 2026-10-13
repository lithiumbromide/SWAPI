---
title: "SetDual Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetDual"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual.html"
---

# SetDual Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::SetDual2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetDual2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDual( _
   ByVal UseDoc As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean

instance.SetDual(UseDoc)
```

### C#

```csharp
void SetDual(
   System.bool UseDoc
)
```

### C++/CLI

```cpp
void SetDual(
   System.bool UseDoc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting, false uses the opposite of the document setting (see **Remarks**)

## VBA Syntax

See [DisplayDimension::SetDual](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetDual.html).

## Remarks

Dual dimensions can use either the same top, bottom, right, or left setting as the document or an opposite top, bottom, right, or left setting. This method allows you to set a dual dimension to use the current document setting or the opposite setting.

Use [IDisplayDimension::GetUseDocDual](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocDual.html) to get the current value of this setting.

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.html)

## Availability

SOLIDWORKS 99, datecode 1999207

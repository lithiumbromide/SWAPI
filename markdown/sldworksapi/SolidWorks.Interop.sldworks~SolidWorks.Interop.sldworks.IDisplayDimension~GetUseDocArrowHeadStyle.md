---
title: "GetUseDocArrowHeadStyle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocArrowHeadStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle.html"
---

# GetUseDocArrowHeadStyle Method (IDisplayDimension)

Gets whether this display dimension uses the document default setting for dimension arrowhead style.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocArrowHeadStyle() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocArrowHeadStyle()
```

### C#

```csharp
System.bool GetUseDocArrowHeadStyle()
```

### C++/CLI

```cpp
System.bool GetUseDocArrowHeadStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension uses the document setting, false if it uses the local display dimension setting

## VBA Syntax

See [DisplayDimension::GetUseDocArrowHeadStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocArrowHeadStyle.html).

## Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. This method gets the setting that indicates which setting is currently in use.

Use [IDisplayDimension::SetArrowHeadStyle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.html) to set this value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetArrowHeadStyle2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2.html)

## Availability

SOLIDWORKS 99, datecode 1999207

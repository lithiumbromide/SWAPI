---
title: "CenterText Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "CenterText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~CenterText.html"
---

# CenterText Property (IDisplayDimension)

Gets or sets whether the text of this display dimension should be automatically centered.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenterText As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.CenterText = value

value = instance.CenterText
```

### C#

```csharp
System.bool CenterText {get; set;}
```

### C++/CLI

```cpp
property System.bool CenterText {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True centers the text, false does not center the text

## VBA Syntax

See [DisplayDimension::CenterText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~CenterText.html).

## Remarks

Dimension text must be positioned somewhere between the two dimensioned points in order to be centered.

| In a... | The two points are the... |
| --- | --- |
| linear dimension | the end points of the dimension |
| diameter dimension | the end points of the dimension line lying on the arc. |
| radius dimension | the center point and the dimension line end point lying on the arc |

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)

## Availability

SOLIDWORKS 99, datecode 1999207

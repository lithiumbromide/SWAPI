---
title: "OffsetText Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "OffsetText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~OffsetText.html"
---

# OffsetText Property (IDisplayDimension)

Gets or sets whether or not to offset the text of a dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetText As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.OffsetText = value

value = instance.OffsetText
```

### C#

```csharp
System.bool OffsetText {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetText {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the dimension text, false to not

## VBA Syntax

See [DisplayDimension::OffsetText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~OffsetText.html).

## Remarks

| If this property is set to... | Then... |
| --- | --- |
| True | Dimension text is attached to the end of a leader that can be moved about freely. Dimension line and extension lines to which the dimension text is associated do not move. |
| false | Dimension text is displayed on the dimension line. Dimension line and extension lines can move when the dimension text is moved. |

Because radial and diametric dimensions are already attached to the end of a leader, this property is not available for these types of dimensions.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4

---
title: "GetLinkedText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetLinkedText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.html"
---

# GetLinkedText Method (IDisplayDimension)

Gets the text linked to this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkedText() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.String

value = instance.GetLinkedText()
```

### C#

```csharp
System.string GetLinkedText()
```

### C++/CLI

```cpp
System.String^ GetLinkedText();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Text linked to this display dimension

## VBA Syntax

See [DisplayDimension::GetLinkedText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetLinkedText.html).

## Examples

[Get Linked Dimensions (VBA)](Get_Linked_Dimensions_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.html)
[IDisplayDimension::Unlink Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.html)
[IDisplayDimension::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0

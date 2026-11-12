---
title: "GetSupportsGenericText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetSupportsGenericText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSupportsGenericText.html"
---

# GetSupportsGenericText Method (IDisplayDimension)

Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSupportsGenericText() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetSupportsGenericText()
```

### C#

```csharp
System.bool GetSupportsGenericText()
```

### C++/CLI

```cpp
System.bool GetSupportsGenericText();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the display dimension was created in SOLIDWORKS 2011 or later and is generic text, false if the display dimension was created in an earlier release of SOLIDWORKS and is dimension text

## VBA Syntax

See [DisplayDimension::GetSupportsGenericText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetSupportsGenericText.html).

## Examples

[Get SOLIDWORKS Version of Display Dimension (C#)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_CSharp.htm)
[Get SOLIDWORKS Version of Display Dimension (VB.NET)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VBNET.htm)
[Get SOLIDWORKS Version of Display Dimension (VBA)](Get_SOLIDWORKS_Version_of_Display_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2011 SP4, Revision 19.4

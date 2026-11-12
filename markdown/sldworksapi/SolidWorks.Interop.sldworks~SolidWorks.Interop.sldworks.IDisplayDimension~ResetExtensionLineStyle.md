---
title: "ResetExtensionLineStyle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ResetExtensionLineStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.html"
---

# ResetExtensionLineStyle Method (IDisplayDimension)

Resets the style of the specified extension line.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResetExtensionLineStyle( _
   ByVal ExtIndex As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim ExtIndex As System.Short
Dim value As System.Boolean

value = instance.ResetExtensionLineStyle(ExtIndex)
```

### C#

```csharp
System.bool ResetExtensionLineStyle(
   System.short ExtIndex
)
```

### C++/CLI

```cpp
System.bool ResetExtensionLineStyle(
   System.short ExtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExtIndex`: Index of extension line

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::ResetExtensionLineStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ResetExtensionLineStyle.html).

## Remarks

Call this method to reset the extension line style if you previously called [IDisplayDimension::SetExtensionLineAsCenterline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetExtensionLineAsCenterline.html) to set the extension line as a centerline. This method corresponds to the extension line's shortcut menu item **Reset extension line style**, which appears after you select the extension line's shortcut menu item **Set extension line as centerline**.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html)
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.html)
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

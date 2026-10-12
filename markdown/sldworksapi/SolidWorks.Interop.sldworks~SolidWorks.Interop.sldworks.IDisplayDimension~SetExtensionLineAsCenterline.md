---
title: "SetExtensionLineAsCenterline Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetExtensionLineAsCenterline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetExtensionLineAsCenterline.html"
---

# SetExtensionLineAsCenterline Method (IDisplayDimension)

Sets whether the specified extension line is a centerline.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtensionLineAsCenterline( _
   ByVal ExtIndex As System.Short, _
   ByVal Centerline As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim ExtIndex As System.Short
Dim Centerline As System.Boolean
Dim value As System.Boolean

value = instance.SetExtensionLineAsCenterline(ExtIndex, Centerline)
```

### C#

```csharp
System.bool SetExtensionLineAsCenterline(
   System.short ExtIndex,
   System.bool Centerline
)
```

### C++/CLI

```cpp
System.bool SetExtensionLineAsCenterline(
   System.short ExtIndex,
   System.bool Centerline
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExtIndex`: Index of extension line to set
- `Centerline`: True to make extension line a centerline, false to not

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::SetExtensionLineAsCenterline](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetExtensionLineAsCenterline.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

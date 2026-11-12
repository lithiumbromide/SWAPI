---
title: "GetExtensionLineAsCenterline Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetExtensionLineAsCenterline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetExtensionLineAsCenterline.html"
---

# GetExtensionLineAsCenterline Method (IDisplayDimension)

Gets whether the specified extension line is a centerline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtensionLineAsCenterline( _
   ByVal ExtIndex As System.Short, _
   ByRef Centerline As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim ExtIndex As System.Short
Dim Centerline As System.Boolean
Dim value As System.Boolean

value = instance.GetExtensionLineAsCenterline(ExtIndex, Centerline)
```

### C#

```csharp
System.bool GetExtensionLineAsCenterline(
   System.short ExtIndex,
   out System.bool Centerline
)
```

### C++/CLI

```cpp
System.bool GetExtensionLineAsCenterline(
   System.short ExtIndex,
   [Out] System.bool Centerline
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExtIndex`: Index of extension line
- `Centerline`: True if the extension line is a centerline, false if not

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::GetExtensionLineAsCenterline](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetExtensionLineAsCenterline.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

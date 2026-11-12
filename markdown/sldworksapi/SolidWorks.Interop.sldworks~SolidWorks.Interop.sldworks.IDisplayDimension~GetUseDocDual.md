---
title: "GetUseDocDual Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocDual"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual.html"
---

# GetUseDocDual Method (IDisplayDimension)

Gets whether this display dimension uses the document setting for positioning dual dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocDual() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocDual()
```

### C#

```csharp
System.bool GetUseDocDual()
```

### C++/CLI

```cpp
System.bool GetUseDocDual();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension uses its dual dimension's top, bottom, right, or left document setting, false if the display dimension uses a setting opposite of the dual dimension's top, bottom, right, or left document setting

## VBA Syntax

See [DisplayDimension::GetUseDocDual](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocDual.html).

## Remarks

Use [IDisplayDimension::SetDual](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetDual.html) to set the dual dimension's top, bottom, right, or left setting for this display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.html)

## Availability

SOLIDWORKS 99, datecode 1999207

---
title: "ConvertFormat Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "ConvertFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~ConvertFormat.html"
---

# ConvertFormat Method (IGtol)

Converts this Gtol to the current format.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertFormat() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Integer

value = instance.ConvertFormat()
```

### C#

```csharp
System.int ConvertFormat()
```

### C++/CLI

```cpp
System.int ConvertFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

0 if successfully converted, otherwise error code as defined by [swGtolFormatConversionError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatConversionError_e.html)

## VBA Syntax

See [Gtol::ConvertFormat](ms-its:sldworksapivb6.chm::/sldworks~Gtol~ConvertFormat.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

Before calling this method, use [IGtol::CanConvertFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~CanConvertFormat.html) to determine whether conversion is possible.

If unsupported data are in this older Gtol, then this method will fail.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

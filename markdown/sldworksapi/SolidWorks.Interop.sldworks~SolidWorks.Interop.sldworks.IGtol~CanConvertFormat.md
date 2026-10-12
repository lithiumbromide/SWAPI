---
title: "CanConvertFormat Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "CanConvertFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~CanConvertFormat.html"
---

# CanConvertFormat Method (IGtol)

Gets whether this Gtol can be converted to the current format.

## Syntax

### Visual Basic (Declaration)

```vb
Function CanConvertFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.CanConvertFormat()
```

### C#

```csharp
System.bool CanConvertFormat()
```

### C++/CLI

```cpp
System.bool CanConvertFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if can be converted, false if not

## VBA Syntax

See [Gtol::CanConvertFormat](ms-its:sldworksapivb6.chm::/sldworks~Gtol~CanConvertFormat.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

If this method returns true, call [IGtol::ConvertFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~ConvertFormat.html) to convert the Gtol to the current format.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

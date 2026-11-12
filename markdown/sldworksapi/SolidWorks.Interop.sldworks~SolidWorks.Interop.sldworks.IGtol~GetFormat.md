---
title: "GetFormat Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFormat.html"
---

# GetFormat Method (IGtol)

Gets the format type of this Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFormat() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Integer

value = instance.GetFormat()
```

### C#

```csharp
System.int GetFormat()
```

### C++/CLI

```cpp
System.int GetFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of Gtol format as defined by [swGtolFormatType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatType_e.html)

## VBA Syntax

See [Gtol::GetFormat](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFormat.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

---
title: "GetUseMisalignedDeviationDocumentProperty Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetUseMisalignedDeviationDocumentProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.html"
---

# GetUseMisalignedDeviationDocumentProperty Method (IMate2)

Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseMisalignedDeviationDocumentProperty() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.GetUseMisalignedDeviationDocumentProperty()
```

### C#

```csharp
System.bool GetUseMisalignedDeviationDocumentProperty()
```

### C++/CLI

```cpp
System.bool GetUseMisalignedDeviationDocumentProperty();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to use the document property value for maximum misalignment deviation, false to not

## VBA Syntax

See [Mate2::GetUseMisalignedDeviationDocumentProperty](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetUseMisalignedDeviationDocumentProperty.html).

## Remarks

If this method returns false, then the maximum deviation used is returned by [IMate2::GetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::SetUseMisalignedDeviationDocumentProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

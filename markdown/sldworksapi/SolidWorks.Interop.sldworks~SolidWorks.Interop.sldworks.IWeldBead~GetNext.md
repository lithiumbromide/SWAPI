---
title: "GetNext Method (IWeldBead)"
project: "SOLIDWORKS API Help"
interface: "IWeldBead"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.html"
---

# GetNext Method (IWeldBead)

Gets the next weld bead annotation in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As WeldBead
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldBead
Dim value As WeldBead

value = instance.GetNext()
```

### C#

```csharp
WeldBead GetNext()
```

### C++/CLI

```cpp
WeldBead^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [weld bead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead.html)

## VBA Syntax

See [WeldBead::GetNext](ms-its:sldworksapivb6.chm::/sldworks~WeldBead~GetNext.html).

## Examples

See the [IWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html) examples.

## See Also

[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IWeldBead Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead_members.html)
[IView::GetFirstWeldBead Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.html)
[IWeldBead::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetAnnotation.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "GetDetailView Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetDetailView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetDetailView.html"
---

# GetDetailView Method (IDetailCircle)

Gets the drawing view of this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetailView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As View

value = instance.GetDetailView()
```

### C#

```csharp
View GetDetailView()
```

### C++/CLI

```cpp
View^ GetDetailView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) that owns this detail circle

## VBA Syntax

See [DetailCircle::GetDetailView](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetDetailView.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

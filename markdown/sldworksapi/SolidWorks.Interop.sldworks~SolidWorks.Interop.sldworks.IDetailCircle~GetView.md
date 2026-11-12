---
title: "GetView Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetView.html"
---

# GetView Method (IDetailCircle)

Gets the the drawing view that displays this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As View

value = instance.GetView()
```

### C#

```csharp
View GetView()
```

### C++/CLI

```cpp
View^ GetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [DetailCircle::GetView](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetView.html).

## Remarks

This is the owning drawing view from which the detail view was derived.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision number 9.0

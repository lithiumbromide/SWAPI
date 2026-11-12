---
title: "Sheet Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Sheet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Sheet.html"
---

# Sheet Property (IView)

Gets the sheet on which this drawing view exists.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sheet As Sheet
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Sheet

value = instance.Sheet
```

### C#

```csharp
Sheet Sheet {get;}
```

### C++/CLI

```cpp
property Sheet^ Sheet {
   Sheet^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html)

## VBA Syntax

See [View::Sheet](ms-its:sldworksapivb6.chm::/sldworks~View~Sheet.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

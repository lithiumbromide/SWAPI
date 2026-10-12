---
title: "IGetView Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetView.html"
---

# IGetView Method (IDrSection)

Gets the drawing view where the section line appears.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As View

value = instance.IGetView()
```

### C#

```csharp
View IGetView()
```

### C++/CLI

```cpp
View^ IGetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) where the section line appears

## VBA Syntax

See [DrSection::IGetView](ms-its:sldworksapivb6.chm::/sldworks~DrSection~IGetView.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetView.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

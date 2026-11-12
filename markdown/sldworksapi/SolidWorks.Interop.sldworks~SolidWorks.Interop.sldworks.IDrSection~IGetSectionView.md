---
title: "IGetSectionView Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetSectionView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetSectionView.html"
---

# IGetSectionView Method (IDrSection)

Gets the section view of this section cut.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSectionView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As View

value = instance.IGetSectionView()
```

### C#

```csharp
View IGetSectionView()
```

### C++/CLI

```cpp
View^ IGetSectionView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the section [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) of this section cut

## VBA Syntax

See [DrSection::IGetSectionView](ms-its:sldworksapivb6.chm::/sldworks~DrSection~IGetSectionView.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetSectionView.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

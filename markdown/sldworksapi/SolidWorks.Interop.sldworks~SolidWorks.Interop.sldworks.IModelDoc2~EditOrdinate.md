---
title: "EditOrdinate Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditOrdinate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditOrdinate.html"
---

# EditOrdinate Method (IModelDoc2)

Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditOrdinate()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.EditOrdinate()
```

### C#

```csharp
void EditOrdinate()
```

### C++/CLI

```cpp
void EditOrdinate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::EditOrdinate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditOrdinate.html).

## Remarks

You must pre-select the existing ordinate dimension and the entities to which to dimension. The position of the text and type of ordinate is determined by the existing ordinate dimension.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.html)
[IModelDoc2::ReattachOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReattachOrdinate.html)
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

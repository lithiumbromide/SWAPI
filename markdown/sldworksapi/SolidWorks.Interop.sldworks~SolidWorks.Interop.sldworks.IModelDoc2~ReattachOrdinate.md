---
title: "ReattachOrdinate Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ReattachOrdinate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReattachOrdinate.html"
---

# ReattachOrdinate Method (IModelDoc2)

Reattaches an ordinate dimension to a different entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReattachOrdinate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.ReattachOrdinate()
```

### C#

```csharp
System.bool ReattachOrdinate()
```

### C++/CLI

```cpp
System.bool ReattachOrdinate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the re-attachment is successful, false if not

## VBA Syntax

See [ModelDoc2::ReattachOrdinate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ReattachOrdinate.html).

## Remarks

To use this method, you must first select the dimension to reattach and then call to [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) must be made that selects the new entity to which this dimension will be attached.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)
[IModelDoc2::EditOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditOrdinate.html)
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

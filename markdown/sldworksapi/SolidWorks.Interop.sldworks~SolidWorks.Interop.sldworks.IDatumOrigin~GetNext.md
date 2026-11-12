---
title: "GetNext Method (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext.html"
---

# GetNext Method (IDatumOrigin)

Gets the next datum origin in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As DatumOrigin
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As DatumOrigin

value = instance.GetNext()
```

### C#

```csharp
DatumOrigin GetNext()
```

### C++/CLI

```cpp
DatumOrigin^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [datum origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin.html) in the view

## VBA Syntax

See [DatumOrigin::GetNext](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~GetNext.html).

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)
[IView::GetFirstDatumOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin.html)
[IAnnotation::GetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html)
[IAnnotation::IGetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)
[IHoleTable::DatumOrigin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~DatumOrigin.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
